import inject
import os
import logging as log

from .Config import Config
from .Path import Path
from .ResticCallService import ResticCallService
from .RepoPasswordService import RepoPasswordService

class RepoIntegrityCheckService:
    @inject.autoparams()
    def __init__(
        self,
        config: Config,
        resticCallService: ResticCallService,
        repoPasswordService: RepoPasswordService
    ) -> None:
        self._config = config
        self._resticCallService = resticCallService
        self._passwordService = repoPasswordService

    def checkRepoIntegrity(self):
        self._passwordService.passRepoPassword()

        path = self._config.repositoryPath

        log.info(f'Checking repo integrity. Path: "{path.path}"')
        self._runRestic(path)

    def checkUsbRepoIntegrity(self):
        self._passwordService.passUsbRepoPassword()

        path = self._config.usbRepositoryPath

        log.info(f'Checking USB drive repo integrity. Path: "{path.path}"')
        self._runRestic(path)

    def checkAllReposIntegrity(self):
        repoPath = self._config.repositoryPath.path
        usbRepoPath = self._config.usbRepositoryPath.path

        if os.path.isdir(repoPath):
            self.checkRepoIntegrity()
        else:
            log.warning(f'Repository not found. Path: "{repoPath}"')

        if os.path.isdir(usbRepoPath):
            self.checkUsbRepoIntegrity()
        else:
            log.warning(f'USB drive repository not found. Path: "{usbRepoPath}"')

    def _runRestic(self, repoPath: Path):
        self._resticCallService.callRestic([
            '-r', repoPath.path,
            'check'
        ])
