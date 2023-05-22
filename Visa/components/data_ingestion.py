import os, sys
import pandas as pd
import numpy as np
from Visa.constant import *
from Visa.logger import logging
from Visa.entity.config_entity import DataIngestionConfig
from Visa.entity.artifact_entity import DataIngestionArtifact
from Visa.exception import CustomException
from datetime import date
from sklearn.model_selection import train_test_split

# download data (cloud, Database, Github)
# Split data into train and test -> Ingested data

class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise CustomException(e,sys) from e
        
    def download_data(self)->str:
        try:
            download_url = self.data_ingestion_config.dataset_download_url # able to download data

            raw_data_dir = self.data_ingestion_config.raw_data_dir

            os.makedirs(raw_data_dir, exist_ok=True)

            us_visa_file_name = os.path.basename(download_url)

            raw_file_path = os.path.join(raw_data_dir, us_visa_file_name)

            return raw_file_path
        except Exception as e:
            raise CustomException(e,sys) from e
        
    def split_data_as_train_test(self) ->DataIngestionArtifact:
        try:
            raw_data_dir = self.data_ingestion_config.raw_data_dir
            file_name = os.listdir(raw_data_dir)[0]

            us_visa_file_name = os.path.join(raw_data_dir, file_name)

            today_date = date.today()
            current_year = today_date.year
            
            us_visa_dataframe = pd.read_csv(us_visa_file_name)

            train_set  = None
            test_set = None

            train_set, test_set = train_test_split(us_visa_dataframe, test_size=0.2, random_state=42)

            train_file_path = os.path.join(self.data_ingestion_config.ingested_train_dir, file_name)

            test_file_path = os.path.join(self.data_ingestion_config.ingested_test_dir, file_name)

            if train_set is not None:
                os.makedirs(self.data_ingestion_config.ingested_train_dir, exist_ok=True)
                train_set.to_csv(train_file_path, index = False)

            if test_set is not None:
                os.makedirs(self.data_ingestion_config.ingested_test_dir, exist_ok=True)
                train_set.to_csv(train_file_path, index = False)

            data_ingestion_artifact = DataIngestionArtifact(train_file_path=train_file_path,
                                                            test_file_path=test_file_path,
                                                            is_ingested=True,
                                                            messages=f"Data Ingestion Comppleted Successfully")
            
            return data_ingestion_artifact




        except Exception as e:
            raise  CustomException(e,sys) from e
            
    
    def initiate_data_ingestion(self):
        try:
            raw_data_file = self.download_data()
            return self.split_data_as_train_test()
        except Exception as e:
            raise  CustomException(e,sys) from e
