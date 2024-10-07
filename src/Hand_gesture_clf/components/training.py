from Hand_gesture_clf.utils.common import read_yaml, create_diorectories
from Hand_gesture_clf.constants import *
import tensorflow as tf
from Hand_gesture_clf.entity.config_entity import TrainingConfig
import time

class Training:
    def __init__(self, config:TrainingConfig):
        self.config = config

    def get_base_model(self):
        self.model = tf.keras.models.load_model(
            self.config.updated_base_model_path
        )
    
    def train_valid_generator(self):
        data_generator_kwargs = dict(
            rescale = 1./255,
            validation_split = 0.25
        )

        dataflow_kwargs = dict(
            target_size = self.config.params_imag_size[:-1],
            batch_size =self.config.params_batch_size,
            interpolation = "bilinear"
        )

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **data_generator_kwargs
        )

        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset='validation',
            shuffle=False,
            **dataflow_kwargs
        )

        if self.config.params_is_augmentation:
            train_data_generator = tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range=40,
                horizontal_flip= True,
                width_shift_range=0.2,
                height_shift_range=0.2,
                shear_range=0.2,
                zoom_range=0.2,
                **data_generator_kwargs
            )
        else:
            train_data_generator = valid_datagenerator

        self.train_generator = train_data_generator.flow_from_directory(
            directory=self.config.training_data,
            subset="training",
            shuffle=True,
            **dataflow_kwargs
        )

    @staticmethod
    def save_model(path: Path, model:tf.keras.Model):
        model.save(path)


    def train(self, callback_list: list):
        self.steps_per_epoch = 20
        self.validation_steps = self.valid_generator.samples // self.valid_generator.batch_size

        self.model.fit(
            self.train_generator,
            epochs = self.config.params_epochs,
            steps_per_epoch  = self.steps_per_epoch,
            validation_steps = self.validation_steps,
            validation_data = self.valid_generator,
            callbacks = callback_list

        )

        self.save_model(
            path = self.config.trained_model_path,
            model = self.model
        )

