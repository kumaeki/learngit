# -*- coding:utf-8 -*-

import re
from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str, tz_str):
    dt = datetime.strptime(dt_str,"%Y-%m-%d %H:%M:%S")
    r = re.match(r"UTC(\+?\-?\d{1,2})\:\d*",tz_str)
    if r:
        tz = int(r.group(1))
    else:
        tz = 0
    return dt.replace(tzinfo=timezone(timedelta(hours=tz))).timestamp()


# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')