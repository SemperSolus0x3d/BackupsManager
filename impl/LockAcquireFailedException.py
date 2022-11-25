class LockAcquireFailedException(Exception):
    def __init__(self):
        super().__init__('Single instance lock acquire failed')
