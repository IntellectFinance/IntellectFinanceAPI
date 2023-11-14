import logging

import re
from PyHelpers import move_date_str
from WarrensDataAccess.TopicCollectionReadOnlyV2 import TopicNotFoundError as TopicNotFoundError_

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class APIError(Exception):
    """Base class for exceptions in this module."""
    STATUS_CODE = 400
    
    def __init__(self, *args: object):
        super().__init__(*args)
        self.ADD_ADDITIONAL_ERROR_INFO = {}
        self.error = args[0] if len(args) else ''
    
    def set_additional_error_info(self, key, value):
        self.ADD_ADDITIONAL_ERROR_INFO[key] = value
    
    def get_additional_error_info(self):
        return self.ADD_ADDITIONAL_ERROR_INFO
    
    def __str__(self):
        return f'{type(self).__name__}: {self.error}'


class TopicNotFoundError(APIError, TopicNotFoundError_):
    """
    If you are in any non-unlimited plan, and call the APT too many times, we will raise this error.
    """
    pass


class APITotalCreditsExceed(APIError):
    """
    If you are in any non-unlimited plan, and call the APT too many times, we will raise this error.
    """
    pass


class APIQPSLimitExceed(APIError):
    """
    If you call the API too fast and exceeds your plan's QPS (query per second) limit, we will raise this error.
    """


class UnknownAPIError(APIError):
    """
    When the API is unknown.
    """


class ParameterMissingError(APIError):
    """Exception raised if one or more required param values are missing.
    """


class CannotFindTickerNameError(APIError):
    pass


class ParameterInvalidError(APIError):
    """Exception raised if the input param value is invalid.
    """


class APIKeysNotFound(APIError):
    """
    When you forget to provide the APT keys
    """
    pass


class ExceptionNoTickerFound(APIError):
    pass


class ExceptionNoCIKFound(APIError):
    pass


LIST_KNOWN_ERROR_NAMES = []
for k in list(globals().values()):
    try:
        if issubclass(k, APIError):
            LIST_KNOWN_ERROR_NAMES.append(k.__name__)
    except Exception:
        pass


def check_date_range(request, start_date, end_date, LARGEST_DATA_RANGE=None):
    if not re.compile(r'^\d\d\d\d-\d\d-\d\d').findall(start_date):
        raise ParameterInvalidError(f'`start_date` must be in the format of YYYY-mm-dd, you provided `{start_date}`.')
    
    if not re.compile(r'^\d\d\d\d-\d\d-\d\d').findall(end_date):
        raise ParameterInvalidError(f'`end_date` must be in the format of YYYY-mm-dd, you provided `{end_date}`.')
    
    if LARGEST_DATA_RANGE:
        if move_date_str(date_str=start_date, days=LARGEST_DATA_RANGE) < end_date:
            if str(request.GET.get('SKIP_CONSTRAINT')).lower() in ['1', 'true']:
                pass
            else:
                raise ParameterInvalidError(f'Data range cannot be larger than {LARGEST_DATA_RANGE} days. You provided ({start_date}--{end_date}).')
