import os
import re
import inject
import subprocess as sp
import logging as log
from shutil import which

from .exceptions import ResticNotFoundException, ResticCallFailedException
from .Config import Config
from .ResticVersion import ResticVersion

class ResticDiscoveryService:
    @inject.autoparams()
    def __init__(self, config: Config):
        self._config = config
        self._resticPath = None
        self._resticVersion = None

    @property
    def resticPath(self):
        if self._resticPath is None:
            self._resticPath = self._getResticPath()

        return self._resticPath

    @property
    def resticVersion(self):
        if self._resticVersion is None:
            self._resticVersion = self._getResticVersion()

        return self._resticVersion

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

    def _getResticVersion(self):
        process = sp.Popen(
            [ self.resticPath, 'version' ],
            stdout=sp.PIPE,
            stderr=sp.PIPE
        )

        returncode = process.wait()

        if returncode != 0:
            raise ResticCallFailedException(process.stderr.read().decode('utf-8'))

        match: re.Match[str] = re.match(
            r'restic ([0-9]+)\.([0-9]+)\.([0-9]+)',
            process.stdout.read().decode('utf-8')
        )

        if match is None:
            raise ResticNotFoundException()

        version = ResticVersion(
            match.group(1),
            match.group(2),
            match.group(3)
        )

        log.info(f'Restic version is {version}')

        return version
