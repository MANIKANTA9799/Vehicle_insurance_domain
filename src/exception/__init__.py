import sys
import logging

def error_message_detail(error_message, error_detail):
    if isinstance(error_detail, tuple):
        _, _, exc_tb = error_detail
    else:
        exc_tb = error_detail.__traceback__

    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    
    return f"Error in [{file_name}] at line [{line_number}]: {error_message}"

class MyException(Exception):
    """
    Custom exception class for handling errors in the US visa application.
    """
    def __init__(self, error_message: str, error_detail: sys):#type:ignore
        """
        Initializes the USvisaException with a detailed error message.

        :param error_message: A string describing the error.
        :param error_detail: The sys module to access traceback details.
        """
        # Call the base class constructor with the error message
        super().__init__(error_message)

        # Format the detailed error message using the error_message_detail function
        self.error_message = error_message_detail(error_message, error_detail)#type:ignore

    def __str__(self) -> str:
        """
        Returns the string representation of the error message.
        """
        return self.error_message