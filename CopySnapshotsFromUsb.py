import inject
from impl import CopySnapshotsService

if __name__ == '__main__':
    inject.instance(CopySnapshotsService).copySnapshotsFromUsbRepo()
