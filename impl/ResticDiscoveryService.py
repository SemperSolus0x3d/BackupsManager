import os
import inject
import logging as log
from shutil import which

from .exceptions import ResticNotFoundException
from .Config import Config

class ResticDiscoveryService:
    @inject.autoparams()
    def __init__(self, config: Config):
        self._config = config
        self._resticPath = None

    @property
    def resticPath(self):
        if self._resticPath is None:
            self._resticPath = self._getResticPath()

        return self._resticPath

    def _getResticPath(self):
        if self._config.resticPath is not None:
            path = self._config.resticPath.path
            if os.path.exists(path):
                log.info(f'Using restic from config: {path}')
                return path

        path = which('restic')

        if path is not None:
            if os.path.exists(path):
                log.info(f'Using restic from PATH: {path}')
                return path

        raise ResticNotFoundException()
