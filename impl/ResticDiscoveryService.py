import inject
from shutil import which

from .Config import Config

class ResticDiscoveryService:
    @inject.autoparams()
    def __init__(self, config: Config):
        self._config = config

    def getResticPath(self):
        if self._config.resticPath is not None:
            return self._config.resticPath

        return which('restic')
