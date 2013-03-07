import os
import sys
import AlarmData
import subprocess

class AlarmSounder:

    alarmDataObject = None

    def __init__(self):
        pass

    # Called if we are observing and a state change happens that
    # we want to know about
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

        if(sys.platform == 'darwin'):
            return_code = subprocess.call(["afplay", self.getTrack()])
        else:
            cmd = 'mpg321 ' + self.getTrack() + ' &'
            print('Cmd is: ' + cmd)
            os.system(cmd)

    # return the path for the mp3 track to play
    # TODO centralise the config file loading
    def getTrack(self):
        currDir = os.path.dirname(os.path.abspath(sys.argv[0]))
        mp3Track = 'song.mp3'

        if os.path.isfile('config.txt'):
            file = open('config.txt')
            keepReading = True
            while keepReading:
                line = file.readline()
                if not line:
                    print('no line')
                    break
                else:
                    splitLine = line.split()
                    if splitLine[0] == 'mp3Track':
                        mp3Track = splitLine[1]
                        print('Set mp3Track to ' + splitLine[1])
                        keepReading = False
        else:
            print('No config.txt')

        return currDir + '/' + mp3Track

    # Stop making the noise (ie, alarm stopped)
    def stopNoise(self, alarmDataObj):
        print('Stop noise')
        pass