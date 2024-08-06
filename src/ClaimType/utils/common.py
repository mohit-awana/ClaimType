import os
import sys

project_dir = '/Users/mo/Downloads/workspace/ClaimType'

sys.path.append(os.path.abspath(os.path.join(project_dir, 'src')))

import os
from box.exceptions import BoxValueError
import yaml
from CNNClassifier import logger
import json
import joblib

# To make sure that our code working fine, and if not then raise exceptions.
from ensure import ensure_annotations
from box import ConfigBox
import box
from pathlib import Path
from typing import Any
import base64


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Read a yaml file from the given path.

    Args:
        :path_to_yaml (str): Path to the yaml file.

    Returns:
        :ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)

    except BoxValueError:
        raise ValueError("yaml file is empty")

    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Create list of directories.

    Args:
        :path_to_directories (list): list of path of directories.
        :verbose (bool, optional): ignore log if multiple dirs is to be created.

    Returns:
        None
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Save json data.

    Args:
        :path (Path): path to json file.
        :data (dict): data to be saved in json file.

    Returns:
        None
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Load json files data.

    Args:
        :path (Path): path to json file.

    Returns:
        :ConfigBox: data as class attributes instead of dict.
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Save binary file.

    Args:
        :data (Any): data to be saved as binary.
        :path (Path): path to binary file.

    Returns:
        None
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Load binary data.

    Args:
        :path (Path): path to binary file.

    Returns:
        :Any: object stored in the file.
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")

    return data


@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get size in KB.

    Args:
        :path (Path): path of the file.

    Returns:
        :str: size in KB.
    """
    size_in_kb = round(os.path.getsize(path) / 1024)

    return f"~ {size_in_kb} KB"


def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, "wb") as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())