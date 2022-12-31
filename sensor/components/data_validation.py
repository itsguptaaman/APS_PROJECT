from sensor.entity import artifact_entity
from sensor.entity import config_entity
from sensor.logger import logging
from scipy.stats import ks_2samp
from sensor.exception import SensorException
from typing import Optional
from sensor import utils
import pandas as pd
import numpy as np
import os
import sys


class DataValidation:

    def __init__(self, data_validation_config: config_entity.DataValidationConfig, data_ingestion_artifact: artifact_entity.DataIngestionArtifact):
        try:
            logging.info(f"{'>>'*20} Data Validation {'<<'*20}")
            self.data_validation_config = data_validation_config
            self.data_ingestion_artifact = data_ingestion_artifact
            self.validation_error = dict()

        except Exception as e:
            raise SensorException(e, sys)

    def drop_missing_values_columns(self, df: pd.DataFrame, threshold: float = 0.3) -> pd.DataFrame:
        """
        Description : This function will drop columns which contains missing values more than specified threshold.

        df : Accepts a pandas dataframe.
        threshold : Percentage value to drop a column
        -------------------------------------------------------------------------------------------------------------
        returns pandas dataframe if atleast a single column is available after missing column drop else returns none.
        """
        try:
            threshold = self.data_validation_config.missing_threshold
            null_report = df.isna().sum()/df.shape[0]

            # selecting column name which contains null
            logging.info(
                f"selecting column name which contains null above to {threshold}")
            drop_column_names = null_report[null_report > threshold].index

            logging.info(f"Columns to drop: {list(drop_column_names)}")
            self.validation_error[report_key_name] = list(drop_column_names)
            df.drop(list(drop_column_names), axis=1, inplace=True)

            # return None no columns left
            if len(df.columns) == 0:
                return None

            return df
        except Exception as e:
            raise SensorException(e, sys)

    def is_required_columns_exists(self, base_df: pd.DataFrame, current_df: pd.DataFrame, report_key_name: str) -> bool:
        try:
            base_columns = base_df.columns
            current_columns = current_df.columns

            missing_columns = []
            for base_columm in base_columns:
                if base_columm not in current_columns:
                    logging.info(f"Column : [{base_column} is not availabe]")
                    missing_columns.append(base_column)

            if len(missing_columns) > 0:
                self.validation_error[report_key_name] = missing_columns
                return False

            return True

        except Exception as e:
            raise SensorException(e, sys)

    def initiate_data_validation(self) -> artifact_entity.DataValidationArtifact:
        try:
            pass
        except Exception as e:
            raise SensorException(e, sys)
