import json
from unittest import TestCase
from unittest.mock import patch
from urllib.error import HTTPError

from IntellectFinanceAPI.API.ErrorTypes import APIKeysNotFound, APIError
from IntellectFinanceAPI.API.Utility import _call_url, _generate_url, set_api_key, send_http_request
from IntellectFinanceAPI.CommonUtility.test_utility import eval_TestCase


class HTTPResponse:
    def read(self):
        return json.dumps({'RESULT': 1})


class HTTPResponseWithError(HTTPError):
    def read(self):
        return json.dumps({'ERROR': 1})


class TestSendHTTPRequest(TestCase):
    
    def test_call_url(self):
        with patch('urllib.request.urlopen') as f:
            f.return_value = HTTPResponse()
            r = _call_url('url')
            assert r == {'RESULT': 1}
        
        def raise_error(x):
            raise HTTPResponseWithError(url='url', code=500, hdrs=None, fp=None, msg=json.dumps({1: 2}))
        
        with patch('urllib.request.urlopen') as f:
            f.side_effect = raise_error
            r = _call_url('https://A_RANDOM_URL')
            assert r == {'ERROR': 1}
    
    def test_generate_url(self):
        set_api_key(1)
        
        assert _generate_url('one_api', {'ticker': 2, 'date': '2021-01-01'}) == \
               'https://www.intellect.finance/api/one_api?ticker=2&date=2021-01-01&apikey=1'
        assert _generate_url('one_api', {}) == \
               'https://www.intellect.finance/api/one_api?apikey=1'

        assert _generate_url('one_api', {'to_delete': None}) == \
               'https://www.intellect.finance/api/one_api?apikey=1'

        set_api_key(None)
    
    def test_send_http_request(self):
        set_api_key(1)
        with patch('IntellectFinanceAPI.API.Utility._call_url') as f:
            f.return_value = {'result': 1}
            r = send_http_request(api_name='one_api', ticker=1, date='2021-01-01')
            assert r == {'result': 1}
    
    def test_send_http_request_with_known_errors(self):
        set_api_key(None)
        with patch('IntellectFinanceAPI.API.Utility._call_url') as f:
            f.return_value = {'error_type': APIKeysNotFound.__name__}
            with self.assertRaises(APIKeysNotFound):
                send_http_request(api_name='one_api', ticker=1, date='2021-01-01')
        
        error_msg = 'EXPECTED_ERROR'
        set_api_key(1)
        with patch('IntellectFinanceAPI.API.Utility._call_url') as f:
            with self.assertRaises(APIKeysNotFound) as ctx:
                f.return_value = {'error_type': APIKeysNotFound.__name__, 'error': error_msg}
                self.assertRaises(send_http_request(api_name='one_api', ticker=1, date='2021-01-01'), APIKeysNotFound('APIKEY_IS_INVALID'))
            assert str(ctx.exception) == error_msg
    
    def test_send_http_request_with_unknown_errors(self):
        error_msg = 'UNKNOWN_ERROR'
        set_api_key(1)
        with patch('IntellectFinanceAPI.API.Utility._call_url') as f:
            with self.assertRaises(APIError) as ctx:
                f.return_value = {'error_type': NotImplementedError.__name__, 'error': error_msg}
                send_http_request(api_name='one_api', ticker=1, date='2021-01-01'), APIKeysNotFound('APIKEY_IS_INVALID')
            assert str(ctx.exception) == error_msg


if __name__ == '__main__':
    eval_TestCase(TestSendHTTPRequest)
