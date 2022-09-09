import logging

from IntellectFinanceAPI.API.api_functions import \
    news_by_ticker, news_by_source
from IntellectFinanceAPI.CommonUtility.time import move_date_str, get_today_us_eastern

today_eastern = get_today_us_eastern()
ten_days_ago = move_date_str(today_eastern, -10)


def check_news_by_ticker():
    r = news_by_ticker(ticker='AAPL', start_date=ten_days_ago, end_date=today_eastern)['result'] + \
        news_by_ticker(ticker='AMZN', start_date=ten_days_ago, end_date=today_eastern)['result'] + \
        news_by_ticker(ticker='GOOGL', start_date=ten_days_ago, end_date=today_eastern)['result'] + \
        news_by_ticker(ticker='QQQ', start_date=ten_days_ago, end_date=today_eastern)['result']
    
    logging.info(r)
    assert len(r) >= 5
    
    