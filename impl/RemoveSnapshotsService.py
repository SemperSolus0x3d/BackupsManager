import inject
import os
import logging as log

from .Path import Path
from .Config import Config
from .ResticCallService import ResticCallService
from .RepoPasswordService import RepoPasswordService

class RemoveSnapshotsService:
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

    def removeOldSnapshots(self):
        args = self.createArgs(self._config.repositoryPath)

        self._passwordService.passRepoPassword()
        self.callRestic(args)

    def removeOldSnapshotsFromUsbRepo(self):
        args = self.createArgs(self._config.usbRepositoryPath)

        self._passwordService.passUsbRepoPassword()
        self.callRestic(args)

    def removeOldSnapshotsFromAllRepos(self):
        path = self._config.repositoryPath
        if os.path.isdir(path.path):
            self.removeOldSnapshots()
        else:
            log.warning(f'Repository not found. Path: {path}')

        path = self._config.usbRepositoryPath

        if os.path.isdir(path.path):
            self.removeOldSnapshotsFromUsbRepo()
        else:
            log.warning(f'USB drive repository not found. Path: {path}')

    def createArgs(self, repoPath: Path):
        args = [
            'forget',
            '-r', repoPath.path,
            '--prune',
            '--keep-tag', 'persistent'
        ]

        if (hourly := self._config.keepHourlySnapshots) > 0:
            args += ['--keep-hourly', str(hourly)]

        if (daily := self._config.keepDailySnapshots) > 0:
            args += ['--keep-daily', str(daily)]

        if (weekly := self._config.keepWeeklySnapshots) > 0:
            args += ['--keep-weekly', str(weekly)]

        if (monthly := self._config.keepMonthlySnapshots) > 0:
            args += ['--keep-monthly', str(monthly)]

        if (yearly := self._config.keepYearlySnapshots) > 0:
            args += ['--keep-yearly', str(yearly)]

        # args.append('forget')
        return args

    def callRestic(self, args: list[str]):
        self._resticCallService.callRestic(args)