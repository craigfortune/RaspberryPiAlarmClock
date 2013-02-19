from time import *
import Utility

class Chime:
    def __init__(self):
        pass

    def update(self):
        hour, minute, second = Utility.hms()

        if(minute == 0):
            if(second == 0):
                print('Chime!')

        return