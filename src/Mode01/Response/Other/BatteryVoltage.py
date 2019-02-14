import Utils
from Mode01.BaseClasses.OBDResponse import OBDResponse
import random

class BatteryVoltage(OBDResponse):

    def getvalue(self):
        return int(self.byteA, 16)

    def responsecode(self):
        return ''

    def __init__(self):
        self.byteA = str((120 + random.randint(0,14))/10)+'V'


