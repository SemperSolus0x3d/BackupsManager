import inject
import sys
import subprocess as sp

from .ResticDiscoveryService import ResticDiscoveryService
from .SingleInstanceLockService import SingleInstanceLockService
from .exceptions import ResticCallFailedException

class ResticCallService:
    @inject.autoparams()
    def __init__(
        self,
        resticDiscoveryService: ResticDiscoveryService,
        lockService: SingleInstanceLockService
    ):
        self._resticDiscoveryService = resticDiscoveryService
        self._lockService = lockService

    def callRestic(self, args: list[str]):
        with self._lockService.lock():
            process = sp.Popen(
                [ self._resticDiscoveryService.resticPath, *args ],
                stdout=sys.stdout,
                stderr=sp.PIPE
            )

            returncode = process.wait()

            if returncode != 0:
                stderr = process.stderr.read().decode("utf-8")
                raise ResticCallFailedException(stderr)
