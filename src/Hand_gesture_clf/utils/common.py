import os
from box.exceptions import BoxValueError
import yaml
from Hand_gesture_clf import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64


@ensure_annotations
def read_yaml(path:Path) -> ConfigBox:
    """reads yaml file and returns

    :arg:path (str): path like input

    :raises: ValueError: if yaml file is empty
    e:empty file

    :return:Configbox:config type
    """
    try :
        with open(path, 'r', encoding='utf-8') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file {path} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_diorectories(path_to_directories: list, verbose = True):
    """
    Create list of Directories
    :param path_to_directories: list of path of directories
    :param verbose: ignore_log(bool, optional) : ignore if multiple dirs has to be created. Default is False.
    :return:
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at : {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data

    :param path: path to json file.
    :param data: dataq to be saved in json file
    """
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at :{path}")

@ensure_annotations
def load_json(path: Path) ->ConfigBox:
    """
    loads json files data
    :param path: path to json file
    :return:ConfigBox : data as a class attributes instead of dict.
    """
    with open(path) as f:
        content = json.load(f)
    logger.info(f"json file is successfully loaded from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path:Path):
    """
    save bin files

    :param data: data to be saved as binary
    :param path:path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    load binary data
    :param path: path to binary file
    :return:Any:object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data


@ensure_annotations
def get_size(path: Path) -> str:
    """
    get size in kb
    :param path: path to file

    :return: str: file size in kb
    
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~{size_in_kb} KB"
    

def decode_image(imgstring, filename):
    imgdata = base64.b64decode(imgstring)
    with open(filename, 'wb') as f:
        f.write(imgdata)
        f.close()


def encode_image(croppedImagePath):
    with open(croppedImagePath, 'rb') as f:
        return base64.b64encode(f.read())
