from dataclasses import dataclass
from .Path import Path

@dataclass
class Config:
    excludes: list[Path]

    # case-insensitive includes
    iexcludes: list[Path]
    
    includePatterns: list[Path]
    includePaths: list[Path]

    repositoryPassword: str
    usbRepositoryPassword: str

    repositoryPath: Path
    usbRepositoryPath: Path

    resticPath: Path | None
