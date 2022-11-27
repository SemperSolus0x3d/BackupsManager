import inject
import sys
import logging as log
from typing import Union

from .Params import Params

def _logTraceGlobal(msg, *args, **kwargs):
    log.getLogger().trace(msg, *args, **kwargs)

def _logTrace(self, msg, *args, **kwargs):
    self.log(log.TRACE, msg, *args, **kwargs)


class LoggingConfigurer:
    def preconfigure(self):
        setattr(log, 'TRACE', log.DEBUG - 1)
        setattr(log.getLoggerClass(), 'trace', _logTrace)
        setattr(log, 'trace', _logTraceGlobal)

        log.addLevelName(log.TRACE, 'TRACE')

    @inject.autoparams()
    def configure(self, params: Params):
        log.basicConfig(
            format='{asctime} [{levelname}]: {message}',
            style='{',
            level=params.logLevel,
            stream=sys.stderr
        )
