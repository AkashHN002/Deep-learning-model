from Hand_gesture_clf.config.configuration import ConfigManager
from Hand_gesture_clf.components.prepare_base_model import PrepareBaseModel
from Hand_gesture_clf import logger

STAGE_NAME = "Prepare base model"

class PrepareBaseModelTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()

        
if __name__ == "__main__":
    try:
        logger.info(f"************************")
        logger.info(f">>>>>>>>>>>>>>Stage {STAGE_NAME} strted<<<<<<<<<<<<<")
        obj  =PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>> Stage {STAGE_NAME} compleated<<<<<<<<<<<<<<")
    except Exception as e:
        raise e
