from sensor.logger import logging
from sensor.exception import SensorException
import sys
import os


def test_logger_and_exception():
    try:
        logging.info("Starting the test logger function")
        result = 3/0
        print(result)
        logging.info("Stopping the test logger function")

    except Exception as e:
        logging.debug("Starting the test logger function")
        raise SensorException(e, sys)


if __name__ == "__main__":
    try:
        test_logger_and_exception()

    except Exception as e:
        print(e)
