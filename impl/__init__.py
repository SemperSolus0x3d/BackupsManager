import inject

from .DIConfigurer import DIConfigurer as _DIConfigurer
from .LoggingConfigurer import LoggingConfigurer as _LoggingConfigurer

from .BackupService import BackupService
from .RepoIntegrityCheckService import RepoIntegrityCheckService
from .CopySnapshotsService import CopySnapshotsService
from .SingleInstanceLockService import SingleInstanceLockService
from .RemoveSnapshotsService import RemoveSnapshotsService
from .TopLevelExceptionHandler import TopLevelExceptionHandler

from .exceptions import *

_DIConfigurer().configure()
inject.instance(_LoggingConfigurer).preconfigure()
inject.instance(_LoggingConfigurer).configure()
