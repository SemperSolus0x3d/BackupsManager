import ctypes
import logging as log
from .exceptions import LockAcquireFailedException
from .SingleInstanceLockService import SingleInstanceLockService

class _Constants:
    FILE_FLAG_FIRST_PIPE_INSTANCE = 0x80000
    ERROR_SUCCESS = 0
    ERROR_ACCESS_DENIED = 5
    PIPE_ACCESS_DUPLEX = 3
    PIPE_NAME = (
        "WL3QV42CLA1SVU3DS4DN4VOAVSBIQI30ML7BO"
        "CK3TFLZLM28ZKQFUQYJI10458MWWKELIQ8A87"
        "TUMJSH0T4OLY6ERFMZAAEZII37UV16SUV4VD3"
        "ULOXLTHYFMPQL65CEAYNRVHPCJTP7V006O0J9"
        "Q13Y8WVXJ7EXWYTH3JLUZB1P10241LU2M8GET"
        "U1TKJ378BCZ49PQ8ITD7C88JJIW9EDD0Z4MUS"
        "XZXIWT2Z6QPA9MFCQ3"
    )

class WindowsSingleInstanceLockService(SingleInstanceLockService):
    def __init__(self):
        self._pipeHandle = None

        super().__init__()

    def _acquireLock(self):
        pipeName = fr'\\.\pipe\{_Constants.PIPE_NAME}'.encode('utf-8')

        self._pipeHandle = ctypes.windll.Kernel32.CreateNamedPipeA(
            pipeName, # pipe name
            _Constants.FILE_FLAG_FIRST_PIPE_INSTANCE |
                _Constants.PIPE_ACCESS_DUPLEX, # create mode
            0, # pipe mode
            2, # max instances count
            10, # output buffer size
            10, # input buffer size,
            0, # default timeout (50ms if 0)
            0, # security attributes
        )

        lastError = ctypes.windll.Kernel32.GetLastError()

        if lastError == _Constants.ERROR_ACCESS_DENIED:
            raise LockAcquireFailedException()

        if lastError != _Constants.ERROR_SUCCESS:
            raise ctypes.WinError(lastError)

    def _releaseLock(self):
        ctypes.windll.Kernel32.CloseHandle(self._pipeHandle)
