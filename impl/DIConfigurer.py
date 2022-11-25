import inject
import platform

from .Params import Params
from .ParamsService import ParamsService
from .Config import Config
from .ConfigService import ConfigService
from .SingleInstanceLockService import SingleInstanceLockService

if platform.system() == 'Windows':
    from .WindowsSingleInstanceLockService import WindowsSingleInstanceLockService
elif platform.system() == 'Linux':
    from .UnixSingleInstanceLockService import UnixSingleInstanceLockService
else:
    raise Exception(f'Unknown system: {platform.system()}')

class DIConfigurer:
    def configure(self):
        inject.configure(DIConfigurer._doConfigure)

    @staticmethod
    def _doConfigure(binder: inject.Binder):
        bindings = [
            (Params, lambda: inject.instance(ParamsService).params),
            (Config, lambda: inject.instance(ConfigService).config),
            DIConfigurer._getSingleInstanceLockServiceBinding()
        ]

        for binding in bindings:
            binder.bind_to_constructor(*binding)

    @staticmethod
    def _getSingleInstanceLockServiceBinding():
        system = platform.system()

        if system == 'Windows':
            return (SingleInstanceLockService, WindowsSingleInstanceLockService)
        elif system == 'Linux':
            return (SingleInstanceLockService, UnixSingleInstanceLockService)
        else:
            raise Exception(f'Unknown system: {system}')
