from IntellectFinanceAPI.API.Utility import send_http_request


def news_by_source(news_source, start_time, end_time): 
    """
    https://www.intellect.finance/API_Document#news_by_source
    Get a list of news by the news source (i.e. WSJ, Bloomberg, or CNBC, etc). The max time range shall be less than 7 days.

    :example: news_by_source(news_source='CNBC', start_time='2022-02-01 02:00:00', end_time='2022-02-01 12:00:00')
    
    :exception: ['ParameterInvalidError', 'ParameterMissingError']
    :param news_source: Source of the news. Available sources are `['Bloomberg', 'Fox', 'CNBC', 'WSJ', 'CNN', 'New York Times', "Barron's", 'Reuters', 'Businesswire', 'PR Newswire', 'Seeking Alpha']`.
    :param start_time: UTC start date time of the news.
    :param end_time: UTC start date time of the news.
    :return: {'result': `A list of news.`}
    """
    return send_http_request('news_by_source', news_source=news_source, start_time=start_time, end_time=end_time)


def news_by_ticker(ticker, start_date, end_date, stop_at_number_of_news=None, if_dedupe_news_ind=None, if_most_relevant_news_ind=None): 
    """
    https://www.intellect.finance/API_Document#news_by_ticker
    Get a list of news that is relevant to a company. The list will be sorted by the news' publish time (descending, which means later news will be on top of the list). Maximum number of news to retrieve is 1000.

    :example: news_by_ticker(ticker='AAPL', start_date='2022-02-01', end_date='2022-02-08', stop_at_number_of_news=1000, if_dedupe_news_ind='True', if_most_relevant_news_ind='False')
    
    :exception: ['ParameterInvalidError', 'ParameterMissingError']
    :param ticker: The ticker.
    :param start_date: Start date (UTC) of the news range. Its format should be `YYYY-MM-DD`. Default is 90 days earlier from today.
    :param end_date: End date (UTC) (including) of the news range. Its format should be `YYYY-MM-DD`. Default is today.
    :param stop_at_number_of_news: Optional (default value is `1000`). Max number of news to retrieve. Must be an integer between 1 and 1000. Default (if not provided) is 1000. If `if_most_relevant_news_ind` is `False` (default), it means we will only retrieve the latest `stop_at_number_of_news` number of pieces of news. If `if_most_relevant_news_ind` is `True`, it means we will only retrieve the top `stop_at_number_of_news` important news.
    :param if_dedupe_news_ind: Optional (default value is `True`). Sometimes, similar news will be reported by several different news sources. For example, on 2022-12-08, CNBC, WSJ and Bloomberg all reported the news that "FTC Sues to Block Microsoft’s Acquisition of Activision Blizzard". This option will enable the API to dedupe such duplicated news (typically keep the earliest news). Default is `True`. You can also get ALL the news (including the duplicated ones) by providing `False`.
    :param if_most_relevant_news_ind: Optional (default value is `False`). Pull relevant news only (Score of the relevance (`cos`) has to be equal or larger than 0.6 for the inputted ticker). Default is False.
    :return: {'result': `A list of news.`}
    """
    return send_http_request('news_by_ticker', ticker=ticker, start_date=start_date, end_date=end_date, stop_at_number_of_news=stop_at_number_of_news, if_dedupe_news_ind=if_dedupe_news_ind, if_most_relevant_news_ind=if_most_relevant_news_ind)


def news_by_topic(topic_name, start_date, end_date): 
    """
    https://www.intellect.finance/API_Document#news_by_topic
    Get list of news under one topic within a certain date range (cannot be more than 7 days). 

    :example: news_by_topic(topic_name='President Biden', start_date='2022-03-30', end_date='2022-04-05')
    
    :exception: ['ParameterInvalidError', 'ParameterMissingError', 'TopicNotFoundError']
    :param topic_name: A topic name. Note that we only accept topic names that are listed in the `time_series_topic_names` API.
    :param start_date: The start date (UTC) of the news related to this topic.
    :param end_date: The end date (UTC) (including) of the news related to this topic.
    :return: {'result': `See the result for the `news_by_source` API.`}
    """
    return send_http_request('news_by_topic', topic_name=topic_name, start_date=start_date, end_date=end_date)


def list_tickers_with_news(year=None, min_number_news_per_ticker=None): 
    """
    https://www.intellect.finance/API_Document#list_tickers_with_news
    Get a list of tickers and their number of news, sorted by the number of news in descending order.

    :example: list_tickers_with_news(year='2022', min_number_news_per_ticker=10)
    
    :exception: ['ParameterInvalidError', 'ParameterMissingError']
    :param year: Optional (default value is `EMPTY`). Filter the year of news. If not provided, we will pull data for the current year and the previous year.
    :param min_number_news_per_ticker: Optional (default value is `10`). Used to exclude the tickers with number of news less than the `min_number_news_per_ticker`. Default value is 10.
    :return: {'result': `A list of hashmaps.`}
    """
    return send_http_request('list_tickers_with_news', year=year, min_number_news_per_ticker=min_number_news_per_ticker)


def time_series_topic_names(start_date, end_date): 
    """
    https://www.intellect.finance/API_Document#time_series_topic_names
    Get a list of topic names within a date range (has to be less or equal than 90 days). 

    :example: time_series_topic_names(start_date='2023-06-01', end_date='2023-06-25')
    
    :exception: ['ParameterInvalidError', 'ParameterMissingError']
    :param start_date: Start date (UTC) of the news range. Its format should be `YYYY-MM-DD`.
    :param end_date: End date (UTC) (including) of the news range. Its format should be `YYYY-MM-DD`. The data range between the start date and the end date shall not be more than 90 days.
    :return: {'result': `A list of topics and the counts of occurrence of the topic, ordered by date (newest date is on the top).`}
    """
    return send_http_request('time_series_topic_names', start_date=start_date, end_date=end_date)


def time_series_topic_sentiment(topic_name, start_date, end_date): 
    """
    https://www.intellect.finance/API_Document#time_series_topic_sentiment
    Get a daily time series of sentiment scores for a topic (the time range cannot be more than 90 days.

    :example: time_series_topic_sentiment(topic_name='President Biden', start_date='2022-03-30', end_date='2022-06-27')
    
    :exception: ['ParameterInvalidError', 'ParameterMissingError', 'TopicNotFoundError']
    :param topic_name: A topic name. Note that we only accept topic names that are listed in the `time_series_topic_names` API.
    :param start_date: The start date (UTC) of the news related to this topic.
    :param end_date: The end date (UTC) (including) of the news related to this topic.
    :return: {'result': `A list of sentiment scores (with number of news), ordered by date.`}
    """
    return send_http_request('time_series_topic_sentiment', topic_name=topic_name, start_date=start_date, end_date=end_date)


def time_series_topic_embedding(topic_name, start_date, end_date): 
    """
    https://www.intellect.finance/API_Document#time_series_topic_embedding
    Get a weekly time series of the embedding vectors for the inputted topic. The embedding vector of a topic in a week is the weighted average of the embedding vectors of all the news related to the inputted topic in that week. See the `estimate_embedding_vector` API regarding how the embedding vector is estimated.

    :example: time_series_topic_embedding(topic_name='President Biden', start_date='2022-01-23', end_date='2022-02-22')
    
    :exception: ['ParameterInvalidError', 'ParameterMissingError', 'TopicNotFoundError']
    :param topic_name: A topic name. Note that we only accept topic names that are listed in the `time_series_topic_names` API.
    :param start_date: The start date (UTC) of the news related to this topic.
    :param end_date: The end date (UTC) (including) of the news related to this topic.
    :return: {'result': `A list of hashmaps, ordered by date in the descending order.`}
    """
    return send_http_request('time_series_topic_embedding', topic_name=topic_name, start_date=start_date, end_date=end_date)


def time_series_relevant_topics_by_topic(topic_name, start_date, end_date): 
    """
    https://www.intellect.finance/API_Document#time_series_relevant_topics_by_topic
    Get a weekly time series for the most relevant topics to the inputted topic.

    :example: time_series_relevant_topics_by_topic(topic_name='President Biden', start_date='2022-01-23', end_date='2022-04-22')
    
    :exception: ['ParameterInvalidError', 'ParameterMissingError', 'TopicNotFoundError']
    :param topic_name: A topic name. Note that we only accept topic names that are listed in the `time_series_topic_names` API.
    :param start_date: The start date (UTC) of the news related to this topic.
    :param end_date: The end date (UTC) (including) of the news related to this topic.
    :return: {'result': `A list of hashmaps, ordered by date in the descending order.`}
    """
    return send_http_request('time_series_relevant_topics_by_topic', topic_name=topic_name, start_date=start_date, end_date=end_date)


def time_series_relevant_tickers_by_topic(topic_name, start_date, end_date): 
    """
    https://www.intellect.finance/API_Document#time_series_relevant_tickers_by_topic
    Get a daily time series for the most relevant tickers for the inputted topic.

    :example: time_series_relevant_tickers_by_topic(topic_name='President Biden', start_date='2022-01-23', end_date='2022-04-22')
    
    :exception: ['ParameterInvalidError', 'ParameterMissingError', 'TopicNotFoundError']
    :param topic_name: A topic name. Note that we only accept topic names that are listed in the `time_series_topic_names` API.
    :param start_date: The start date (UTC) of the news related to this topic.
    :param end_date: The end date (UTC) (including) of the news related to this topic.
    :return: {'result': `A list of hashmaps, ordered by date in the descending order.`}
    """
    return send_http_request('time_series_relevant_tickers_by_topic', topic_name=topic_name, start_date=start_date, end_date=end_date)


def estimate_embedding_vector(input): 
    """
    https://www.intellect.finance/API_Document#estimate_embedding_vector
    Calculate a 768 dimension dense embedding vector using the <a target='_blank' href='https://huggingface.co/sentence-transformers/paraphrase-mpnet-base-v2'>sentence-transformers/paraphrase-mpnet-base-v2</a> model for any ticker, topic, or a paragraph. If you provide a ticker, we will calculate the embedding vector as the weighted average of the embeddings vectors of the related news since 2020, with higher weights assigned to the more recent news and more relevant news. <br><br>We also guarantee that the ticker's embedding always contain the most updated information, by re-calculating the embeddings for tickers based on the latest news in our backend data pipeline. <br><br>If the inputted text is longer than 1024 characters, we suggest you to use the `POST` method (instead of the GET method), and put hte inputted text into the `data` field. See the demo below.

    :example: estimate_embedding_vector(input='GOOGL')
    
    :exception: ['ParameterMissingError']
    :param input: Any input, such as ticker, topic, or a paragraph.
    :return: {'result': `A hashmap with the embedding information.`}
    """
    return send_http_request('estimate_embedding_vector', input=input)


def short_summary(inputted_paragraph): 
    """
    https://www.intellect.finance/API_Document#short_summary
    Provide a short summary for the inputted text. We fine-tuned the Llama 2 7B model to predict the news title with the content of English news from top ranked financial news sites. Therefore, the short summary you will get from this API will also have the flavor of news title.<br><br>If the inputted text is longer than 1024 characters, we suggest you to use the `POST` method (instead of the GET method), and put hte inputted text into the `data` field. See the demo below.

    :example: short_summary(inputted_paragraph='JOHANNESBURG—African fintech companies have found creative ways to help the continent’s consumers spend their money. Traditional payments companies want in.
Global payment giants, including Mastercard MA -2.13 decrease; red down pointing triangle and Visa V -1.55 decrease; red down pointing triangle, are pouring billions of dollars into African companies that have powered a sharp expansion in e-commerce on the continent. Recent deals have focused on mobile-money operators, which allow users to send funds using simple cellphones, and platforms that facilitate such payments for merchants such as Uber Technologies UBER -3.11 decrease; red down pointing triangle, Netflix or Estée Lauder without relying on credit cards or bank accounts.
The investments come on the back of extraordinary growth in e-commerce in Africa, where online transactions have long lagged behind other regions, especially North America.')
    
    :exception: ['ParameterMissingError']
    :param inputted_paragraph: Any text (must less than 3000 words).
    :return: {'result': `A hashmap with the short summary.`}
    """
    return send_http_request('short_summary', inputted_paragraph=inputted_paragraph)


def zero_shot_classifier(inputted_paragraph, list_topics): 
    """
    https://www.intellect.finance/API_Document#zero_shot_classifier
    Measure the relevance between the inputted text anc any given topic. The model we use for this API is a Llama 2 7B model fine-tuned on financial, political, or tech news, with the 'truth' data distilled from ChatGPT. <br><br>If the inputted text is longer than 1024 characters, we suggest you to use the `POST` method (instead of the GET method), and put hte inputted text into the `data` field. See the demo below.

    :example: zero_shot_classifier(inputted_paragraph='Pfizer Prices Covid Drug Paxlovid at $1,400 for a Five-Day Course. The drugmaker, which has begun negotiating with pharmacy-benefit managers and health plans this week, is expected to offer steep discounts to ensure wide access.', list_topics='Politics; Retail; Defence Industry; Healthcare; Geopolitical Risks')
    
    :exception: ['ParameterMissingError']
    :param inputted_paragraph: Any text, such as a piece of news, or a paragraph.
    :param list_topics: A list of topics, separated by `;`.
    :return: {'result': `A hashmap contains the relevance score of each provided topic.`}
    """
    return send_http_request('zero_shot_classifier', inputted_paragraph=inputted_paragraph, list_topics=list_topics)


def sentiment_overall(input): 
    """
    https://www.intellect.finance/API_Document#sentiment_overall
    Estimate the sentiment scores for the inputted sentence. The sentiment score ranges from -1 to +1, where -1 means extremely positive, and +1 means extremely positive. The model we use for this API is the <a target='_blank' href='https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment'>cardiffnlp/twitter-roberta-base-sentiment model</a>. <br><br>If the inputted text is longer than 1024 characters, we suggest you to use the `POST` method (instead of the GET method), and put hte inputted text into the `data` field. See the demo below.

    :example: sentiment_overall(input='Tesla’s Earnings Fall as Price Cuts Weigh on Profit.')
    
    :exception: ['ParameterMissingError']
    :param input: Any input, such as a piece of news, or a paragraph.
    :return: {'result': `A hashmap with the sentiment score.`}
    """
    return send_http_request('sentiment_overall', input=input)


def time_series_ticker_sentiment(ticker, start_date, end_date): 
    """
    https://www.intellect.finance/API_Document#time_series_ticker_sentiment
    Get a daily time series of sentiment scores for a ticker (the time range cannot be more than 90 days). 

    :example: time_series_ticker_sentiment(ticker='AMZN', start_date='2021-06-30', end_date='2021-09-27')
    
    :exception: ['ParameterInvalidError', 'ParameterMissingError']
    :param ticker: A ticker.
    :param start_date: The start date (UTC) of the news.
    :param end_date: The end date (UTC) (including) of the news.
    :return: {'result': `A time series (list) of sentiment scores (with number of news), ordered by date.`}
    """
    return send_http_request('time_series_ticker_sentiment', ticker=ticker, start_date=start_date, end_date=end_date)


def relevant_tickers_by_ticker(ticker): 
    """
    https://www.intellect.finance/API_Document#relevant_tickers_by_ticker
    Get a list of the most relevant tickers to the input ticker. The more frequent that ticker A and B appear in the same news, then the more relevant these two tickers are.

    :example: relevant_tickers_by_ticker(ticker='GOOGL')
    
    :exception: ['ExceptionNoTickerFound', 'ParameterMissingError']
    :param ticker: A ticker.
    :return: {'result': `A list of dictionaries, ordered by the relevance score (high to low). Each dictionary contains a relevant ticker to the input ticker, and the degree of their relevance (relevance sores).`}
    """
    return send_http_request('relevant_tickers_by_ticker', ticker=ticker)


def relevance_score_between_two_tickers(ticker_1, ticker_2): 
    """
    https://www.intellect.finance/API_Document#relevance_score_between_two_tickers
    Calculate the relevance score between two tickers. The score measures the similarity of the two tickers/companies. Note that the relevance score may change every day as we receive new information (i.e. new events, or news) about each ticker.

    :example: relevance_score_between_two_tickers(ticker_1='GOOGL', ticker_2='MSFT')
    
    :exception: ['ExceptionNoTickerFound', 'ParameterMissingError']
    :param ticker_1: A ticker.
    :param ticker_2: Another ticker.
    :return: {'result': `The degree of relevance or similarity between the two tickers, ranging from (0, 1). The higher the score, the more related/similar are these two tickers.`}
    """
    return send_http_request('relevance_score_between_two_tickers', ticker_1=ticker_1, ticker_2=ticker_2)


def annualized_sharpe_ratio_by_ticker(ticker, start_date, end_date, risk_free_rate, smart_sharpe_flag=None): 
    """
    https://www.intellect.finance/API_Document#annualized_sharpe_ratio_by_ticker
    Calculate the annualized Sharpe Ratio for a ticker in a given period (should be less than 370 days).

    :example: annualized_sharpe_ratio_by_ticker(ticker='MSFT', start_date='2021-01-01', end_date='2021-12-31', risk_free_rate=0.02, smart_sharpe_flag='false')
    
    :exception: ['ExceptionNoTickerFound', 'ParameterInvalidError', 'ParameterMissingError']
    :param ticker: A ticker.
    :param start_date: Start date. Its format should be `YYYY-MM-DD`.
    :param end_date: End date (including). Its format should be `YYYY-MM-DD`. The max time range between `start_date` and `end_date` has to be less than 370 days.
    :param risk_free_rate: Risk-free rate of interest (expressed in annualized term).
    :param smart_sharpe_flag: Optional (default value is `false`). A boolean flag (`false` or `true`) indicating whether a Smart Sharpe ratio is returned. Default is `false`.
    :return: {'result': `The Sharpe ratio in annualized term (round to 3 decimal places).`}
    """
    return send_http_request('annualized_sharpe_ratio_by_ticker', ticker=ticker, start_date=start_date, end_date=end_date, risk_free_rate=risk_free_rate, smart_sharpe_flag=smart_sharpe_flag)


def max_drawdown_by_ticker(ticker, start_date, end_date): 
    """
    https://www.intellect.finance/API_Document#max_drawdown_by_ticker
    Calculate the maximum drawdown (MDD) for a ticker in a given period (should be less than 370 days).

    :example: max_drawdown_by_ticker(ticker='MSFT', start_date='2021-01-01', end_date='2021-12-31')
    
    :exception: ['ExceptionNoTickerFound', 'ParameterInvalidError', 'ParameterMissingError']
    :param ticker: A ticker.
    :param start_date: Start date. Its format should be `YYYY-MM-DD`.
    :param end_date: End date (including). Its format should be `YYYY-MM-DD`. Should be less 370 days from the start_date.
    :return: {'result': `A hashmap that contains the maximum drawdown and the date at which the maximum drawdown occurs.`}
    """
    return send_http_request('max_drawdown_by_ticker', ticker=ticker, start_date=start_date, end_date=end_date)


def treasury_yield(duration, start_date, end_date): 
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


def treasury_real_yield(duration, start_date, end_date): 
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


def fed_fund_target_rate(start_date, end_date): 
    """
    https://www.intellect.finance/API_Document#fed_fund_target_rate
    
    Get the Federal fund target rate for a time period (has to be less than 370 days). The federal funds rate is the interest rate at which depository institutions trade federal funds 
    (balances held at Federal Reserve Banks) with each other overnight.
    The Federal Open Market Committee (FOMC) meets eight times a year to determine the federal funds target rate. 
    See <a href='https://fred.stlouisfed.org/series/DFF' target='_blank'>https://fred.stlouisfed.org/series/DFF</a>.

    :example: fed_fund_target_rate(start_date='2021-01-01', end_date='2021-03-01')
    
    :exception: ['ParameterInvalidError', 'ParameterMissingError']
    :param start_date: Start date. Its format should be `YYYY-MM-DD`.
    :param end_date: End date (including). Its format should be `YYYY-MM-DD`. The max time range between `start_date` and end_date has to be less than 370 days.
    :return: {'result': `A time series of the Fed fund target rate data.`}
    """
    return send_http_request('fed_fund_target_rate', start_date=start_date, end_date=end_date)


def tickers_available(): 
    """
    https://www.intellect.finance/API_Document#tickers_available
    Get a full list of currently active tickers.

    :example: tickers_available()
    
    :exception: ['ParameterMissingError']
    :return: {'result': `A list of tickers that are active (not de-listed).`}
    """
    return send_http_request('tickers_available', )


def company_info_by_cik(cik): 
    """
    https://www.intellect.finance/API_Document#company_info_by_cik
    Get company information by Central Index Key (CIK) number.

    :example: company_info_by_cik(cik=1652044)
    
    :exception: ['ExceptionNoCIKFound', 'ParameterMissingError']
    :param cik: A Central Index Key (CIK) number.
    :return: {'result': `A list of company information, deduped by ['cik', 'sic', 'ticker', 'cleaned_name'].`}
    """
    return send_http_request('company_info_by_cik', cik=cik)


def company_info_by_ticker(ticker): 
    """
    https://www.intellect.finance/API_Document#company_info_by_ticker
    Get company information by a company's ticker.

    :example: company_info_by_ticker(ticker='AAPL')
    
    :exception: ['ExceptionNoTickerFound', 'ParameterMissingError']
    :param ticker: A ticker.
    :return: {'result': `A list of company information, deduped by ['cik', 'sic', 'ticker', 'cleaned_name'].`}
    """
    return send_http_request('company_info_by_ticker', ticker=ticker)


def search_company(input): 
    """
    https://www.intellect.finance/API_Document#search_company
    Get company information by searching a company's ticker, CIK or name. This API supports the auto-complete functionality (powered by Elasticsearch). Auto-completion means that you don't need to input the full name of the company. For example, just input `starb`, and we will return `Starbucks`. Note that we will return at most 20 items in this search API. 

    :example: search_company(input='Starb')
    
    :exception: ['ParameterMissingError']
    :param input: A company's ticker, CIK or name (don't need to input the full name).
    :return: {'result': `A list of company that matched the input.`}
    """
    return send_http_request('search_company', input=input)


def big_index_holdings(index_name): 
    """
    https://www.intellect.finance/API_Document#big_index_holdings
    Get an updated list of stock tickers and their weights held in a stock index.

    :example: big_index_holdings(index_name=1652044)
    
    :exception: ['ParameterMissingError']
    :param index_name: The index name. Currently we cover the following indices ['SP500', 'SP_MIDCAP_400', 'DIJA', 'NASDAQ_100', 'Russell_2000'].
    :return: {'result': `The holdings of the index, and the weight of each holding.`}
    """
    return send_http_request('big_index_holdings', index_name=index_name)


def sec_raw_financial_data(cik_or_ticker, year_quarter, statement_type): 
    """
    https://www.intellect.finance/API_Document#sec_raw_financial_data
    Get the raw financial statement reported by a company in a given quarter. 
    Our data contains not only the most common financial items such as `Sales`, or `Net Income`, 
    but also the financial items in certain dimensions. For example, for Apple (cik is 320193), we provide the `Nert sales` by 
    each `ProductOrServiceAxis`, 
    ranging from `IPadMember`, `IPhoneMember`, `MacMember`, `WearablesHomeandAccessoriesMember`, and `ServiceMember` etc (these are the dimension values). 
    See the `dimension_type` in the return.

    :example: sec_raw_financial_data(cik_or_ticker=320193, year_quarter='2022Q1', statement_type='INCOME_STATEMENT')
    
    :exception: ['ExceptionNoCIKFound', 'ExceptionNoTickerFound', 'ParameterInvalidError', 'ParameterMissingError']
    :param cik_or_ticker: CIK or ticker.
    :param year_quarter: The year-quarter of the statement, in the format such as `2022Q1`.
    :param statement_type: Must be one of ['FINANCIAL_NOTES', 'CASHFLOW', 'BALANCE_SHEET', 'INCOME_STATEMENT'].
    :return: {'result': `A list of items in the statement.`}
    """
    return send_http_request('sec_raw_financial_data', cik_or_ticker=cik_or_ticker, year_quarter=year_quarter, statement_type=statement_type)


def sec_cleaned_financial_data(cik_or_ticker, stmt=None, q_or_ttm=None, end_year_q=None): 
    """
    https://www.intellect.finance/API_Document#sec_cleaned_financial_data
    Get the financial statement of a company in a range of quarters. This API provides the essentially same data as the `sec_raw_financial_data` API, but this API 1) cleans up the raw data to make it presentable as a data.frame or in Excel, and 2) provides financial data for multiple quarters, rather than single quarter like the `sec_raw_financial_data` API.

    :example: sec_cleaned_financial_data(cik_or_ticker=789019, stmt='INCOME_STATEMENT', q_or_ttm='ttm', end_year_q='2023Q3')
    
    :exception: ['ExceptionNoCIK', 'ExceptionNoData', 'ParameterInvalidError', 'ParameterMissingError']
    :param cik_or_ticker: CIK or ticker a company.
    :param stmt: Optional (default value is `INCOME_STATEMENT`). Type of Statement of the company. A valid option should be one of one of ['FINANCIAL_NOTES', 'CASHFLOW', 'BALANCE_SHEET', 'INCOME_STATEMENT']. Default is `INCOME_STATEMENT`.
    :param q_or_ttm: Optional (default value is `ttm`). Get `q` (quarterly) or `ttm` (each quarter contains the data from the trailing 12 months) data. Default is `ttm`.
    :param end_year_q: Optional (default value is `LATEST`). Ending calendar (not fiscal) year and quarter. The format should be like `2023Q3`, or `LATEST`. Default is `LATEST`, which means we will just return the latest available data. If you provide a specific quarter, the quarter has to be later than `2023Q3`.
    :return: {'result': `Cleaned financial statement for at least 8 quarters (if `q_or_ttm`) is `q`), or at least  5 years (if `q_or_ttm` is `ttm` or `yearly`). It is a hashmap (with key `df_main` representing the major financial items, and `df_children` representing for financial items in certain dimensions).`}
    """
    return send_http_request('sec_cleaned_financial_data', cik_or_ticker=cik_or_ticker, stmt=stmt, q_or_ttm=q_or_ttm, end_year_q=end_year_q)


def fundamental_metrics(cik_or_ticker, metric_name, start_year_quarter=None, end_year_quarter=None): 
    """
    https://www.intellect.finance/API_Document#fundamental_metrics
    Get fundamental metrics (such as P/E and P/S ratios) by quarter. If the metric requires stock price as the input (such as PE), we will use the latest stock price for the latest quarter, whereas for other quarters, we will use the volume-weighted average end-of-day stock price one month after the fiscal quarter ends (For example, if the fiscal quarter ends at 12/31/2022, we will use the stock price from 02/01/2023 - 02/28/2023).

    :example: fundamental_metrics(cik_or_ticker=789019, metric_name='PE', start_year_quarter='2021Q3', end_year_quarter='2023Q4')
    
    :exception: ['ExceptionNoData', 'ParameterInvalidError', 'ParameterMissingError']
    :param cik_or_ticker: CIK or ticker a company.
    :param metric_name: Metric name. Must be one of ['Market-Cap', 'Dividend-Yield', 'Outstanding-Shares', 'EBIT', 'EBITDA', 'Book-Value', 'Tangible-Book-Value', 'Enterprise-Value', 'PE-Diluted', 'PE', 'PS', 'FCF', 'Price-to-FCF-Ratio', 'Price-to-Book-Value', 'Price-to-Tangible-Book-Value', 'Gross-Margin', 'Operating-Margin', 'Net-Margin', 'Return-on-Invested-Capital', 'Return-on-Equity', 'Return-on-Asset', 'Interest-Coverage', 'Current-Ratio', 'Quick-Ratio', 'Receivables-Turnover', 'Asset-Turnover'].
    :param start_year_quarter: Optional (default value is `None`). Default is 7 quarters from the latest available quarter.
    :param end_year_quarter: Optional (default value is `None`). Default is the latest available quarter.
    :return: {'result': `List of fundamental metrics.`}
    """
    return send_http_request('fundamental_metrics', cik_or_ticker=cik_or_ticker, metric_name=metric_name, start_year_quarter=start_year_quarter, end_year_quarter=end_year_quarter)


def list_sec_daily_filings(date, cik=None, _NEXT_TOKEN_=None): 
    """
    https://www.intellect.finance/API_Document#list_sec_daily_filings
    Get the list of all filings reported to SEC on a certain date. 
    Usually this date is the filling date of all the filings included. 
    In some rare cases, SEC will also include filings from previous days. 
    For each API call, we will return a max number of 500 entries. 
    If there are more than 500 filings in one day, 
    we will return a `_NEXT_TOKEN_` value, 
    and you can pass this value through the `_NEXT_TOKEN_` parameter in the API URL to continue to retrieve more data.

    :example: list_sec_daily_filings(date='2022-02-01', cik='1652044', _NEXT_TOKEN_=500)
    
    :exception: ['ParameterInvalidError', 'ParameterMissingError']
    :param date: Date that SEC indexed the filings. Usually this date is the filling date.
    :param cik: Optional (default value is `EMPTY`). If you only know the ticker of a company (say AAPL), the corresponding CIK of that company can be retrieved through the `company_info_by_ticker` API.
    :param _NEXT_TOKEN_: Optional (default value is `None`). Next token, used to continue to retrieve more data. If not provided, we will retrieve the data from the beginning.
    :return: {'result': `A list of filings.`}
    """
    return send_http_request('list_sec_daily_filings', date=date, cik=cik, _NEXT_TOKEN_=_NEXT_TOKEN_)


def sec_8k_6k(cik_or_ticker, start_date, end_date): 
    """
    https://www.intellect.finance/API_Document#sec_8k_6k
    Get a list of 8-K or 6-K filings from start_date to end_date (cannot be more than 700 days). 
    8-K and 6-K are especially important as they are to announce the material events (i.e. deal, merger, earning, or new product, etc.) of a company. 
    8-K are for domestic companies (U.S.), whereas 6-K are for foreign companies. 
    Note that this API does not include 10-K, 10-Q, 20-F, 40-F, 3, 4, 5, and SC 13. These filings have their own separate APIs. 

    :example: sec_8k_6k(cik_or_ticker='1652044', start_date='2022-02-01', end_date='2022-02-05')
    
    :exception: ['ExceptionNoCIKFound', 'ExceptionNoTickerFound', 'ParameterInvalidError', 'ParameterMissingError']
    :param cik_or_ticker: CIK or ticker.
    :param start_date: Start date for the filing date range.
    :param end_date: End date for the filing date range.
    :return: {'result': `A list of filings.`}
    """
    return send_http_request('sec_8k_6k', cik_or_ticker=cik_or_ticker, start_date=start_date, end_date=end_date)


def sec_other(cik_or_ticker, start_date, end_date): 
    """
    https://www.intellect.finance/API_Document#sec_other
    Get a list of `other` filings (i.e. 13-F, 13-H, SC TO-T, CORRESP, DEF 14A, DEFA14A, PX14A6G, EC STAFF LETTER, etc) filings in a certain date period (cannot be more than 190 days). 
    Note that this API does not include 10-K, 10-Q, 20-F, 40-F, 3, 4, 5, 8-K, 6-K, and SC 13. These filings have their own separate APIs. 

    :example: sec_other(cik_or_ticker='1652044', start_date='2022-02-01', end_date='2022-02-05')
    
    :exception: ['ExceptionNoCIKFound', 'ExceptionNoTickerFound', 'ParameterInvalidError', 'ParameterMissingError']
    :param cik_or_ticker: CIK or ticker.
    :param start_date: Start date for the filing date range.
    :param end_date: End date for the filing date range.
    :return: {'result': `A list of filings.`}
    """
    return send_http_request('sec_other', cik_or_ticker=cik_or_ticker, start_date=start_date, end_date=end_date)


def sec_10k_10q_20f_40f(cik_or_ticker, start_date, end_date): 
    """
    https://www.intellect.finance/API_Document#sec_10k_10q_20f_40f
    Get a list of 10-K, 10-Q, 20-F, or 40-F filings in a certain date period (cannot be more than 380 days). 
    Such filings are the quarterly or annual report of companies. 
    10-K (annual) and 10-Q (quarterly) are for domestic companies (U.S.), 
    whereas 20-F and 40-F (both annual) are for foreign companies. 

    :example: sec_10k_10q_20f_40f(cik_or_ticker='1652044', start_date='2022-02-01', end_date='2022-02-05')
    
    :exception: ['ExceptionNoCIKFound', 'ExceptionNoTickerFound', 'ParameterInvalidError', 'ParameterMissingError']
    :param cik_or_ticker: CIK or ticker.
    :param start_date: Start date for the filing date range.
    :param end_date: End date for the filing date range.
    :return: {'result': `A list of filings.`}
    """
    return send_http_request('sec_10k_10q_20f_40f', cik_or_ticker=cik_or_ticker, start_date=start_date, end_date=end_date)


def sec_345(cik_or_ticker, start_date, end_date): 
    """
    https://www.intellect.finance/API_Document#sec_345
    Get a list of Form `3`, `4`, and `5` filings. 
    Form `3` is used for initial filings of insiders. 
    Form `4` is for the changes in ownership for insiders. 
    Form 5 is used if insiders had conducted security transactions during the year but failed to report them via SEC Form. 

    :example: sec_345(cik_or_ticker='1652044', start_date='2022-02-01', end_date='2022-02-05')
    
    :exception: ['ExceptionNoCIKFound', 'ExceptionNoTickerFound', 'ParameterInvalidError', 'ParameterMissingError']
    :param cik_or_ticker: CIK or ticker.
    :param start_date: Start date for the filing date range.
    :param end_date: End date for the filing date range.
    :return: {'result': `A list of filings.`}
    """
    return send_http_request('sec_345', cik_or_ticker=cik_or_ticker, start_date=start_date, end_date=end_date)
