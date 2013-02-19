from time import *

#Simply saves some typing
def hms():
    hour = localtime().__getattribute__('tm_hour')
    minute = localtime().__getattribute__('tm_min')
    second = localtime().__getattribute__('tm_sec')

    return hour, minute, second

