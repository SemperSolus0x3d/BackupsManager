import toml
from Params import Params
from Config import Config
from Path import Path


class ConfigService:
    @property
    def config(self):
        return self._config

    def __init__(self, params: Params):
        rawConfig = self._readRawConfig(params.configPath)
        self._config = self._createConfig(rawConfig)


    def _readRawConfig(self, configPath):
        return toml.load(configPath)


    def _createConfig(self, rawConfig):
        placeholders = rawConfig['placeholders']

        excludes = self._toPaths(rawConfig['excludes'], placeholders)
        iexcludes = self._toPaths(rawConfig['iexcludes'], placeholders)
        includePatterns = self._toPaths(rawConfig['includePatterns'], placeholders)
        includePaths = self._toPaths(rawConfig['includePaths'], placeholders)

        return Config(
            excludes=excludes,
            iexcludes=iexcludes,
            includePatterns=includePatterns,
            includePaths=includePaths,
            repositoryPassword=rawConfig['repositoryPassword'],
            usbRepositoryPassword=rawConfig['usbRepositoryPassword'],
        )

    def _toPaths(self, componentsLists: list[list[str]], placeholders: dict[str, str]):
        paths = []

        for componentsList in componentsLists:
            paths.append(Path(x.format(**placeholders) for x in componentsList))

        return paths
