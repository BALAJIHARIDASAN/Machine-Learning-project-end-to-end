# To keep log or detail of the process, this can keep track of the project execution.

import logging 
from datetime import datetime
import os
import pandas as pd
from housing.constant import get_current_time_stamp 

LOG_DIR="logs"  # creating the directory as log 

def get_log_file_name():
    '''Description : This function will create a log file to store the log '''
    return f"log_{get_current_time_stamp()}.log"

LOG_FILE_NAME=get_log_file_name()  # creating log file name

os.makedirs(LOG_DIR,exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_DIR,LOG_FILE_NAME)  # creating log file path



logging.basicConfig(filename=LOG_FILE_PATH,
filemode="w",
format='[%(asctime)s]%(name)s-%(levelname)s-%(message)s',
level=logging.INFO
) # this code will helps to create the log

def get_log_dataframe(file_path):
    '''This function will create the dataframe to store the log'''
    data=[]
    with open(file_path) as log_file:
        for line in log_file.readlines():
            data.append(line.split("^;"))

    log_df = pd.DataFrame(data)
    columns=["Time stamp","Log Level","line number","file name","function name","message"]
    log_df.columns=columns
    
    log_df["log_message"] = log_df['Time stamp'].astype(str) +":$"+ log_df["message"]

    return log_df[["log_message"]]


















