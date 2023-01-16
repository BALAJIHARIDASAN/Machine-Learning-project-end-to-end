from collections import namedtuple


DataIngestionConfig=namedtuple("DataIngestionConfig",
["dataset_download_url",  "tgz_download_dir",             "raw_data_dir",    "ingested_train_dir", "ingested_test_dir"])
 # url                     # folder for compressed file   # raw data folder   # train folder        # test folder

DataValidationConfig = namedtuple("DataValidationConfig", ["schema_file_path",    "report_file_path",   "report_page_file_path"])
                                                            # schema folder path  # report folder path   # report html foler path


DataTransformationConfig = namedtuple("DataTransformationConfig", ["add_bedroom_per_room", "transformed_train_dir", "transformed_test_dir","preprocessed_object_file_path"])
                                                                    # to add column         # train folder           # test folder          # pickle folder of preprocessing object




ModelTrainerConfig = namedtuple("ModelTrainerConfig", ["trained_model_file_path",           "base_accuracy"  ,   "model_config_file_path"])
                                                        # pickle trained model folder      # base accuracy                 



ModelEvaluationConfig = namedtuple("ModelEvaluationConfig", ["model_evaluation_file_path",                               "time_stamp"])
                                                            #  folder for information about models in production        # timestamp for model evaluation



ModelPusherConfig = namedtuple("ModelPusherConfig", ["export_dir_path"])
                                                    # folder for model 



TrainingPipelineConfig = namedtuple("TrainingPipelineConfig", ["artifact_dir"])
 


 # These are the information that will be provided to configuration file.
 # Thses information will be either stored in yaml file or databases.
 # These infomation will be read from the yaml file.


