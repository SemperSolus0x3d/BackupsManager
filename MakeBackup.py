import inject
from impl import BackupService, TopLevelExceptionHandler

if __name__ == '__main__':
    with inject.instance(TopLevelExceptionHandler).handleExceptions():
        inject.instance(BackupService).makeBackup()
