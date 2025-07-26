import sys
import logging

def error_message_detail(error:Exception,error_details:sys):
    """
    Extracts detailed error information including file name, line number, and the error message.
    : param error: The exception that occurred.
    : param error_details: The sys module to access exception details.
    : return: A Formatted error message string.
    """

    # Extract traceback details (exception information)
    _,_, exc_tb = error_details.exc_info()

    # Get the file name where exception occurred
    file_name = exc_tb.tb_frame.f_code.co_filename

    # creates a formatted error message string with file name, line number and actual error 
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in python script: [{file_name}] at line number: [{line_number}] error: {str(error)}"

    # log the error for better tracking
    logging.error(error_message)

    return error_message

class MyException(Exception):
    """
    Custom exception class for handling errors.
    """
    def __init__(self, error_message:str,error_details:sys):
        """
        Initializes the custom exception with an error message.
        
        params: error_message: The error message to be logged.
        params: error_details: The sys module to access exception details.
        """
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_details)

    def __str__(self) -> str:
        """
        Returns the string representation of the error message.
        """
        return self.error_message