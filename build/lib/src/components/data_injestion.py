import numpy as np
import pandas as pd
import os
from src.logger import logger
from src.custom_exception import CustomException
import sys 
from dataclasses import dataclass

@dataclass
class DataIngestionConfig():
    raw_data_path: str = os.path.join('artifact','raw_data.csv')
    train_data_path: str = os.path.join('artifact','train_data.csv')
    test_data_path: str = os.path.join('artifact','test_data.csv')

class DataIngestion():
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logger.info("Data Ingestion method starts")
        try:
            df = pd.read_csv(os.path.join('notebook/data','stud.csv'))
            logger.info("Dataset read as pandas dataframe")

            os.makedirs(os.path.dirname(self.data_ingestion_config.raw_data_path), exist_ok=True)

            df.to_csv(self.data_ingestion_config.raw_data_path, index=False)
            logger.info("Raw data is saved")

            from sklearn.model_selection import train_test_split
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.data_ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.data_ingestion_config.test_data_path, index=False, header=True)
            logger.info("Train and Test data is saved")

            return (
                self.data_ingestion_config.train_data_path,
                self.data_ingestion_config.test_data_path
            )
        except Exception as e:
            logger.info("Exception occurred in Data Ingestion stage")
            raise CustomException(e, sys.exc_info())

