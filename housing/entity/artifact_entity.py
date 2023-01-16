from collections import namedtuple


# output of the data ingestion
DataIngestionArtifact = namedtuple("DataIngestionArtifact",
[ "train_file_path",                     "test_file_path",                   "is_ingested", "message"])
 # downloaded folder for train data    # downloaded folder for test data      
