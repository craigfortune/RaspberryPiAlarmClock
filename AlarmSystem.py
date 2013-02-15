from time import *

import AlarmData
import FileLoader

# The AlarmSystem class holds a collection of
# alarmData objects and updates them in a loop
class AlarmSystem:

    def __init__(self):
        self.alarmDataList = list()
        self.loadingDelegate = FileLoader.FileLoader()

    # Update each AlarmData object we hold
    def update(self):
        for item in self.alarmDataList:
            item.update()

    # Called to set things running
    def start(self):
        self.loadData()

    # Load data from a file
    def loadData(self):
        if not(self.loadingDelegate):
            print('No loadingDelegate set')
            return
        func = getattr(self.loadingDelegate, 'initialiseAlarmDataList')
        if(func):
            self.loadingDelegate.initialiseAlarmDataList(self.alarmDataList)
        else:
            print('No \'initialiseAlarmDataList\' method on delegate object')