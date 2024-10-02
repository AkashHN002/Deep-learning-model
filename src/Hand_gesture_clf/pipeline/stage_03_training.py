from Hand_gesture_clf.config.configuration import ConfigManager
from Hand_gesture_clf.components.prepare_callbacks import PrepareCallbacks
from Hand_gesture_clf.components.training import Training
from Hand_gesture_clf import logger 

STAGE_NAME = "Training"

class ModelTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigManager()
        prepare_callback_config = config.get_prepare_callbacksd_config()
        prepare_callback = PrepareCallbacks(config = prepare_callback_config)
        call_back_list = prepare_callback.get_tb_ckpt_callbacks()

        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train(
            callback_list=call_back_list
        )
    
