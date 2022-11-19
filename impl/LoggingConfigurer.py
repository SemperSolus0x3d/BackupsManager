import inject
import sys
import logging as log

from .Params import Params

class LoggingConfigurer:
    @inject.autoparams()
    def __init__(self, params: Params):
        self._params = params

    def configure(self):
        log.basicConfig(
            format='{asctime} [{levelname}]: {message}',
            style='{',
            level=self._params.logLevel,
            stream=sys.stderr
        )
