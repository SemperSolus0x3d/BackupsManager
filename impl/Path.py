import os
from typing import Iterable

class Path:
    def __init__(self, path: str | Iterable[str]):
        if isinstance(path, str):
            self._path = path
        else:
            self._path = os.path.join(*path)

    @property
    def path(self):
        return self._path
