import sys
import logging as log

from Params import Params

class ParamsService:
    def __init__(self):
        self._parseParams()

    @property
    def params(self):
        return self._params

    def _parseParams(self):
        def pairwise(iterable):
            a = iter(iterable)
            return zip(a, a)

        result = Params()

        for p, v in pairwise(sys.argv[1:]):
            match p:
                case '-c' | '--config':
                    result.configPath = v
                case '-l' | '--log-level':
                    result.logLevel = self._getLogLevel(v)

        self._params = result

    def _getLogLevel(self, level_name: str):
        nameToLevelMap = { k.casefold(): v for k, v in {
            'debug': log.DEBUG,
            'info': log.INFO,
            'warning': log.WARNING,
            'error': log.ERROR,
            'critical': log.CRITICAL
        }.items() }

        try:
            return nameToLevelMap[level_name.casefold()]
        except KeyError as ex:
            raise RuntimeError(f'Invalid log level: "{level_name}"') from ex
