import inject
from impl import BackupService

if __name__ == '__main__':
    inject.instance(BackupService).makeBackupToUsbRepo()
