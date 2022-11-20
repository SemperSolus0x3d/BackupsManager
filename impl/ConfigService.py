import toml
import inject
from .Params import Params
from .Config import Config
from .Path import Path


class ConfigService:
    @property
    def config(self):
        return self._config

    @inject.autoparams()
    def __init__(self, params: Params):
        rawConfig = self._readRawConfig(params.configPath)
        self._config = self._createConfig(rawConfig)


    def _readRawConfig(self, configPath):
        return toml.load(configPath)


    def _createConfig(self, rawConfig):
        placeholders = rawConfig['placeholders']

        def toPathOrNone(components):
            return self._toPathOrNone(components, placeholders)

        def toPath(components):
            return self._toPath(components, placeholders)

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
            repositoryPath=toPath(rawConfig['repositoryPath']),
            usbRepositoryPath=toPath(rawConfig['usbRepositoryPath']),
            resticPath=toPathOrNone(rawConfig['resticPath'])
        )

    def _toPaths(self, componentsLists: list[list[str]], placeholders: dict[str, str]):
        paths = []

        for componentsList in componentsLists:
            paths.append(self._toPath(componentsList, placeholders))

        return paths

    def _toPathOrNone(
            self,
            components: list[str],
            placeholders: dict[str, str]
        ) -> Path | None:
        if len(components) == 0:
            return None

        return self._toPath(components, placeholders)

    def _toPath(self, components: list[str], placeholders: dict[str, str]) -> Path:
        return Path(x.format(**placeholders) for x in components)
