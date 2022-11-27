import inject
from impl import CopySnapshotsService, TopLevelExceptionHandler

if __name__ == '__main__':
    with inject.instance(TopLevelExceptionHandler).handleExceptions():
        inject.instance(CopySnapshotsService).copySnapshotsToUsbRepo()
