from src.ClaimType  import logger
from src.ClaimType.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.ClaimType.pipeline.stage_02_data_transform import DataTransformationTrainingPipeline

STAGE_NAME = "Date Ingestion Stage"


try:
    logger.info(f">>>>>Stage {STAGE_NAME} started <<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<<\n\nx====")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Prepare Transformation Stage"


try:
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    transform_data = DataTransformationTrainingPipeline()
    transform_data.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
