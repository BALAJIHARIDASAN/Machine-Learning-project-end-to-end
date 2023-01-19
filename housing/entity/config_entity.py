from collections import namedtuple
# Input for the every component in the pipeline
# This infomation should be provided  to the configuration

# The information required to this config_entity will be read from the config.yaml file


# input information provides to the data ingestion component - this component contains these informations
DataIngestionConfig=namedtuple("DataIngestionConfig",
["dataset_download_url",  "tgz_download_dir",             "raw_data_dir",    "ingested_train_dir", "ingested_test_dir"])
 # url                     # folder for compressed file   # raw data folder   # train folder        # test folder


# input information provides to the data validation component
DataValidationConfig = namedtuple("DataValidationConfig", ["schema_file_path",    "report_file_path",   "report_page_file_path"])
                                                            # schema folder path  # report folder path   # report html folder path

# input provides to the data transformation component
DataTransformationConfig = namedtuple("DataTransformationConfig", ["add_bedroom_per_room", "transformed_train_dir", "transformed_test_dir","preprocessed_object_file_path"])
                                                                    # to add column         # train folder           # test folder          # pickle folder of preprocessing object



# input  provides to the model tranier component
ModelTrainerConfig = namedtuple("ModelTrainerConfig", ["trained_model_file_path",           "base_accuracy"  ,   "model_config_file_path"])
                                                        # pickle trained model folder      # base accuracy        $ model config folder path         


# input provides to the model evaluation component
ModelEvaluationConfig = namedtuple("ModelEvaluationConfig", ["model_evaluation_file_path",                               "time_stamp"])
                                                            #  folder for information about models in production        # timestamp for model evaluation


# input provides to the  model pusher component
ModelPusherConfig = namedtuple("ModelPusherConfig", ["export_dir_path"])
                                                    # folder for model  


# input to the training pipeline component
TrainingPipelineConfig = namedtuple("TrainingPipelineConfig", ["artifact_dir"])
 


 # These are the information that will be provided to configuration file.
 # Thses information will be either stored in yaml file or databases.
 # These infomation will be read from the yaml file.


