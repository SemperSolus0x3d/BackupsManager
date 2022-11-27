import traceback
import logging as log
from contextlib import contextmanager

class TopLevelExceptionHandler:
    @contextmanager
    def handleExceptions(self):
        try:
            yield
        except Exception as ex:
            log.critical(ex)
            log.debug(''.join(traceback.format_exception(ex)))
