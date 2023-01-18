from cgi import test
from sklearn import preprocessing
from housing.exception import HousingException
from housing.logger import logging
from housing.entity.config_entity import DataTransformationConfig 
from housing.entity.artifact_entity import DataIngestionArtifact,\
DataValidationArtifact,DataTransformationArtifact
import sys,os
import numpy as np
from sklearn.base import BaseEstimator,TransformerMixin
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
import pandas as pd
from housing.constant import *
from housing.util.util import read_yaml_file,save_object,save_numpy_array_data,load_data


#   longitude: float
#   latitude: float
#   housing_median_age: float
#   total_rooms: float
#   total_bedrooms: float
#   population: float
#   households: float
#   median_income: float
#   median_house_value: float
#   ocean_proximity: category
#   income_cat: float


class FeatureGenerator(BaseEstimator, TransformerMixin):  # inheriting the class from the sklearn library

    def __init__(self, add_bedrooms_per_room=True,
                 total_rooms_ix=3,
                 population_ix=5,
                 households_ix=6,
                 total_bedrooms_ix=4, columns=None):
        """
        FeatureGenerator Initialization
        add_bedrooms_per_room: bool
        total_rooms_ix: int index number of total rooms columns
        population_ix: int index number of total population columns
        households_ix: int index number of  households columns
        total_bedrooms_ix: int index number of bedrooms columns
        """
        try:
            self.columns = columns
            if self.columns is not None:
                total_rooms_ix = self.columns.index(COLUMN_TOTAL_ROOMS)   # calculate total number of room
                population_ix = self.columns.index(COLUMN_POPULATION)     # population of the each house
                households_ix = self.columns.index(COLUMN_HOUSEHOLDS)     # 
                total_bedrooms_ix = self.columns.index(COLUMN_TOTAL_BEDROOM)

            self.add_bedrooms_per_room = add_bedrooms_per_room
            self.total_rooms_ix = total_rooms_ix
            self.population_ix = population_ix
            self.households_ix = households_ix
            self.total_bedrooms_ix = total_bedrooms_ix
        except Exception as e:
            raise HousingException(e, sys) from e

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        try:
            room_per_household = X[:, self.total_rooms_ix] / \
                                 X[:, self.households_ix]
            population_per_household = X[:, self.population_ix] / \
                                       X[:, self.households_ix]  
            if self.add_bedrooms_per_room:  
                bedrooms_per_room = X[:, self.total_bedrooms_ix] / \
                                    X[:, self.total_rooms_ix]
                generated_feature = np.c_[
                    X, room_per_household, population_per_household, bedrooms_per_room] # if it true then new columns will be added # concatination
            else:
                generated_feature = np.c_[
                    X, room_per_household, population_per_household]  # concatinating the columns 

            return generated_feature
        except Exception as e:
            raise HousingException(e, sys) from e





class DataTransformation:

    def __init__(self, data_transformation_config: DataTransformationConfig,
                 data_ingestion_artifact: DataIngestionArtifact,
                 data_validation_artifact: DataValidationArtifact
                 ):   # creating artifact for data transformation
        try:
            logging.info(f"{'>>' * 30}Data Transformation log started.{'<<' * 30} ")
            self.data_transformation_config= data_transformation_config
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_artifact = data_validation_artifact

        except Exception as e:
            raise HousingException(e,sys) from e

    

    def get_data_transformer_object(self)->ColumnTransformer:
        try:
            schema_file_path = self.data_validation_artifact.schema_file_path  # reading schema file path

            dataset_schema = read_yaml_file(file_path=schema_file_path)  # reading the dataset

            numerical_columns = dataset_schema[NUMERICAL_COLUMN_KEY]  # generating numerical columns
            categorical_columns = dataset_schema[CATEGORICAL_COLUMN_KEY]  # generating categorical columns


            num_pipeline = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy="median")),
                ('feature_generator', FeatureGenerator(
                    add_bedrooms_per_room=self.data_transformation_config.add_bedroom_per_room,
                    columns=numerical_columns
                )),
                ('scaler', StandardScaler())
            ]
            )   # creating the pipeline for numerical columns

            cat_pipeline = Pipeline(steps=[
                 ('impute', SimpleImputer(strategy="most_frequent")),
                 ('one_hot_encoder', OneHotEncoder()),
                 ('scaler', StandardScaler(with_mean=False))
            ]
            )  # creating the pipeline for categorical columns

            logging.info(f"Categorical columns: {categorical_columns}")
            logging.info(f"Numerical columns: {numerical_columns}")


            preprocessing = ColumnTransformer([
                ('num_pipeline', num_pipeline, numerical_columns), # numerical column pipeline
                ('cat_pipeline', cat_pipeline, categorical_columns), # categorical column pipeline
            ])   # creating column transformer for the processing, concatination both pipeline
            return preprocessing  # give data as the processed data

        except Exception as e:
            raise HousingException(e,sys) from e   


    def initiate_data_transformation(self)->DataTransformationArtifact:
        try:
            logging.info(f"Obtaining preprocessing object.")
            preprocessing_obj = self.get_data_transformer_object()  # reading the preprocessing object


            logging.info(f"Obtaining training and test file path.")
            train_file_path = self.data_ingestion_artifact.train_file_path  # reading the train data
            test_file_path = self.data_ingestion_artifact.test_file_path    # reading the test data
            

            schema_file_path = self.data_validation_artifact.schema_file_path  # reading the schema path
            
            logging.info(f"Loading training and test data as pandas dataframe.")
            train_df = load_data(file_path=train_file_path, schema_file_path=schema_file_path)  # loading the train data
            
            test_df = load_data(file_path=test_file_path, schema_file_path=schema_file_path)  # loading the test data

            schema = read_yaml_file(file_path=schema_file_path)  # reading the dataset
 
            target_column_name = schema[TARGET_COLUMN_KEY]  # creating the target data


            logging.info(f"Splitting input and target feature from training and testing dataframe.")
            input_feature_train_df = train_df.drop(columns=[target_column_name],axis=1)  # creating the train data
            target_feature_train_df = train_df[target_column_name] # creating the test data

            input_feature_test_df = test_df.drop(columns=[target_column_name],axis=1) # test data input features
            target_feature_test_df = test_df[target_column_name]  # test data output features
            

            logging.info(f"Applying preprocessing object on training dataframe and testing dataframe")
            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)  # preprocessing train input features
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df) # preprocessing test input features


            train_arr = np.c_[ input_feature_train_arr, np.array(target_feature_train_df)] # concatinating train data

            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]  # concatinting test data
            
            transformed_train_dir = self.data_transformation_config.transformed_train_dir  # path for train dataset
            transformed_test_dir = self.data_transformation_config.transformed_test_dir  # path for test dataset

            train_file_name = os.path.basename(train_file_path).replace(".csv",".npz")  # reading the housin.csv
            test_file_name = os.path.basename(test_file_path).replace(".csv",".npz")  # reading the housing.csv

            transformed_train_file_path = os.path.join(transformed_train_dir, train_file_name)  # path for transformed dataset
            transformed_test_file_path = os.path.join(transformed_test_dir, test_file_name) # path for transformed dataset

            logging.info(f"Saving transformed training and testing array.")
            
            save_numpy_array_data(file_path=transformed_train_file_path,array=train_arr)  # saving the output as numpy array
            save_numpy_array_data(file_path=transformed_test_file_path,array=test_arr)  # saving the output as numpy array

            preprocessing_obj_file_path = self.data_transformation_config.preprocessed_object_file_path  # creating path for pickle file

            logging.info(f"Saving preprocessing object.")
            save_object(file_path=preprocessing_obj_file_path,obj=preprocessing_obj)  # saving the pickle object

            data_transformation_artifact = DataTransformationArtifact(is_transformed=True,
            message="Data transformation successfull.",
            transformed_train_file_path=transformed_train_file_path,
            transformed_test_file_path=transformed_test_file_path,
            preprocessed_object_file_path=preprocessing_obj_file_path

            )  
            logging.info(f"Data transformationa artifact: {data_transformation_artifact}")
            return data_transformation_artifact  # return output in data validation aritifact
        except Exception as e:
            raise HousingException(e,sys) from e

    def __del__(self):
        logging.info(f"{'>>'*30}Data Transformation log completed.{'<<'*30} \n\n")
