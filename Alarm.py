from time import *
import AlarmSystem
import Chime

alarmSystem = AlarmSystem.AlarmSystem()
chimeSystem = Chime.Chime()

def main():
    alarmSystem.start()
    while True:
        alarmSystem.update()
        chimeSystem.update()
        sleep(1)

if __name__ == '__main__':
    main()
