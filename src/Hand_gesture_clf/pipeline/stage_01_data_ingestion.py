from Hand_gesture_clf.config.configuration import ConfigManager
from Hand_gesture_clf.components.data_ingestion import DataIngestion
from Hand_gesture_clf import logger

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self) -> None:
        pass
        
    def main(self):
        config = ConfigManager()
        data_indestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_indestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == '__main__':
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} compleated<<<<<<<< \n\n x===============x")

    except Exception as e:
        raise e
