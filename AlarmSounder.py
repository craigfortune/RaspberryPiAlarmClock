import os
import sys
import AlarmData

class AlarmSounder:

    alarmDataObject = None

    def __init__(self):
        pass

    def updateNotification(self, object):
        if self.alarmDataObject == object:
            if self.alarmDataObject.alarmSounding == True:
                self.makeNoise(object)
            else:
                self.stopNoise(object)

    # Start making some noise (ie, alarm is sounding)
    def makeNoise(self, alarmDataObj):
        print(os.path.dirname(os.path.abspath(sys.argv[0])))
        # Using mpg321 to make a noise by calling it directly with an MP3 track
        currDir = os.path.dirname(os.path.abspath(sys.argv[0]))
        os.system('mpg321 ' + currDir + '/song.mp3 &')

    # Stop making the noise (ie, alarm stopped)
    def stopNoise(self, alarmDataObj):
        pass