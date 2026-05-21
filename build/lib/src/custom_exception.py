import sys
from typing import Any, Tuple


def log_exception(error: Exception, error_details: Any) -> str:
    # Accept either an exc_info() tuple or a module like `sys`; prefer tuple when provided
    if isinstance(error_details, tuple):
        _, _, exc_tb = error_details
    else:
        _, _, exc_tb = sys.exc_info()

    if exc_tb is None:
        file_name = '<unknown>'
        line_number = 0
    else:
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno

    error_message = (
        f"Error occurred in file: {file_name} at line: {line_number} with error message: {str(error)}"
    )

    return error_message


class CustomException(Exception):
    def __init__(self, error_message: Exception, error_details: Any = None):
        super().__init__(error_message)
        details = error_details if error_details is not None else sys.exc_info()
        self.error_message = log_exception(error_message, details)

    def __str__(self) -> str:
        return self.error_message