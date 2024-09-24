import os
from urllib.request import urlretrieve
import zipfile
from Hand_gesture_clf import logger
from Hand_gesture_clf.utils.common import get_size
from Hand_gesture_clf.entity.config_entity import DataIngestionConfig
from pathlib import Path

class DataIngestion:
    def __init__(self, config:DataIngestionConfig) -> None:
        self.config = config

    # Download the data
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = urlretrieve(
                url = self.config.source_url,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download! with info: \n{headers}")

        else:
            logger.info(f"File - {self.config.local_data_file} already exists with size : {get_size(Path(self.config.local_data_file))}")
    
    # Extract the data
    def extract_zip_file(self):
        """
        zip_file_path:str
        Extract the zip into the data directory
        return none
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok = True)
        with zipfile.ZipFile(self.config.local_data_file) as zip_ref:
            zip_ref.extractall(unzip_path)

