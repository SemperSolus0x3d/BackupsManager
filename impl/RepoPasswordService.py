import os
import inject

from .Config import Config

class RepoPasswordService:
    @inject.autoparams()
    def __init__(self, config: Config):
        self._config = config

    def passRepoPassword(self):
        self._setPasswordInEnvironment(self.getRepoPassword())

    def passUsbRepoPassword(self):
        self._setPasswordInEnvironment(self.getUsbRepoPassword())

    def getRepoPassword(self):
        return self._config.repositoryPassword

    def getUsbRepoPassword(self):
        return self._config.usbRepositoryPassword

    def _setPasswordInEnvironment(self, password: str):
        os.environ['RESTIC_PASSWORD'] = password
