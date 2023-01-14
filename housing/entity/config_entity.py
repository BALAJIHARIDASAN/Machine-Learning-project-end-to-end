from collections import namedtuple


DataIngestionConfig=namedtuple("DataIngestionConfig",
["dataset_download_url","tgz_download_dir",                "raw_data_dir",      "ingested_train_dir",         "ingested_test_dir"])
# dataset url           # folder for downloaded dataset    # raw data folder    # Train datset folder name    # test dataset folder name

DataValidationConfig = namedtuple("DataValidationConfig", ["schema_file_path","report_file_path","report_page_file_path"])  
                                                            # schema folder      # report folder    # reprot html foler path

DataTransformationConfig = namedtuple("DataTransformationConfig", ["add_bedroom_per_room" ,"transformed_train_dir",   "transformed_test_dir", "preprocessed_object_file_path"])
                                                                # add bedroom                  # train datset folder   #test dataset folder    # pickle file folder 

ModelTrainerConfig = namedtuple("ModelTrainerConfig", ["trained_model_file_path", "base_accuracy", "model_config_file_path"])
                                                        # trained model folder     # base accuracy   # pickle folder

ModelEvaluationConfig = namedtuple("ModelEvaluationConfig", ["model_evaluation_file_path","time_stamp"])
                                                             # model evaluation folder      # timestamp

ModelPusherConfig = namedtuple("ModelPusherConfig", ["export_dir_path"])
                                                        # folder of exported model

TrainingPipelineConfig = namedtuple("TrainingPipelineConfig", ["artifact_dir"])                             
                                                               # folder for all atrifact



# information are provided through yaml file and create object for all steps for pipeline

