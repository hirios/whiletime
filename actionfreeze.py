import datetime
import math


class Actionfreeze():
    def __init__(self):
        self.hora = str(datetime.datetime.now())
        self.seconds = math.trunc(float(self.hora.split(":")[2]))


    def timefreeze(time):
        futuresec = Actionfreeze().seconds + time
        if futuresec > 60:
            futuresec = futuresec - 60
        return futuresec


def actualseconds():
    return Actionfreeze().seconds


def timefreeze(time):
    return Actionfreeze.timefreeze(time)