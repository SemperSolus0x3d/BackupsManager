import inject

from .DIConfigurer import DIConfigurer
from .LoggingConfigurer import LoggingConfigurer

from .BackupService import BackupService

DIConfigurer().configure()
inject.instance(LoggingConfigurer).configure()
