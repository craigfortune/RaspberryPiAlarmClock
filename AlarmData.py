from time import *
from threading import Timer
import math
import ObserverPattern
import Utility

# AlarmData holds information about
class AlarmData(ObserverPattern.ObsSubject):

    daysOfTheWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    alarmSounding = False
    snoozeAllowed = 1
    snoozeTime = 300

    def __init__(self, hour, minute, second):

        super().__init__()

        print('Created AlarmData object')
            
        self.activeDays = {
            'Monday': True,
            'Tuesday': True,
            'Wednesday': True,
            'Thursday': True,
            'Friday': True,
            'Saturday': True,
            'Sunday': True
            }

        # Some sanity checks
        self.second = second % 60
        self.minute = minute % 60
        self.hour = hour % 24

        # More sanity checks
        self.second = math.floor(self.second)
        self.minute = math.floor(self.minute)
        self.hour = math.floor(self.hour)

        # and yet more sanity checks
        if second > 59:
            self.minute += 1
        if minute > 59:
            self.hour += 1
        if hour > 23:
            self.hour = 0


        self.displayAlarmTime()


    # Display the days an alarm CAN be set to be on
    def displayAllAlarmDays(self):
        print('Printing all alarm days...')

        for x in range(0, len(self.daysOfTheWeek)):
            print(self.daysOfTheWeek[x], ':', self.activeDays[self.daysOfTheWeek[x]])

    # Display the days this alarm IS set to be on
    def displayActiveAlarmDays(self):
        print('Printing active alarm days...')

        for x in range(0, len(self.daysOfTheWeek)):
            if(self.activeDays[self.daysOfTheWeek[x]]):
                print(self.daysOfTheWeek[x])

    # Check is a day is active. e.g. object.isDayActive('Monday')
    def isDayActive(self, day):
        return self.activeDays[day]

    # Make a day active. e.g. object.setActiveDay('Tuesday')
    def setActiveDay(self, day):
        if(self.daysOfTheWeek.index(day) >= 0):
            self.activeDays[day] = True
            self.displayAlarmTime()
            return True
        else:
            return False

    # Make a day inactive. e.g. object.setInactiveDay(Wednesday')
    def setInactiveDay(self, day):
        if(self.daysOfTheWeek.index(day) >= 0):
            self.activeDays[day] = False
        else:
            return False

    # Displays the time of the alarm and the days (in truncated form) it is active
    def displayAlarmTime(self):
        cumulativeDays = ''
        for x in range(0, len(self.daysOfTheWeek)):
            if(self.activeDays[self.daysOfTheWeek[x]]):
                if not (cumulativeDays == ''):
                    cumulativeDays = cumulativeDays + '/' + self.daysOfTheWeek[x][0:3]
                else:
                    cumulativeDays = self.daysOfTheWeek[x][0:3]

        if not (cumulativeDays == ''):
            print('Alarm set for:', self.hour, self.minute, self.second, 'on', cumulativeDays)
        else:
            print('Alarm set for:', self.hour, self.minute, self.second, 'on no days')

    # Update loop to check if the alarm time is satisfied
    def update(self):
        hour, minute, second = Utility.hms()

        if(self.isDayActive(self.daysOfTheWeek[localtime().__getattribute__('tm_wday')])):
            if(self.hour == hour):
                if(self.minute == minute):
                    if(self.second == second):
                        # Alarm ready to go!
                        self.startAlarm()
                    return

    # Alarm triggered
    def startAlarm(self):
        if not(self.alarmSounding):
            hour, minute, second = Utility.hms()
            print('ALARM SOUNDING', hour, minute, second)

            # Internal state to be sounding the alarm
            self.alarmSounding = True
            # Let any observers know we are sounding
            self.notify()

            # The reset time (i.e. when the alarm goes off by itself)
            t = Timer(5.0, self.resetAlarm).start()

    # Alarm turning off
    def resetAlarm(self):
        hour, minute, second = Utility.hms()
        print('RESET TRIGGER', hour, minute, second)

        # Update internal state and let observers know
        self.alarmSounding = False
        self.notify()