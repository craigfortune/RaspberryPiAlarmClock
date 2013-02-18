from time import *
from threading import Timer
import ObserverPattern

# AlarmData holds information about
class AlarmData(ObserverPattern.ObsSubject):

    daysOfTheWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    alarmSounding = False

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

        # Some sanity
        self.hour = hour % 24
        self.minute = minute % 60
        self.second = second % 60

        self.displayAlarmTime()


    def displayAllAlarmDays(self):
        print('Printing all alarm days...')

        for x in range(0, len(self.daysOfTheWeek)):
            print(self.daysOfTheWeek[x], ':', self.activeDays[self.daysOfTheWeek[x]])
        
    def displayActiveAlarmDays(self):
        print('Printing active alarm days...')

        for x in range(0, len(self.daysOfTheWeek)):
            if(self.activeDays[self.daysOfTheWeek[x]]):
                print(self.daysOfTheWeek[x])

    def isDayActive(self, day):
        return self.activeDays[day]

    def setActiveDay(self, day):
        if(self.daysOfTheWeek.index(day) >= 0):
            self.activeDays[day] = True
            self.displayAlarmTime()
            return True
        else:
            return False

    def setInactiveDay(self, day):
        if(self.daysOfTheWeek.index(day) >= 0):
            self.activeDays[day] = False
        else:
            return False

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

    def update(self):
        hour, minute, second = self.hms()

        if(self.isDayActive(self.daysOfTheWeek[localtime().__getattribute__('tm_wday')])):
            if(self.hour == hour):
                if(self.minute == minute):
                    if(self.second == second):
                        self.startAlarm()
                    return

    def startAlarm(self):
        if not(self.alarmSounding):
            hour, minute, second = self.hms()
            print('ALARM SOUNDING', hour, minute, second)

            self.alarmSounding = True
            self.notify()

            t = Timer(5.0, self.resetAlarm).start()

    def resetAlarm(self):
        hour, minute, second = self.hms()
        print('RESET TRIGGER', hour, minute, second)

        self.alarmSounding = False
        self.notify()

    # utility, simply saves some typing
    def hms(self):
        hour = localtime().__getattribute__('tm_hour')
        minute = localtime().__getattribute__('tm_min')
        second = localtime().__getattribute__('tm_sec')

        return hour, minute, second
