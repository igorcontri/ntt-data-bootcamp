# pip install pytz (biblioteca de terceiros)

import datetime
import pytz

d = datetime.datetime.now(pytz.timezone("America/Sao_Paulo"))
print(d)