import inject
import platform

from .ResticCallService import ResticCallService
from .RepoPasswordService import RepoPasswordService
from .Config import Config
from .Path import Path
from .exceptions import UnsupportedOperationException

class MountService:
    @inject.autoparams()
    def __init__(
        self,
        config: Config,
        resticCallService: ResticCallService,
        passwordService: RepoPasswordService
    ):
        self._config = config
        self._resticCallService = resticCallService
        self._passwordService = passwordService

    def mountRepo(self):
        self._checkPlatform()
        self._passwordService.passRepoPassword()
        self.mountRepo(
            self._config.repositoryPath,
            self._config.repoMountpoint
        )

    def mountUsbRepo(self):
        self._checkPlatform()
        self._passwordService.passUsbRepoPassword()
        self.mountRepo(
            self._config.usbRepositoryPath,
            self._config.usbRepoMountpoint
        )

    def _mount(self, repoPath: Path, mountpoint: Path):
        self._resticCallService.callRestic([
            'mount',
            '-r', repoPath.path,
            '--allow-other',
            mountpoint.path
        ])

    def _checkPlatform(self):
        if platform.system() == 'Windows':
            raise UnsupportedOperationException(
                'Mounting repository is not supported on Windows'
            )
