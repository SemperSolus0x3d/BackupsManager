import os
from typing import Iterable

class Path:
    def __init__(self, path: str | Iterable[str]):
        if isinstance(path, str):
            self._path = path
        else:
            components = (*path,)
            if len(components) != 0:
                self._path = os.path.join(*components)
            else:
                self._path = ''

    @property
    def path(self):
        return self._path

    def __str__(self):
        return self.path
