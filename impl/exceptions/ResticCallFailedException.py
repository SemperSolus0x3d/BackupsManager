class ResticCallFailedException(Exception):
    def __init__(self):
        super().__init__('Restic call failed')
