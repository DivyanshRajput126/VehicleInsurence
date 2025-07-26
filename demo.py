# # Below code is to check the logging config

# from src.logger import logging

# logging.debug("This is a debug message")
# logging.info("This is an info message")
# logging.warning("This is a warning message")
# logging.error("This is an error message")
# logging.critical("This is a critical message")

# # Below code is to check the exception handling
# from src.exception import MyException
# from src.logger import logging
# import sys

# try:
#     a = 1+'z'
# except Exception as e:
#     logging.info(e)
#     raise MyException(e, sys) from e

from src.pipline.training_pipeline import TrainPipeline

pipeline = TrainPipeline()
pipeline.run_pipeline()