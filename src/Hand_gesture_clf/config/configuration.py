from Hand_gesture_clf.constants import *
import os
from Hand_gesture_clf.utils.common import read_yaml, create_diorectories
from Hand_gesture_clf.entity.config_entity import ( DataIngestionConfig,
                                                   PrepareBaseModelConfig,
                                                    PrepareCallbacksConfig,
                                                    TrainingConfig)

class ConfigManager:
    def __init__(
            self,
            config_file_path  = CONFIG_FILE_PATH,
            params_file_path = PARAMS_FILE_PATH):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)

        create_diorectories([self.config.artifacts_root])


    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_diorectories([config.root_dir])
        data_ingestion_config  =DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file = config.local_data_file,
            unzip_dir= config.unzip_dir
        )

        return data_ingestion_config
    
    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        config = self.config.prepare_base_model
        
        create_diorectories([config.root_dir])

        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path= Path(config.updated_base_model_path),
            params_image_size= self.params.IMAGE_SIZE,
            params_learning_rate= self.params.LEARNING_RATE,
            params_include_top= self.params.INCLUDE_TOP,
            params_weight=self.params.WEIGHTS,
            params_class=self.params.CLASSES
        )
        return prepare_base_model_config
    
    def get_prepare_callbacksd_config(self) -> PrepareCallbacksConfig:
        config = self.config.prepare_callbacks
        model_chkpt_dir = os.path.dirname(config.checkpoint_model_filepath)

        create_diorectories([
            Path(model_chkpt_dir),
            Path(config.tensorboard_root_log_dir)
        ])

        prepare_callback_config = PrepareCallbacksConfig(
            root_dir=Path(config.root_dir),
            tensorboard_root_log_dir= Path(config.tensorboard_root_log_dir),
            checkpoint_model_filepath= Path(config.checkpoint_model_filepath)
        )
        return prepare_callback_config
    
    def get_training_config(self)->TrainingConfig:
        training = self.config.training
        prepare_base_model = self.config.prepare_base_model
        params = self.params
        training_data = os.path.join(self.config.data_ingestion.unzip_dir, "HandGesture")

        create_diorectories([Path(training.root_dir)])


        training_config = TrainingConfig(
            root_dir = Path(training.root_dir),
            trained_model_path = Path(training.trained_model_path),
            updated_base_model_path = Path(prepare_base_model.updated_base_model_path),
            training_data = Path(training_data),
            params_epochs = params.EPOCHS,
            params_batch_size = params.BATCH_SIZE,
            params_is_augmentation = params.AUGMENTATION,
            params_imag_size = params.IMAGE_SIZE
         )
        
        return training_config
