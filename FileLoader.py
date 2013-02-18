from time import *
import AlarmData
import AlarmSounder

class FileLoader:
    def __init__(self):
        pass

    # temporary data to test with
    def tempData(self, tmpList):
        time = localtime()
        hour = time.__getattribute__('tm_hour')
        minute = time.__getattribute__('tm_min')
        second = time.__getattribute__('tm_sec')

        # 15 seconds on from now
        alarmData = AlarmData.AlarmData(hour, minute, second + 15)

        # Set the delegate object for dealing with making noise on
        # the alarmData object we've just created
        # Different objects can make different noises
        alarmSounder = AlarmSounder.AlarmSounder()
        alarmData.attach(alarmSounder)
        alarmSounder.alarmDataObject = alarmData

        # Place it into the alarmDataList
        self.insertAlarmData(tmpList, alarmData)

    # If we create an AlarmData object, then we want to insert
    # it into our list for updating etc
    def insertAlarmData(self, tmpList, alarmData):
        tmpList.insert(0, alarmData)

    # The main delegation method
    # You can do whatever you want with this. Here we are just loading
    # up some default data for testing with
    # You simply need to return the initialised tmpList
    def initialiseAlarmDataList(self, tmpList):
        return self.tempData(tmpList)