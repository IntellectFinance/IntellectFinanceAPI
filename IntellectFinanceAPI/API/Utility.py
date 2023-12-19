import copy
import json
import urllib.request
import urllib.parse
from urllib.error import HTTPError
import ssl

from IntellectFinanceAPI.API.ErrorTypes import *

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

DICT_GLOBAL_VALUES = {
    'apikey': None
}


def set_api_key(apikey):
    DICT_GLOBAL_VALUES['apikey'] = apikey


def _call_url(url):
    # As we are accessing the API with `https`, we have to provide an SSL context.
    try:
        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE
    except Exception:
        ssl_context = None
        
    max_retry = 3
    retry_times = 0
    
    error = None
    
    while retry_times <= max_retry:
        retry_times += 1
        try:
            logging.info(f'Sending to API: {url}')
            http_response = urllib.request.urlopen(url, context=ssl_context)
            
            result_dict = json.loads(http_response.read())  # `result_dict` is a dictionary
            return result_dict
        
        except HTTPError as e:
            http_response = e  # contains informative error message.
            result_dict_str = http_response.read()
            try:
                result_dict = json.loads(result_dict_str)  # `result_dict` is a dictionary
            except Exception as parsing_error:
                logger.info(f'Error in parsing the JSON: {parsing_error}')
                result_dict = {'error': str(result_dict_str), 'error_type': UnknownAPIError.__name__}
            return result_dict
        
        except ConnectionResetError as e:
            logger.info(f'Retry `{url}` as there is an error: {e}')
            error = e
    
    if error:
        raise error
    else:
        raise NotImplementedError('Failed for unknown reason')


def _generate_url(api_name, kargs):
    
    url = f'https://www.intellect.finance/api/{api_name}?'
    
    if kargs:
        kargs_filtered = copy.deepcopy(kargs)
        # Do not pass `None` args
        for i in kargs:
            if kargs[i] is None:
                try:
                    del kargs_filtered[i]
                except KeyError:
                    pass
        
        if kargs_filtered:
            url += urllib.parse.urlencode(kargs_filtered) + '&'
    
    url += f"apikey={DICT_GLOBAL_VALUES['apikey']}"
    return url


def send_http_request(api_name, **kargs):
    if not DICT_GLOBAL_VALUES['apikey']:
        raise APIKeysNotFound(
            'Please run `from IntellectFinanceAPI import set_api_key; set_api_key(_YOUR_API_KEY_)` function to set up your API Key.` '
            'You can claim or change the API Key through https://www.intellect.finance/User?TabNameUserScreen=API+Keys.'
        )
    
    url = _generate_url(api_name, kargs)
    
    result_dict = _call_url(url)
    
    error_msg = result_dict.get('error')
    if error_msg:
        # Raise Error
        error_type = result_dict.get('error_type')
        if error_type in LIST_KNOWN_ERROR_NAMES and error_type in globals():
            ErrorClass = globals()[result_dict.get('error_type')]
        else:
            ErrorClass = APIError
        e = ErrorClass(error_msg)
        
        # pass the HTTP return to the error
        e.__setattr__('http_response', result_dict)
        
        raise e
    
    return result_dict
