from Hand_gesture_clf.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.Hand_gesture_clf import logger

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} compleated<<<<<<<< \n\n x===============x")

except Exception as e:
    raise e