from housing.config.configuration import Configuartion

from housing.logger import logging

from housing.exception import HousingException

from housing.entity.artifact_entity import *

from housing.entity.config_entity import *

from housing.component.data_ingestion import *

import os, sys

class Pipeline:


    def __init__(self,config:Configuartion= Configuartion())-> None:
        try:
            self.config = config

        except Exception as e:
            raise HousingException(e,sys) from e



    def start_date_ingestion(self) -> DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(data_ingestion_config = self.config.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()

        except Exception as e:
            raise HousingException(e,sys) from e




    def run_pipeline(self):
        try:
            data_ingestion_artifact = self.start_date_ingestion()
        except Exception as e:
            raise HousingException(e,sys) from e
