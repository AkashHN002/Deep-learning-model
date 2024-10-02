from Hand_gesture_clf.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.Hand_gesture_clf import logger
from Hand_gesture_clf.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from Hand_gesture_clf.pipeline.stage_03_training import ModelTrainingPipeline


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} compleated<<<<<<<< \n\n x===============x")

except Exception as e:
    raise e




STAGE_NAME = "Prepare base model"
try:
    logger.info(f"************************")
    logger.info(f">>>>>>>>>>>>>>Stage {STAGE_NAME} strted<<<<<<<<<<<<<")
    obj  =PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>> Stage {STAGE_NAME} compleated<<<<<<<<<<<<<<")
except Exception as e:
    raise e



STAGE_NAME = "Training"
try:
    logger.info(f"************************")
    logger.info(f">>>>>>>>>>>>>>Stage {STAGE_NAME} strted<<<<<<<<<<<<<")
    obj  =ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>> Stage {STAGE_NAME} compleated<<<<<<<<<<<<<<")
except Exception as e:
    raise e