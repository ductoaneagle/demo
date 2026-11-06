import datetime

#---------------Read the system time from pc----------
def ReadRtc():
    nows = datetime.datetime.now()
    dt = nows.strftime("%d:%m:%Y-%H:%M:%S") #str
    secs = nows.second #int
    return dt, secs