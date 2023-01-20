
from housing.pipeline.pipeline import Pipeline
from housing.exception import HousingException
from housing.logger import logging
from housing.config.configuration import *

def main():
    pipeline = Pipeline()
    pipeline.run_pipeline()
    

if __name__ == "__main__":
    main()
