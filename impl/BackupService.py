import os
import tempfile
import subprocess
import inject
import logging as log

from .Config import Config
from .Path import Path

class BackupService:
    _EXCLUDES_FILE_NAME = 'excludes.txt'
    _IEXCLUDES_FILE_NAME = 'iexcludes.txt'
    _INCLUDE_PATTERNS_FILE_NAME = 'includePatterns.txt'
    _INCLUDE_PATHS_FILE_NAME = 'includePaths.txt'
    _PASSWORD_FILE_NAME = 'password.txt'

    @inject.autoparams()
    def __init__(self, config: Config):
        self._config = config

    def makeBackup(self):
        self._setPassword()

        with tempfile.TemporaryDirectory() as tempDir:
            self._writeFiles(tempDir)
            self._runRestic(tempDir)

    def _setPassword(self):
        os.environ['RESTIC_PASSWORD'] = self._config.repositoryPassword

    def _writeFiles(self, tempDirPath: str):
        def makePath(filename: str):
            return os.path.join(tempDirPath, filename)

        args = [
            (self._config.excludes, makePath(self._EXCLUDES_FILE_NAME)),
            (self._config.iexcludes, makePath(self._IEXCLUDES_FILE_NAME)),
            (self._config.includePatterns, makePath(self._INCLUDE_PATTERNS_FILE_NAME)),
            (self._config.includePaths, makePath(self._INCLUDE_PATHS_FILE_NAME), '\0')
        ]

        for argsTuple in args:
            self._writePaths(*argsTuple)

    def _writePaths(self, paths: list[Path], tempFilePath: str, lineSep: str = '\n'):
        self._writeLines((x.path for x in paths), tempFilePath, lineSep)

    def _writeLines(self, lines: list[str], tempFilePath: str, lineSep: str = '\n'):
        with open(tempFilePath, 'w', encoding='utf-8') as file:
            file.writelines(x + lineSep for x in lines)


    def _runRestic(self, tempDirPath: str):
        def makePath(filename: str):
            return os.path.join(tempDirPath, filename)

        subprocess.run([
            'restic',
            '-r', self._config.repositoryPath.path, # repo path
            '--exclude-file', makePath(self._EXCLUDES_FILE_NAME), # excludes file path
            '--iexclude-file', makePath(self._IEXCLUDES_FILE_NAME), # case-insensitive excludes file path
            '--files-from', makePath(self._INCLUDE_PATTERNS_FILE_NAME), # include patterns file path
            '--files-from-raw', makePath(self._INCLUDE_PATHS_FILE_NAME), # include paths file path
            '--verbose',
            'backup'
        ])
