from contextlib import contextmanager

class SingleInstanceLockService:
    @property
    def isLockAcquired(self):
        return self._isLockAcquired

    def __init__(self):
        self._isLockAcquired = False

    @contextmanager
    def lock(self):
        isLockAcquired = self._isLockAcquired

        if not isLockAcquired:
            self._acquireLock()

        try:
            yield
        finally:
            if not isLockAcquired:
                self._releaseLock()

    def _acquireLock(self):
        raise NotImplementedError()

    def _releaseLock(self):
        raise NotImplementedError()
