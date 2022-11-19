from dataclasses import dataclass
import logging as log

@dataclass
class Params:
    configPath: str = 'config.toml'
    logLevel = log.INFO
