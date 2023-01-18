
# artifact_entity - the required output of the each component pipeline


from collections import namedtuple


# output of the data ingestion
DataIngestionArtifact = namedtuple("DataIngestionArtifact",
[ "train_file_path",                     "test_file_path",                   "is_ingested", "message"])
 # downloaded folder for train data    # downloaded folder for test data      



DataValidationArtifact = namedtuple("DataValidationArtifact",
["schema_file_path",   "report_file_path",    "report_page_file_path",     "is_validated",                 "message"])
# schema file path     # report file path     # report page folder path     # status of the validation      # message of the completed pipeline



DataTransformationArtifact = namedtuple("DataTransformationArtifact",["is_transformed",            "message", "transformed_train_file_path",                 "transformed_test_file_path",            "preprocessed_object_file_path"])
                                                                       # status of transformation               # file path for transformed train data      # file path for transformed test data     # path for pickle file



ModelTrainerArtifact = namedtuple("ModelTrainerArtifact", ["is_trained", "message",   "trained_model_file_path", "train_rmse", "test_rmse", "train_accuracy",  "test_accuracy", "model_accuracy"])
                                                           # status      # message    # trained model file path   # train rmse  # test rmse   #train accuracy   # test accuracy  # model accuracy

                                                           