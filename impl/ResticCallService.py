import inject
import subprocess

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
            result: subprocess.CompletedProcess[str] = subprocess.run([
                self._resticDiscoveryService.resticPath, *args
            ])

        try:
            result.check_returncode()
        except subprocess.CalledProcessError as ex:
            raise ResticCallFailedException() from ex
