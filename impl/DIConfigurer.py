import inject

from Params import Params
from ParamsService import ParamsService
from Config import Config
from ConfigService import ConfigService

class DIConfigurer:
    def configure(self):
        inject.configure(DIConfigurer._doConfigure)

    @staticmethod
    def _doConfigure(binder: inject.Binder):
        bindings = [
            (Params, lambda: inject.instance(ParamsService).params),
            (Config, lambda: inject.instance(ConfigService).config)
        ]

        for binding in bindings:
            binder.bind_to_constructor(*binding)
