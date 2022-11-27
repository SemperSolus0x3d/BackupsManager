class ResticCallFailedException(Exception):
    def __init__(self, stderr: str):
        super().__init__(f'Restic call failed. Error: {stderr}')
