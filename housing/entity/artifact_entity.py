
# artifact_entity - the required output of the each component pipeline


from collections import namedtuple


# output of the data ingestion
DataIngestionArtifact = namedtuple("DataIngestionArtifact",
[ "train_file_path",                     "test_file_path",                   "is_ingested", "message"])
 # downloaded folder for train data    # downloaded folder for test data      



DataValidationArtifact = namedtuple("DataValidationArtifact",
["schema_file_path",   "report_file_path",    "report_page_file_path",     "is_validated",                 "message"])
# schema file path     # report file path     # report page folder path     # status of the validation      # message of the completed pipeline