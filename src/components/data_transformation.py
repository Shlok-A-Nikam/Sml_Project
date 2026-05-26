## create module of data transformation functions -
## 1. Handle missing values - numerical - median, categorical - mode
## 2. Handle categorical variables - one hot encoding, label encoding
## 3. Feature scaling - standardization, normalization

import os
import sys
import numpy as np
import pandas as pd
import pickle
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from src.logger import logging
from src.custom_exception import CustomException
from dataclasses import dataclass
from sklearn.impute import SimpleImputer

@dataclass
class DataTransformationConfig():
    preprocessor_obj_file_path: str = os.path.join('artifacts', 'preprocessor.pkl')

class DataTransformation():
    def __init__(self):
        self.preprocessor_config = DataTransformationConfig()
    
    def get_data_transformer_object(self, train_df):
        try:
            num_col = train_df.select_dtypes(include=[np.number]).columns
            cat_col = train_df.select_dtypes(include=['object']).columns
            ## numerical pipeline
            num_pipe = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='median')),
                ('scaler', StandardScaler())
            ])

            ## categorical pipeline
            cat_pipe = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='most_frequent')),
                ('onehot', OneHotEncoder(handle_unknown='ignore')),
                ('scaler', StandardScaler(with_mean=False))
            ])
            logging.info("Numerical and categorical pipelines created successfully")

            ## add the pipelines to a column transformer
            preprocessor = ColumnTransformer([
                ('num_pipe', num_pipe, num_col),
                ('cat_pipe', cat_pipe, cat_col)
            ])

            return preprocessor
        except Exception as e:
            raise CustomException(e, sys.exc_info())
    
    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("Read train and test data successfully")
            target_column_name = 'total_score'

            # If target column doesn't exist, compute it from the three score columns
            score_cols = ['math score', 'reading score', 'writing score']
            if target_column_name not in train_df.columns or target_column_name not in test_df.columns:
                if all(col in train_df.columns for col in score_cols) and all(col in test_df.columns for col in score_cols):
                    # ensure numeric then sum
                    train_df[score_cols] = train_df[score_cols].apply(pd.to_numeric, errors='coerce')
                    test_df[score_cols] = test_df[score_cols].apply(pd.to_numeric, errors='coerce')
                    train_df[target_column_name] = train_df[score_cols].sum(axis=1)
                    test_df[target_column_name] = test_df[score_cols].sum(axis=1)
                    logging.info("Computed '%s' from score columns", target_column_name)
                else:
                    raise CustomException(f"Required score columns {score_cols} not found to compute '{target_column_name}'", sys.exc_info())
            input_feature_train_df = train_df.drop(columns=[target_column_name])
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(columns=[target_column_name])
            target_feature_test_df = test_df[target_column_name]

            preprocessor_obj = self.get_data_transformer_object(input_feature_train_df)

            ## transform the input features
            input_feature_train_arr = preprocessor_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessor_obj.transform(input_feature_test_df)

            ## save the preprocessor object
            os.makedirs(os.path.dirname(self.preprocessor_config.preprocessor_obj_file_path), exist_ok=True)
            with open(self.preprocessor_config.preprocessor_obj_file_path, 'wb') as f:
                pickle.dump(preprocessor_obj, f)
            
            logging.info("Data transformation completed successfully")

            return (
                input_feature_train_arr,
                target_feature_train_df,
                input_feature_test_arr,
                target_feature_test_df,
                self.preprocessor_config.preprocessor_obj_file_path
            )
        except Exception as e:
            raise CustomException(e, sys.exc_info())