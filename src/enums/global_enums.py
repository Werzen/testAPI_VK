from enum import Enum


class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = "Received status code is not equal to expected."
    WRONG_VALUE_FIELDS = "Value of fields are not equal to expected."
    WRONG_COUNT_PHOTOS = "Incorrect result statistics."
