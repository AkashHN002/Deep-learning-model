from Hand_gesture_clf.config.configuration import ConfigManager
from Hand_gesture_clf.components.model_evaluation import Evaluation
from Hand_gesture_clf import logger



STAGE_NAME = "Evaluation Stage"

class EvaluationPipeline:
    def __init__(self) -> None:
        pass
        
    def main(self):
        config = ConfigManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_scores()


if __name__ == '__main__':
    try:
        logger.info(f"****************************************")
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} compleated<<<<<<<< \n\n x===============x")

    except Exception as e:
        raise e