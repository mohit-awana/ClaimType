from src.ClaimType  import logger
from src.ClaimType.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Date Ingestion Stage"


try:
    logger.info(f">>>>>Stage {STAGE_NAME} started <<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<<\n\nx====")
except Exception as e:
    logger.exception(e)
    raise e
