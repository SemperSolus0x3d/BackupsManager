import os
import re
import platform
from typing import Iterable, Union

class Path:
    _DRIVE_LETTER_REGEX = re.compile('[A-Za-z]:')

    def __init__(self, pathOrComponents: Union[str, Iterable[str]]):
        if isinstance(pathOrComponents, str):
            self._path = pathOrComponents
        else:
            self._path = self._join(list(pathOrComponents))

    @property
    def path(self):
        return self._path

    def __str__(self):
        return self.path

    def _join(self, components: list[str]):
        if len(components) == 0:
            return ''

        if platform.system() == 'Windows':
            if self._DRIVE_LETTER_REGEX.fullmatch(components[0]) is not None:
                components[0] += os.sep

        return os.path.join(*components)
