import sys
import logging

import sys
import logging

def error_message_detail(error: Exception, error_detail: sys) -> str:#type:ignore
    # get exception traceback object (type, value, traceback)
    _, _, exc_tb = error_detail.exc_info()

    # check if traceback exists (safe handling)
    if exc_tb is not None:
        # extract file name where exception occurred
        file_name = exc_tb.tb_frame.f_code.co_filename
        
        # extract exact line number of error
        line_number = exc_tb.tb_lineno
    else:
        # fallback if traceback not available
        file_name = "unknown"
        line_number = "unknown"

    # create structured error message
    error_message = f"Error occurred in python script: [{file_name}] at line number [{line_number}]: {str(error)}"

    # log error message using logging module
    logging.error(error_message)

    # return formatted error message
    return error_message


class MyException(Exception):
    def __init__(self, error: Exception, error_detail: sys):#type:ignore
        # call base exception constructor with basic error message
        super().__init__(str(error))

        # generate detailed error message with file + line info
        self.error_message = error_message_detail(error, error_detail)

    def __str__(self) -> str:
        # return custom formatted error message when printed
        return self.error_message