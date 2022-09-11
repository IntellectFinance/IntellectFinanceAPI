from IntellectFinanceAPI.API.Utility import send_http_request


def news_by_source(*ignore, news_source, start_time, end_time): 
    """
    https://www.intellect.finance/API_Document#news_by_source
    Get a list of news by the news source (i.e. WSJ, Bloomberg, or CNBC, etc). The max time range shall be less than 24.5 hours.

    :example: news_by_source(news_source='CNBC', start_time='2022-02-01 02:00:00', end_time='2022-02-01 12:00:00')
    
    :exception: ['ParameterInvalidError', 'ParameterMissingError']
    :param news_source: Source of the news. Available sources are `['Bloomberg', 'Fox', 'CNBC', 'WSJ', 'CNN', 'New York Times', "Barron's", 'Reuters', 'Businesswire', 'PR Newswire']`.
    :param start_time: UTC start date time of the news.
    :param end_time: UTC start date time of the news.
    :return: {'result': `A list of news.`}
    """
    return send_http_request('news_by_source', news_source=news_source, start_time=start_time, end_time=end_time)


def news_by_ticker(*ignore, ticker, start_date, end_date): 
    """
    https://www.intellect.finance/API_Document#news_by_ticker
    Get a list of news that is relevant to a company. Note that the input date range of the news has to be less than 32 days.

    :example: news_by_ticker(ticker='AAPL', start_date='2022-02-01', end_date='2022-02-08')
    
    :exception: ['ParameterInvalidError', 'ParameterMissingError']
    :param ticker: The ticker.
    :param start_date: Start date (UTC) of the news range. Its format should be `YYYY-MM-DD`.
    :param end_date: End date (UTC) (including) of the news range. Its format should be `YYYY-MM-DD`.
    :return: {'result': `A list of news.`}
    """
    return send_http_request('news_by_ticker', ticker=ticker, start_date=start_date, end_date=end_date)


def news_by_topic(*ignore, topic_name, start_date, end_date): 
    """
    https://www.intellect.finance/API_Document#news_by_topic
    Get list of news under one topic within a certain date range (cannot be more than 95 days). In case the topic you provide is merged with a new topic, we will return an JSON response 
    {
       "error_type": "TopicIsMergedToAnotherTopic", 
       "new_topic_name": "A_NEW_TOPIC_NAME", 
    }
<br/>with HTTP code `301`. Thus, you can re-call this API with the new topic name showed in `A_NEW_TOPIC_NAME`. 

    :example: news_by_topic(topic_name='Hidden impact on China's financial center', start_date='2022-03-30', end_date='2022-07-02')
    
    :exception: ['ParameterInvalidError', 'ParameterMissingError', 'TopicIsMergedToAnotherTopicError']
    :param topic_name: A topic name. Note that we only accept topic names listed in the `topic_names` API.
    :param start_date: The start date (UTC) of the news.
    :param end_date: The end date (UTC) (including) of the news.
    :return: {'result': `A list of news.`}
    """
    return send_http_request('news_by_topic', topic_name=topic_name, start_date=start_date, end_date=end_date)


def relevance_score_between_two_tickers(*ignore, ticker_1, ticker_2): 
    """
    https://www.intellect.finance/API_Document#relevance_score_between_two_tickers
    Get the relevance score between two tickers. The score measures the similarity of the two tickers/companies. Note that the relevance score may change every day as we receive new information (i.e. new events, or news) about each ticker.

    :example: relevance_score_between_two_tickers(ticker_1='GOOGL', ticker_2='MSFT')
    
    :exception: ['ExceptionNoTickerFound', 'ParameterMissingError']
    :param ticker_1: A ticker.
    :param ticker_2: Another ticker.
    :return: {'result': `The degree of relevance or similarity between the two trickers, ranging from (0, 1). The higher the score, the more related this topic is about this ticker.`}
    """
    return send_http_request('relevance_score_between_two_tickers', ticker_1=ticker_1, ticker_2=ticker_2)


def relevant_tickers_by_ticker(*ignore, ticker): 
    """
    https://www.intellect.finance/API_Document#relevant_tickers_by_ticker
    Get a list of the most relevant tickers to the input ticker. The more frequent that ticker A and B appear in the same news, then the more relevant these two tickers are.

    :example: relevant_tickers_by_ticker(ticker='GOOGL')
    
    :exception: ['ExceptionNoTickerFound', 'ParameterMissingError']
    :param ticker: A ticker.
    :return: {'result': `A list of dictionaries, ordered by the relevance score (high to low). Each dictionary contains a relevant ticker to the input ticker, and the degree of their relevance (relevance sores).`}
    """
    return send_http_request('relevant_tickers_by_ticker', ticker=ticker)


def relevant_tickers_by_topic(*ignore, topic_name, year): 
    """
    https://www.intellect.finance/API_Document#relevant_tickers_by_topic
    Get the most relevant tickers under one topic, and the degree of the relevance of those tickers to that topic. In case the topic you provide is merged with a new topic, we will return an JSON response 
    {
       "error_type": "TopicIsMergedToAnotherTopic", 
       "new_topic_name": "A_NEW_TOPIC_NAME", 
    }
<br/>with HTTP code `301`. Thus, you can re-call this API with the new topic name showed in `A_NEW_TOPIC_NAME`. 

    :example: relevant_tickers_by_topic(topic_name='Hidden impact on China's financial center', year='2021')
    
    :exception: ['CannotFindTopicNameError', 'ParameterInvalidError', 'ParameterMissingError', 'TopicIsMergedToAnotherTopicError']
    :param topic_name: A topic name. Note that we only accept topic names found in the `topic_names` API.
    :param year: The year of the topic.
    :return: {'result': `A list of dictionaries, ordered by the relevance score (high to low). Each dictionary contains a relevant ticker to the input topic, and the degree of their relevance (relevance sores).`}
    """
    return send_http_request('relevant_tickers_by_topic', topic_name=topic_name, year=year)


def topic_names(*ignore, start_date, end_date): 
    """
    https://www.intellect.finance/API_Document#topic_names
    Get a list of topic names within a date range (has to be less or equal than 95 days). 
    The topic names may change at any time. For example, 
    we may merge topics `A` and `B` together and create a new topic `C`. 
    Then the list will no longer contain topics `A` and `B`.

    :example: topic_names(start_date='2022-02-01', end_date='2022-02-03')
    
    :exception: ['ParameterInvalidError', 'ParameterMissingError']
    :param start_date: Start date (UTC) of the news range. Its format should be `YYYY-MM-DD`.
    :param end_date: End date (UTC) (including) of the news range. Its format should be `YYYY-MM-DD`. The data range between start date to end date shall not be more than 31 days.
    :return: {'result': `A hashmap of topics. Key is the topic name, and value is the information about the topic.`}
    """
    return send_http_request('topic_names', start_date=start_date, end_date=end_date)


def sentiment_time_series_one_topic(*ignore, topic_name, start_date, end_date): 
    """
    https://www.intellect.finance/API_Document#sentiment_time_series_one_topic
    Get a time series of sentiment scores for a topic (the time range cannot be more than 65 days). In case the topic you provide is merged with a new topic, we will return an JSON response 
    {
       "error_type": "TopicIsMergedToAnotherTopic", 
       "new_topic_name": "A_NEW_TOPIC_NAME", 
    }
<br/>with HTTP code `301`. Thus, you can re-call this API with the new topic name showed in `A_NEW_TOPIC_NAME`. 

    :example: sentiment_time_series_one_topic(topic_name='Hidden impact on China's financial center', start_date='2022-03-30', end_date='2022-06-02')
    
    :exception: ['CannotFindTopicNameError', 'ParameterInvalidError', 'ParameterMissingError', 'TopicIsMergedToAnotherTopicError']
    :param topic_name: A topic name. Note that we only accept topic names listed in the `topic_names` API.
    :param start_date: The start date (UTC) of the news.
    :param end_date: The end date (UTC) (including) of the news.
    :return: {'result': `A list of sentiment scores (with number of news), ordered by date.`}
    """
    return send_http_request('sentiment_time_series_one_topic', topic_name=topic_name, start_date=start_date, end_date=end_date)


def sentiment_time_series_one_ticker(*ignore, ticker, start_date, end_date): 
    """
    https://www.intellect.finance/API_Document#sentiment_time_series_one_ticker
    Get a time series of sentiment scores for a ticker (the time range cannot be more than 65 days). 

    :example: sentiment_time_series_one_ticker(ticker='AMZN', start_date='2021-06-30', end_date='2021-09-02')
    
    :exception: ['ExceptionNoTickerFound', 'ParameterInvalidError', 'ParameterMissingError']
    :param ticker: A ticker.
    :param start_date: The start date (UTC) of the news.
    :param end_date: The end date (UTC) (including) of the news.
    :return: {'result': `A time series (list) of sentiment scores (with number of news), ordered by date.`}
    """
    return send_http_request('sentiment_time_series_one_ticker', ticker=ticker, start_date=start_date, end_date=end_date)


def annualized_sharpe_ratio_by_ticker(*ignore, ticker, start_date, end_date, risk_free_rate, smart_sharpe_flag=None): 
    """
    https://www.intellect.finance/API_Document#annualized_sharpe_ratio_by_ticker
    Calculate the annualized Sharpe Ratio for a ticker in a given period (should be less 370 days).

    :example: annualized_sharpe_ratio_by_ticker(ticker='MSFT', start_date='2021-01-01', end_date='2021-12-31', risk_free_rate=0.02, smart_sharpe_flag='false')
    
    :exception: ['ExceptionNoTickerFound', 'ParameterInvalidError', 'ParameterMissingError']
    :param ticker: A ticker.
    :param start_date: Start date. Its format should be `YYYY-MM-DD`.
    :param end_date: End date (including). Its format should be `YYYY-MM-DD`. The max time range between `start_date` and `end_date` has to be less than 370 days.
    :param risk_free_rate: Risk-free rate of interest (expressed in annualized term).
    :param smart_sharpe_flag: Optional. A boolean flag (`false` or `true`) indicating whether a Smart Sharpe ratio is returned. Default is `false`.
    :return: {'result': `The Sharpe ratio in annualized term (round to 3 decimal places).`}
    """
    return send_http_request('annualized_sharpe_ratio_by_ticker', ticker=ticker, start_date=start_date, end_date=end_date, risk_free_rate=risk_free_rate, smart_sharpe_flag=smart_sharpe_flag)


def max_drawdown_by_ticker(*ignore, ticker, start_date, end_date): 
    """
    https://www.intellect.finance/API_Document#max_drawdown_by_ticker
    Calculate the maximum drawdown (MDD) for a ticker in a given period (should be less 370 days).

    :example: max_drawdown_by_ticker(ticker='MSFT', start_date='2021-01-01', end_date='2021-12-31')
    
    :exception: ['ExceptionNoTickerFound', 'ParameterInvalidError', 'ParameterMissingError']
    :param ticker: A ticker.
    :param start_date: Start date. Its format should be `YYYY-MM-DD`.
    :param end_date: End date (including). Its format should be `YYYY-MM-DD`. Should be less 370 days from the start_date.
    :return: {'result': `A hashmap that contains the maximum drawdown and the date at which the maximum drawdown occurs.`}
    """
    return send_http_request('max_drawdown_by_ticker', ticker=ticker, start_date=start_date, end_date=end_date)


def treasury_yield(*ignore, duration, start_date, end_date): 
    """
    https://www.intellect.finance/API_Document#treasury_yield
    
    Get the U.S. Treasury par yield curve rates for a time period (has to be less than 370 days). These rates are commonly referred to as `Constant Maturity Treasury` rates, or CMTs. 
    Yields are interpolated by the Treasury from the daily par yield curve. 
    This curve, which relates the yield on a security to its time to maturity, 
    is based on the closing market bid prices on the most recently auctioned Treasury securities in the over-the-counter market. 
    See the <a href='https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202208' target='_blank'>data source here</a>.
    

    :example: treasury_yield(duration='duration_1mo', start_date='2021-01-01', end_date='2021-03-01')
    
    :exception: ['ParameterInvalidError', 'ParameterMissingError']
    :param duration: Duration of the treasury securities. Available durations to choose are ('duration_1mo', 'duration_2mo', 'duration_3mo', 'duration_6mo', 'duration_1yr', 'duration_2yr', 'duration_3yr', 'duration_5yr', 'duration_7yr', 'duration_10yr', 'duration_20yr', 'duration_30yr').
    :param start_date: Start date. Its format should be `YYYY-MM-DD`.
    :param end_date: End date (including). Its format should be `YYYY-MM-DD`. The max time range between `start_date` and end_date has to be less than 370 days.
    :return: {'result': `A time series of the yield data.`}
    """
    return send_http_request('treasury_yield', duration=duration, start_date=start_date, end_date=end_date)


def treasury_real_yield(*ignore, duration, start_date, end_date): 
    """
    https://www.intellect.finance/API_Document#treasury_real_yield
    
    Get the U.S. Treasury par real yield curve rates for a time period (has to be less than 370 days). 
    These rates are commonly referred to as `Real Constant Maturity Treasury` rates, or R-CMTs. 
    Par real yields on Treasury Inflation Protected Securities (TIPS) at `constant maturity` are interpolated by the U.S. 
    Treasury from Treasury's daily par real yield curve. 
    These par real yields are calculated from indicative secondary market quotations obtained 
    by the Federal Reserve Bank of New York.  
    See the <a href='https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_real_yield_curve&field_tdr_date_value_month=202208' target='_blank'>data source here</a>.
    

    :example: treasury_real_yield(duration='duration_10yr', start_date='2021-01-01', end_date='2021-03-01')
    
    :exception: ['ParameterInvalidError', 'ParameterMissingError']
    :param duration: Duration of the treasury securities. Available durations to choose are ['duration_5yr', 'duration_7yr', 'duration_10yr', 'duration_20yr', 'duration_30yr'].
    :param start_date: Start date. Its format should be `YYYY-MM-DD`.
    :param end_date: End date (including). Its format should be `YYYY-MM-DD`. The max time range between `start_date` and end_date has to be less than 370 days.
    :return: {'result': `A time series of the yield data.`}
    """
    return send_http_request('treasury_real_yield', duration=duration, start_date=start_date, end_date=end_date)


def fed_fund_target_rate(*ignore, start_date, end_date): 
    """
    https://www.intellect.finance/API_Document#fed_fund_target_rate
    
    Get the Federal fund target rate for a time period (has to be less than 370 days). The federal funds rate is the interest rate at which depository institutions trade federal funds 
    (balances held at Federal Reserve Banks) with each other overnight.
    The Federal Open Market Committee (FOMC) meets eight times a year to determine the federal funds target rate. 
    See <a href='https://fred.stlouisfed.org/series/DFF' target='_blank'>https://fred.stlouisfed.org/series/DFF.</a>

    :example: fed_fund_target_rate(start_date='2021-01-01', end_date='2021-03-01')
    
    :exception: ['ParameterInvalidError', 'ParameterMissingError']
    :param start_date: Start date. Its format should be `YYYY-MM-DD`.
    :param end_date: End date (including). Its format should be `YYYY-MM-DD`. The max time range between `start_date` and end_date has to be less than 370 days.
    :return: {'result': `A time series of the Fed fund target rate data.`}
    """
    return send_http_request('fed_fund_target_rate', start_date=start_date, end_date=end_date)


def tickers_available(*ignore, ): 
    """
    https://www.intellect.finance/API_Document#tickers_available
    Get a full list of currently active tickers.

    :example: tickers_available()
    
    :exception: ['ParameterMissingError']
    :return: {'result': `A list of tickers that are active (not de-listed).`}
    """
    return send_http_request('tickers_available', )


def company_info_by_cik(*ignore, cik): 
    """
    https://www.intellect.finance/API_Document#company_info_by_cik
    Get company information by Central Index Key (CIK) number.

    :example: company_info_by_cik(cik=1652044)
    
    :exception: ['ParameterMissingError']
    :param cik: A Central Index Key (CIK) number.
    :return: {'result': `A list of company information, deduped by `cik`, `sic`, `ticker`, and `cleaned_name`.`}
    """
    return send_http_request('company_info_by_cik', cik=cik)


def company_info_by_ticker(*ignore, ticker): 
    """
    https://www.intellect.finance/API_Document#company_info_by_ticker
    Get company information by a company's ticker.

    :example: company_info_by_ticker(ticker='AAPL')
    
    :exception: ['ParameterMissingError']
    :param ticker: A ticker.
    :return: {'result': `A list of company information, deduped by `cik`, `sic`, `ticker`, and `cleaned_name`.`}
    """
    return send_http_request('company_info_by_ticker', ticker=ticker)


def list_sec_daily_filings(*ignore, date, cik=None, _NEXT_TOKEN_=None): 
    """
    https://www.intellect.finance/API_Document#list_sec_daily_filings
    Get the list of all filings reported to SEC on a certain date. 
    Usually this date is the filling date of the all the filings included. 
    In some rare cases, SEC will also include filings from previous days. 
    For each API call, we will return a max number of 500 entries. 
    If there are more than 500 filings in one day, 
    we will return a `_NEXT_TOKEN_` value, 
    and you can pass this value through the `_NEXT_TOKEN_` parameter in the API URL to continue retrieval more data.

    :example: list_sec_daily_filings(date='2022-02-01', cik='1652044', _NEXT_TOKEN_=500)
    
    :exception: ['ParameterInvalidError', 'ParameterMissingError']
    :param date: Date that SEC indexed the filings. Usually this date is the filling date.
    :param cik: Optional. If you only know the ticker of a company (say AAPL), you can get the corresponding CIK of that company can be retrieved through the `company_info_by_ticker` API.
    :param _NEXT_TOKEN_: Optional. Next token, used to continue to retrieve more data. If not provided, we will retrieve the data from the beginning.
    :return: {'result': `A list of filings.`}
    """
    return send_http_request('list_sec_daily_filings', date=date, cik=cik, _NEXT_TOKEN_=_NEXT_TOKEN_)


def sec_raw_financial_data(*ignore, cik, year_quarter, statement_type): 
    """
    https://www.intellect.finance/API_Document#sec_raw_financial_data
    Get the financial statement reported by a company in a given quarter. 
    Our data contains not only the most common financial items such as `Sales`, or `Net Income`, 
    but also the financial items in certain dimensions. For example, for Apple (cik is 320193), we provide the `Nert sales` by 
    each `ProductOrServiceAxis`, 
    ranging from `IPadMember`, `IPhoneMember`, `MacMember`, `WearablesHomeandAccessoriesMember`, and `ServiceMember` etc (these are the dimension values). 
    See the `dimension_type` in the return.

    :example: sec_raw_financial_data(cik=320193, year_quarter='2022Q1', statement_type='INCOME_STATEMENT')
    
    :exception: ['ParameterInvalidError', 'ParameterMissingError']
    :param cik: If you only know the ticker of a company (say AAPL), you can get the corresponding CIK of that company can be retrieved through the `company_info_by_ticker` API.
    :param year_quarter: The year-quarter of the statement, in the format such as `2022Q1`.
    :param statement_type: Must be one of ['CASHFLOW', 'BALANCE_SHEET', 'INCOME_STATEMENT'].
    :return: {'result': `A list of items in the statement.`}
    """
    return send_http_request('sec_raw_financial_data', cik=cik, year_quarter=year_quarter, statement_type=statement_type)


def sec_8k_6k_and_other(*ignore, cik, start_date, end_date): 
    """
    https://www.intellect.finance/API_Document#sec_8k_6k_and_other
    Get a list of 8-K, 6-K, and other filings (i.e. 13-F, 13-H, SC TO-T, CORRESP, DEF 14A, DEFA14A, PX14A6G, EC STAFF LETTER, etc) filings in a certain date period (cannot be more than 95 days). 
    8-K and 6-K are especially important as they are to announce the material events (i.e. deal, merger, earning, or new product, etc.) of a company. 
    8-K are for domestic companies (U.S.), whereas 6-K are for foreign companies. 
    Note that this API does not include 10-K, 10-Q, 20-F, 40-F, 3, 4, 5, and SC 13. These filings have their own separate APIs. 

    :example: sec_8k_6k_and_other(cik='1652044', start_date='2022-02-01', end_date='2022-02-05')
    
    :exception: ['ParameterInvalidError', 'ParameterMissingError']
    :param cik: If you only know the ticker of a company (say AAPL), you can get the corresponding CIK of that company can be retrieved through the `company_info_by_ticker` API.
    :param start_date: Start date for the filing date range.
    :param end_date: End date for the filing date range.
    :return: {'result': `A list of filings.`}
    """
    return send_http_request('sec_8k_6k_and_other', cik=cik, start_date=start_date, end_date=end_date)


def sec_10k_10q_20f_40f(*ignore, cik, start_date, end_date): 
    """
    https://www.intellect.finance/API_Document#sec_10k_10q_20f_40f
    Get a list of 10-K, 10-Q, 20-F, or 40-F filings in a certain date period (cannot be more than 380 days). 
    Such filings are the quarterly or annual report of companies. 
    10-K (annual) and 10-Q (quarterly) are for domestic companies (U.S.), 
    whereas 20-F and 40-F (both annual) are for foreign companies. 

    :example: sec_10k_10q_20f_40f(cik='1652044', start_date='2022-02-01', end_date='2022-02-05')
    
    :exception: ['ParameterInvalidError', 'ParameterMissingError']
    :param cik: If you only know the ticker of a company (say AAPL), you can get the corresponding CIK of that company can be retrieved through the `company_info_by_ticker` API.
    :param start_date: Start date for the filing date range.
    :param end_date: End date for the filing date range.
    :return: {'result': `A list of filings.`}
    """
    return send_http_request('sec_10k_10q_20f_40f', cik=cik, start_date=start_date, end_date=end_date)


def sec_345(*ignore, cik, start_date, end_date): 
    """
    https://www.intellect.finance/API_Document#sec_345
    Get a list of Form `3`, `4`, and `5` filings. 
    Form `3` is used for initial filings of insiders. 
    Form `4` is for the changes in ownership for insiders. 
    Form 5 is used if insiders had conducted security transactions during the year but failed to report them via SEC Form. 

    :example: sec_345(cik='1652044', start_date='2022-02-01', end_date='2022-02-05')
    
    :exception: ['ParameterInvalidError', 'ParameterMissingError']
    :param cik: If you only know the ticker of a company (say AAPL), you can get the corresponding CIK of that company can be retrieved through the `company_info_by_ticker` API.
    :param start_date: Start date for the filing date range.
    :param end_date: End date for the filing date range.
    :return: {'result': `A list of filings.`}
    """
    return send_http_request('sec_345', cik=cik, start_date=start_date, end_date=end_date)
