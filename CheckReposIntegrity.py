import inject

from impl import RepoIntegrityCheckService

if __name__ == '__main__':
    inject.instance(RepoIntegrityCheckService).checkAllReposIntegrity()
