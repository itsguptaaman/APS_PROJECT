import pandas as pd
from sensor.logger import logging
from sensor.exception import SensorException
from sensor.config import mongo_client
import os
import sys


def get_collection_as_dataframe(database_name: str, collection_name: str) -> pd.DataFrame:
    """
    Description : This function returns collection as a dataframe.
    --------------------------------------------------------------
    Params:
    database_name : Name of the database.
    collection_name : Name of the collection
    --------------------------------------------------------------
    returns pandas datafrane of a collection.
    """
    try:
        logging.info(
            f"Reading the data from the database : {database_name} and collection : {collection_name}")
        # .find() will give a generator we need to convert it into list then into a datafrmae
        df = pd.DataFrame(
            list(mongo_client[database_name][collection_name].find()))
        logging.info(f"Found columns : {df.columns}")

        if "_id" in df.columns:
            logging.info(f"Dropping columns : _id ")
            df.drop("_id", axis=1)
        logging.info(f"No of rows and columns in df are {df.shape}")

        return df

    except Exception as e:
        raise SensorException(e, sys)
