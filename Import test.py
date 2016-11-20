import time, re

time_re = re.compile('(24:00|2[0-3]:[0-5][0-9]|[0-1][0-9]:[0-5][0-9])')

def daily(startTime):

    if startTime == time_re:
        print ('startTime')
    else:
        print ('still not bloody working')

time_re = re.compile(r'^(([01]\d|2[0-3]):([0-5]\d)|24:00)$')
def is_time_format(s):
    print (bool(time_re.match(s)))


is_time_format('09:00')
daily('09:00')
