from dataclasses import dataclass
from pathlib import Path

# Creating a dataclass with "frozen=True" means its instances are frozen and cannot be changed.


@dataclass(frozen=True)
class DataIngestionConfig:
    """
    DataIngesionConfig is a dataclass that holds the configuration for the data ingestion pipeline.
    """

    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path