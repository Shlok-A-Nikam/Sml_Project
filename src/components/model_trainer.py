import os
import sys
import numpy as np
import pandas as pd
import pickle
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score
from src.logger import logging
from src.custom_exception import CustomException
from dataclasses import dataclass
from src.components.data_injestion import DataIngestion
from src.components.data_transformation import DataTransformationConfig, DataTransformation

@dataclass
class ModelTrainerconfig():
    trained_model_file_path: str = os.path.join('artifacts', 'model.pkl')
    def __init__(self):
        self.model_trainer_config = ModelTrainerconfig()
    def initiate_model_trainer(self):
        try:
            data_injestion = DataIngestion()
            input_feature_train_arr, target_feature_train_arr, input_feature_test_arr, target_feature_test_arr, preprocessor_obj = DataTransformation().initiate_data_transformation()
            model = DecisionTreeRegressor()
            model.fit(input_feature_train_arr, target_feature_train_arr)
            logging.info("Model training is completed successfully")

            target_pred = model.predict(input_feature_test_arr)
            r2_square = r2_score(target_feature_test_arr, target_pred)
            
            logging.info("Model evaluation is completed successfully with r2 score: %s", r2_square)
            os.makedirs(os.path.dirname(self.model_trainer_config.trained_model_file_path), exist_ok=True)
            with open(self.model_trainer_config.trained_model_file_path, 'wb') as f:
                pickle.dump(model, f)
            logging.info("Trained model saved at path: %s", self.model_trainer_config.trained_model_file_path)
        except Exception as e:
            raise CustomException(e, sys.exc_info())
        