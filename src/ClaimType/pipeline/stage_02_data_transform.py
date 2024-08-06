import os
import sys

project_dir = '/Users/mo/Downloads/workspace/ClaimType/'

sys.path.append(os.path.abspath(os.path.join(project_dir, 'src')))

from ClaimType.config.configuration import ConfigurationManager
from ClaimType.components.data_transformation import DataTransform
from ClaimType import logger

STAGE_NAME = "Date Transformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transform = DataTransform(config=data_transformation_config)
        data_transform.transform()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>Stage {STAGE_NAME} started <<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>> stage {STAGE_NAME} completed <<<<\n\nx====")
    except Exception as e:
        logger.exception(e)
        raise e