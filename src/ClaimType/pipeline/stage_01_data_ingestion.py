import os
import sys

project_dir = '/Users/mo/Downloads/workspace/ClaimType/'

sys.path.append(os.path.abspath(os.path.join(project_dir, 'src')))

from ClaimType.config.configuration import ConfigurationManager
from ClaimType.components.data_ingestion import DataIngestion
from ClaimType import logger


STAGE_NAME = "Date Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>Stage {STAGE_NAME} started <<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>> stage {STAGE_NAME} completed <<<<\n\nx====")
    except Exception as e:
        logger.exception(e)
        raise e