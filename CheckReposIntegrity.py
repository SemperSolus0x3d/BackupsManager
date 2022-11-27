import inject

from impl import RepoIntegrityCheckService, TopLevelExceptionHandler

if __name__ == '__main__':
    with inject.instance(TopLevelExceptionHandler).handleExceptions():
        inject.instance(RepoIntegrityCheckService).checkAllReposIntegrity()
