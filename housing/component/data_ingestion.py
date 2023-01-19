# code for data ingestion configuration

# 1. download housing data
# 2. extract the data
# 3. Split the data as train and test



from housing.entity.config_entity import DataIngestionConfig
import sys,os
from housing.exception import HousingException
from housing.logger import logging
from housing.entity.artifact_entity import DataIngestionArtifact
import tarfile
import numpy as np
from six.moves import urllib
import pandas as pd
from sklearn.model_selection import StratifiedShuffleSplit

class DataIngestion:

    def __init__(self,data_ingestion_config:DataIngestionConfig ):
        try:
            logging.info(f"{'>>'*20}Data Ingestion log started.{'<<'*20} ")
            self.data_ingestion_config = data_ingestion_config  # inilizing the data ingestion config path

        except Exception as e:
            raise HousingException(e,sys)
    

    def download_housing_data(self,) -> str:  # download the data from url
        try:
            #extraction remote url to download dataset
            download_url = self.data_ingestion_config.dataset_download_url

            #folder location to download file
            tgz_download_dir = self.data_ingestion_config.tgz_download_dir
            
            os.makedirs(tgz_download_dir,exist_ok=True)  # create the folder  for downloading dataset

            housing_file_name = os.path.basename(download_url)  # extract only the housing.tgz from the url where the dataset is present

            tgz_file_path = os.path.join(tgz_download_dir, housing_file_name) # create a folder with file of url file

            logging.info(f"Downloading file from :[{download_url}] into :[{tgz_file_path}]")
            urllib.request.urlretrieve(download_url, tgz_file_path)   # to read  and download the data from the url 
            logging.info(f"File :[{tgz_file_path}] has been downloaded successfully.")
            return tgz_file_path  # location of the dataset to be downloaded

        except Exception as e:
            raise HousingException(e,sys) from e

    def extract_tgz_file(self,tgz_file_path:str):  # extracting the data 
        try:
            raw_data_dir = self.data_ingestion_config.raw_data_dir  # get the directory of raw data folder

            if os.path.exists(raw_data_dir): # To check whether the folder is exist or not
                os.remove(raw_data_dir)   # remove the folder if it exist

            os.makedirs(raw_data_dir,exist_ok=True)  # to create the folder raw data dir to save the dataset

            logging.info(f"Extracting tgz file: [{tgz_file_path}] into dir: [{raw_data_dir}]")
            with tarfile.open(tgz_file_path) as housing_tgz_file_obj:
                housing_tgz_file_obj.extractall(path=raw_data_dir) # extract the raw data dir
            logging.info(f"Extraction completed")

        except Exception as e:
            raise HousingException(e,sys) from e
    
    def split_data_as_train_test(self) -> DataIngestionArtifact:  # split the data into train and test dataset
        try:
            raw_data_dir = self.data_ingestion_config.raw_data_dir  # get the directory for data ingested

            file_name = os.listdir(raw_data_dir)[0]  # To get the file name from the list

            housing_file_path = os.path.join(raw_data_dir,file_name)   # directory for complete file path that need to split


            logging.info(f"Reading csv file: [{housing_file_path}]")
            housing_data_frame = pd.read_csv(housing_file_path)  # reading the extracted file

            housing_data_frame["income_cat"] = pd.cut(
                housing_data_frame["median_income"],
                bins=[0.0, 1.5, 3.0, 4.5, 6.0, np.inf],
                labels=[1,2,3,4,5]
            )  # distribution of the median income
            

            logging.info(f"Splitting data into train and test")
            strat_train_set = None # creating the dataset for train 
            strat_test_set = None # creating the dataset for test

            split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=121)  # spliting the dataset

            for train_index,test_index in split.split(housing_data_frame, housing_data_frame["income_cat"]): # ration that split happens will always have same proportion
                strat_train_set = housing_data_frame.loc[train_index].drop(["income_cat"],axis=1)  # extract the row wise data using values
                strat_test_set = housing_data_frame.loc[test_index].drop(["income_cat"],axis=1)  # extract the row wise data using values
  
            train_file_path = os.path.join(self.data_ingestion_config.ingested_train_dir,
                                            file_name)  # creating the directory for the train data

            test_file_path = os.path.join(self.data_ingestion_config.ingested_test_dir,
                                        file_name)   # creating the directory for the test data
            
            if strat_train_set is not None:
                os.makedirs(self.data_ingestion_config.ingested_train_dir,exist_ok=True)
                logging.info(f"Exporting training datset to file: [{train_file_path}]")
                strat_train_set.to_csv(train_file_path,index=False)  # to store the data in the train directory

            if strat_test_set is not None:
                os.makedirs(self.data_ingestion_config.ingested_test_dir, exist_ok= True)
                logging.info(f"Exporting test dataset to file: [{test_file_path}]")
                strat_test_set.to_csv(test_file_path,index=False)  # to store the data in the test directory
            

            data_ingestion_artifact = DataIngestionArtifact(train_file_path=train_file_path,
                                test_file_path=test_file_path,
                                is_ingested=True,
                                message=f"Data ingestion completed successfully."
                                )
            logging.info(f"Data Ingestion artifact:[{data_ingestion_artifact}]")
            return data_ingestion_artifact

        except Exception as e:
            raise HousingException(e,sys) from e

    def initiate_data_ingestion(self)-> DataIngestionArtifact:  # to initiate the data ingestion component
        '''This function will return the data ingestion artifact path'''
        try:
            tgz_file_path =  self.download_housing_data()  # download the file
            self.extract_tgz_file(tgz_file_path=tgz_file_path) # extract the file
            return self.split_data_as_train_test() # split the file as train and test
        except Exception as e:
            raise HousingException(e,sys) from e
    


    def __del__(self):
        logging.info(f"{'>>'*20}Data Ingestion log completed.{'<<'*20} \n\n")


    def __del__(self):
        logging.info(f"{'>>'*20}Data Ingestion log completed.{'<<'*20} \n\n")