import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class APIError(Exception):
    """Base class for exceptions in this module."""
    STATUS_CODE = 400
    
    ADD_ADDITIONAL_ERROR_INFO = {}
    
    def set_additional_error_info(self, key, value):
        self.ADD_ADDITIONAL_ERROR_INFO[key] = value
    
    def get_additional_error_info(self):
        return self.ADD_ADDITIONAL_ERROR_INFO


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


class CannotFindTopicNameError(APIError):
    pass


class TopicIsMergedToAnotherTopicError(APIError):
    STATUS_CODE = 301  # 301 Moved Permanently
    JSON_EXAMPLE_FOR_API_DOC = {"error_type": "TopicIsMergedToAnotherTopic", "new_topic_name": "A_NEW_TOPIC_NAME"}
    
    ERROR_KEY_new_topic_name = 'new_topic_name'


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


LIST_KNOWN_ERROR_NAMES = []
for k in list(globals().values()):
    try:
        if issubclass(k, APIError):
            LIST_KNOWN_ERROR_NAMES.append(k.__name__)
    except Exception:
        pass
