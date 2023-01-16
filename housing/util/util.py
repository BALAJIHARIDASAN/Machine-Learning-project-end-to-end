# This file is used to create helper function which is not part of the project but necessary function for projects

import yaml
from housing.exception import HousingException
import os,sys
import numpy as np
import dill
import pandas as pd
from housing.constant import *





def read_yaml_file(file_path:str)->dict:
    """
    Reads a YAML file and returns the contents as a dictionary.
    file_path: str
    """
    try:
        with open(file_path, 'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise HousingException(e,sys) from e

