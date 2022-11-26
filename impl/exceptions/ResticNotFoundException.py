class ResticNotFoundException(Exception):
    def __init__(self):
        super().__init__('Restic not found')
