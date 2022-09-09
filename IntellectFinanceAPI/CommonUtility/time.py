import datetime
import typing
import pytz
from dateutil.relativedelta import relativedelta
import datetime
import typing

import pytz
from dateutil.relativedelta import relativedelta


def move_date_str(date_str, days=0, hours=0, output_format='%Y-%m-%d', input_format='%Y-%m-%d', months=0):
    """
    date_str = '2019-01-01'
    :param date_str:
    :param hours:
    :param days = -1
    :param output_format:
    :param input_format:
    :return:
    """
    return (datetime.datetime.strptime(date_str, input_format) + relativedelta(months=months) + relativedelta(days=days) + relativedelta(
        hours=hours)).strftime(output_format)



def get_today_us_eastern(tz='US/Eastern', format_: typing.Optional[str] = '%Y-%m-%d'):
    dt = datetime.datetime.now(pytz.timezone(tz))
    if format_ is None:
        return dt
    else:
        return dt.strftime(format_)
