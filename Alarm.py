from time import *
import AlarmSystem

alarmSystem = None

def main():
    global alarmSystem
    alarmSystem = AlarmSystem.AlarmSystem()
    alarmSystem.start()
    while True:
        alarmSystem.update()
        sleep(1)

if __name__ == '__main__':
    main()
