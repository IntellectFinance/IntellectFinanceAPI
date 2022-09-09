# IntellectFinanceAPI

An open-source package for the [intellect.finance](https://www.intellect.finance/API_Document) API.

### How to Use this Package

1. Please run the following code to set up the API key first. You can claim or change the API Key through https://www.intellect.finance/User?TabNameUserScreen=API+Keys.

```python
from IntellectFinanceAPI import set_api_key
set_api_key('TestKey')  # you need to replace this API key with your own API key.
```

2. Run `import` for an API function, then you can start using it! Below we use the `news_by_ticker` API as an example. 
You can find all the available APIs in our online [API doc](https://www.intellect.finance/API_Document).

    **Note that we only accept [keyword arguments, not the positional arguments](https://www.educative.io/answers/what-are-keyword-arguments-in-python), in the API function.**

```python
from pprint import pprint
from IntellectFinanceAPI import news_by_ticker

r = news_by_ticker(ticker='AAPL', start_date='2022-06-01', end_date='2022-06-30')

pprint(r['result'])

# [
#  {'emo': -0.36,
#   'h': 'BNPL firm Openpay pauses U.S. operations, to focus on Australia',
#   'i': 'https://www.reuters.com/pf/resources/images/reuters/reuters-default.png?d=100',
#   'landing_index': 24.0,
#   'len': 1310.0,
#   'len_by_p': 7.0,
#   'other_tickers': {'AAPL': {'cos': 0.363, 'paragraph_index': 2.0},
#                     'OPY.AX': {'paragraph_index': 0.0}},
#   'p': 'Reuters',
#   'pub_t': '2022-06-30 23:22:50',
#   's': ['Australian buy-now-pay-later firm Openpay Group Ltd said on Friday it '
#         'will "indefinitely" pause its United States operations and '
#         '"materially" reduce its workforce, citing adverse macroeconomic and '
#         'public market conditions.'],
#   'sub_p': ['Finance',
#             'Business',
#             'Sustainable Business',
#             'Government',
#             'Litigation',
#             'Transactional',
#             'Legal',
#             'Tech'],
#   'u': 'https://www.reuters.com/business/finance/bnpl-firm-openpay-pauses-us-operations-focus-australia-2022-06-30'},
#  {'emo': -0.85,
#   'h': 'Big technology stocks like Tesla, Amazon and Microsoft just finished '
#        'their worst quarter in years',
#   'i': 'https://image.cnbcfm.com/api/v1/image/107083439-1656624430121-gettyimages-1395183190-05022022-elonmuskmayemoss_z_003_c196544d-5bd8-4e51-b217-40.jpeg?v=1656624476&w=1920&h=1080',
#   'landing_index': 0.0,
#   'len': 2841.0,
#   'len_by_p': 10.0,
#    ...},
# ....
# ]
```

### How to Process the Results

You can get the results from the `result` key.

In addition, if the result is a list, typically you can transform it to a pandas `data.frame` (it requires you to pip install `pandas` first).


```python
import pandas as pd
from IntellectFinanceAPI import news_by_ticker

r = news_by_ticker(ticker='AAPL', start_date='2022-06-01', end_date='2022-06-20')
pd.DataFrame(r['result'])
#       emo                                        h                                        i  landing_index      len  len_by_p                            other_tickers          p                pub_t                                        s                                    sub_p                                        u
#0    0.44  US Sanctions Helped China Supercharg...  https://assets.bwbx.io/images/users/...            8.0   4591.0      18.0  {'002415': {'cos': 0.349, 'country':...  Bloomberg  2022-06-20 21:00:00  [Most of the world's fastest-expandi...                    [technology, Economy]  https://www.bloomberg.com/news/artic...
#1   -0.13  Opinion | Semiconductor Dependency I...  https://images.wsj.net/im-566633/social           25.0  10765.0      25.0  {'AAPL': {'cos': 0.511, 'paragraph_i...        WSJ  2022-06-20 20:54:00  [The U.S. Innovation and Competition...              [Commentary (U.S.), _HOME_]  https://www.wsj.com/articles/semicon...
#2    0.94  Biden says he is 'proud' of Apple re...  https://media.cnn.com/api/v1/images/...            0.0   7506.0      12.0  {'AAPL': {'cos': 0.31, 'paragraph_in...        CNN  2022-06-20 20:39:51  [President Joe Biden said he was "pr...       [Investing, Perspectives, Economy]  https://www.cnn.com/2022/06/20/tech/...
#3   -0.37  Hedge Funds Are the Rage as ‘Nothing...  https://assets.bwbx.io/images/users/...           20.0   7015.0      15.0  {'AAPL': {'cos': 0.358, 'country': '...  Bloomberg  2022-06-18 20:00:00  [Fed is maybe regaining some control...      [markets, _HOME_, Markets, Economy]  https://www.bloomberg.com/news/artic...
#4   -0.70  BTS Hiatus Deals Another Blow to Kor...  https://assets.bwbx.io/images/users/...           20.0   3654.0      17.0  {'289220': {'country': 'KS', 'paragr...  Bloomberg  2022-06-18 00:00:00  [Basket of Korean pop, drama shares ...               [markets, _HOME_, Markets]  https://www.bloomberg.com/news/artic...
#..    ...                                      ...                                      ...            ...      ...       ...                                      ...        ...                  ...                                      ...                                      ...                                      ...
#105 -0.88  Trillions at Stake in India as Women...  https://assets.bwbx.io/images/users/...            9.0  11313.0      37.0  {'AAPL': {'cos': 0.288, 'country': '...  Bloomberg  2022-06-02 00:01:13  [A small fraction of women in India ...                      [equality, Economy]  https://www.bloomberg.com/news/featu...
#106  0.21  Meta's Sheryl Sandberg Is Stepping Down  https://images.barrons.com/im-555735...           32.0   1699.0      13.0  {'AAPL': {'cos': 0.304, 'paragraph_i...   Barron's  2022-06-01 20:06:00  ["It is time for me to write the nex...           [Stock Alert, _HOME_, Feature]  https://www.barrons.com/articles/she...
#107  0.28  Amazon Splits Its Stock Next Week. W...  https://images.barrons.com/im-555253...            6.0   4308.0      19.0  {'AAPL': {'cos': 0.564, 'paragraph_i...   Barron's  2022-06-01 17:34:00  [Some of a flurry of recently announ...               [Feature, _HOME_, Markets]  https://www.barrons.com/articles/ama...
#108 -0.04  Elon Musk reportedly tells Tesla wor...  https://image.cnbcfm.com/api/v1/imag...            0.0   2657.0      13.0  {'AAPL': {'cos': 0.373, 'paragraph_i...       CNBC  2022-06-01 14:10:07  [Elon Musk has reportedly told Tesla...  [Tech, Business, Investing, Politics...  https://www.cnbc.com/2022/06/01/elon...
#109 -0.74  Amazon sharply criticizes looming an...  https://media.cnn.com/api/v1/images/...            0.0   6979.0       7.0  {'AAPL': {'cos': 0.45, 'paragraph_in...        CNN  2022-06-01 13:30:47  [Amazon has sharply criticized a loo...       [Investing, Perspectives, Economy]  https://www.cnn.com/2022/06/01/tech/...
#[110 rows x 12 columns]
```
### How to use the `_NEXT_TOKEN_` parameter.
For certain APIs. we limit the number of items that can be retrieved each time. 
In those APIs, if the number of available results is more than the API's limit, 
we will return a `_NEXT_TOKEN_`, which can be passed to the URL again to retrieve more results. 

In the example below for the 'list_sec_daily_filings' API, 
due to this API's limit on the number of items returned each time, the first request will only return the first 500 SEC filings. 
However, users can then use the `_NEXT_TOKEN_` parameter returned to query more SEC filings. See the code below.

```python
from IntellectFinanceAPI import list_sec_daily_filings

# initial request without _NEXT_TOKEN_
r = list_sec_daily_filings(date='2022-02-01')
# You can pass the _NEXT_TOKEN_ in the next request, and go on.
r = list_sec_daily_filings(date='2022-02-01', _NEXT_TOKEN_=r['_NEXT_TOKEN_'])

```
### How to Process the Errors

You can import any error from `IntellectFinanceAPI.API.ErrorTypes`, such as:
```python
from IntellectFinanceAPI.API.ErrorTypes import ParameterMissingError
```

To understand the possible exceptions raised by a particular API function, 
please refer our [online documentation](https://www.intellect.finance/API_Document) 
(see the `Exceptions` section in any of the API function's documentation).


We also provide rich error information of the error through the `http_response` attribute of the exception. See the code below:


```python
from pprint import pprint
from IntellectFinanceAPI import relevant_tickers_by_topic
from IntellectFinanceAPI.API.ErrorTypes import TopicIsMergedToAnotherTopicError

try:
    relevant_tickers_by_topic(year=2021, topic_name="China's credit demand slumps as covid lockdowns curb")
except TopicIsMergedToAnotherTopicError as e:
    pprint(e.http_response)

# {'_NUMBER_CREDITS_CONSUMED_': 1,
#  'error': "The topic `China's credit demand slumps as covid lockdowns curb` "
#           "has been merged to the topic `Hidden impact on China's financial "
#           'center`.',
#  'error_type': 'TopicIsMergedToAnotherTopicError',
#  'new_topic_name': "Hidden impact on China's financial center"}
```