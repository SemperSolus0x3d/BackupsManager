import inject

from .Config import Config
from .Path import Path
from .ResticCallService import ResticCallService
from .RepoPasswordService import RepoPasswordService

class CopySnapshotsService:
    @inject.autoparams()
    def __init__(
        self,
        config: Config,
        resticCallService: ResticCallService,
        repoPasswordService: RepoPasswordService
    ):
        self._config = config
        self._resticCallService = resticCallService
        self._passwordService = repoPasswordService

    def copySnapshotsToUsbRepo(self):
        self._passwordService.passRepoPasswordAsFromRepoPassword()
        self._passwordService.passUsbRepoPassword()

        self._copySnapshots(
            self._config.repositoryPath,
            self._config.usbRepositoryPath
        )

    def copySnapshotsFromUsbRepo(self):
        self._passwordService.passUsbRepoPasswordAsFromRepoPassword()
        self._passwordService.passRepoPassword()

        self._copySnapshots(
            self._config.usbRepositoryPath,
            self._config.repositoryPath
        )

    def _copySnapshots(
        self,
        fromRepoPath: Path,
        toRepoPath: Path
    ):
        self._resticCallService.callRestic([
            '-r', toRepoPath.path,
            '--from-repo', fromRepoPath.path,
            'copy'
        ])
