import inject

from .DIConfigurer import DIConfigurer as _DIConfigurer
from .LoggingConfigurer import LoggingConfigurer as _LoggingConfigurer

from .BackupService import BackupService
from .RepoIntegrityCheckService import RepoIntegrityCheckService
from .CopySnapshotsService import CopySnapshotsService

_DIConfigurer().configure()
inject.instance(_LoggingConfigurer).configure()
