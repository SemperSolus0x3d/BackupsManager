import inject
from impl import RemoveSnapshotsService, TopLevelExceptionHandler

if __name__ == '__main__':
    with inject.instance(TopLevelExceptionHandler).handleExceptions():
        inject.instance(RemoveSnapshotsService).removeOldSnapshotsFromAllRepos()
