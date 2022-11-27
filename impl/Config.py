from dataclasses import dataclass
from typing import Union
from .Path import Path

@dataclass
class Config:
    excludes: list[Path]

    # case-insensitive excludes
    iexcludes: list[Path]

    includePatterns: list[Path]
    includePaths: list[Path]

    repositoryPassword: str
    usbRepositoryPassword: str

    repositoryPath: Path
    usbRepositoryPath: Path

    resticPath: Union[Path, None]

    repoMountpoint: Path
    usbRepoMountpoint: Path

    keepHourlySnapshots: int
    keepDailySnapshots: int
    keepWeeklySnapshots: int
    keepMonthlySnapshots: int
    keepYearlySnapshots: int
