from contextlib import contextmanager

class SingleInstanceLockService:
    @property
    def isLockAcquired(self):
        return self._locksCount != 0

    def __init__(self):
        self._locksCount = 0

    @contextmanager
    def lock(self):
        if self._locksCount == 0:
            self._acquireLock()

        self._locksCount += 1

        try:
            yield
        finally:
            self._locksCount -= 1

            if self._locksCount == 0:
                self._releaseLock()

    def _acquireLock(self):
        raise NotImplementedError()

    def _releaseLock(self):
        raise NotImplementedError()
