class ResticVersion:
    def __init__(self, major: int, minor: int, patch: int):
        self._major = major
        self._minor = minor
        self._patch = patch

    @property
    def major(self):
        return self._major

    @property
    def minor(self):
        return self._minor

    @property
    def patch(self):
        return self._patch

    def __str__(self):
        return f'{self._major}.{self._minor}.{self._patch}'

    def __repr__(self):
        return f'ResticVersion({self._major}, {self._minor}, {self._patch})'
    
    def __eq__(self, other):
        if type(self) != type(other):
            return False

        return (
            self._major == other._major and
            self._minor == other._minor and
            self._patch == other._patch
        )

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        if self._major != other._major:
            return self._major > other._major

        if self._minor != other._minor:
            return self._minor > other._minor

        return self._patch > other._patch

    def __lt__(self, other):
        if self._major != other._major:
            return self._major < other._major

        if self._minor != other._minor:
            return self._minor < other._minor

        return self._patch < other._patch

    def __ge__(self, other):
        return self == other or self > other

    def __le__(self, other):
        return self == other or self < other
