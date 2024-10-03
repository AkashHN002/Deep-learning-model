
import os
from pathlib import Path
import tensorflow as tf
from urllib.parse import urlparse
from Hand_gesture_clf.config.configuration import EvaluateConfig
from Hand_gesture_clf.utils.common import save_json



class Evaluation:
    def __init__(self, config: EvaluateConfig) -> None:
        self.config = config

    def _valid_generator(self):
        
        data_generator_kwargs = dict(
            rescale = 1./255,
            validation_split = 0.3
        )

        data_flow_kwargs = dict(
            target_size = self.config.params_image_size[:-1],
            batch_size = self.config.params_batch_size,interpolation = 'bilinear'
        )

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **data_generator_kwargs
        )

        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset = "validation",
            shuffle= False,
            **data_flow_kwargs
        )


    @staticmethod
    def load_model(path:Path) -> tf.keras.Model:
        return tf.keras.models.load_model(path)
    

    def evaluation(self):
        self.model = self.load_model(self.config.path_of_model)
        self._valid_generator()
        self.score = self.model.evaluate(self.valid_generator)


    def save_scores(self):
        scores = {"loss":self.score[0], "accuracy":self.score[1]}
        save_json(path=Path("scores.json"), data = scores)



        