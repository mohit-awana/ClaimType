import os
import sys

project_dir = '/Users/mo/Downloads/workspace/ClaimType/'
sys.path.append(os.path.abspath(os.path.join(project_dir, 'src')))

from ClaimType.constants import *
from ClaimType.utils.common import read_yaml, create_directories, save_json
from ClaimType.entity.config_entity import DataIngestionConfig


class ConfigurationManager:
    def __init__(self, config_file_path=CONFIG_FILE_PATH, params_file_path=PARAMS_FILE_PATH):

        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,	
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir,
        )

        return data_ingestion_config


