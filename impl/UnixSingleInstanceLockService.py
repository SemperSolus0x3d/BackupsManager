import fcntl
import os
import logging as log
from .exceptions import LockAcquireFailedException
from .SingleInstanceLockService import SingleInstanceLockService

class UnixSingleInstanceLockService(SingleInstanceLockService):
    _LOCK_FOLDER = 'locks'
    _LOCK_NAME = 'single-instance-lock.lock'
    _LOCK_PATH = os.path.join(_LOCK_FOLDER, _LOCK_NAME)

    def __init__(self):
        self._file = None

        super().__init__()

    def _acquireLock(self):
        self._ensureLocksFolderExists()

        self._file = open(self._LOCK_PATH, 'w')

        try:
            fcntl.flock(self._file, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise LockAcquireFailedException()

    def _releaseLock(self):
        fcntl.flock(self._file, fcntl.LOCK_UN)
        self._file.close()

    def _ensureLocksFolderExists(self):
        if not os.path.isdir(self._LOCK_FOLDER):
            os.makedirs(self._LOCK_FOLDER)
