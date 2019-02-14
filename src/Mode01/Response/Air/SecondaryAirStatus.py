import random
from Mode01.BaseClasses.OBDResponse import OBDResponse

class SecondaryAirStatus(OBDResponse):

    validBytes = ['01', '02', '04', '08']

    def getvalue(self):
        val = self.byteA
        if val=='01':
            return 'Upstream'
        elif val=='02':
            return 'Downstream of catalytic converter'
        elif val=='04':
            return 'From the outside atmosphere or off'
        elif val=='08':
            return 'Pump commanded on for diagnostics'
        else:
            return None

    def responsecode(self):
        return '41 12'

    def __init__(self):
        self.byteA = random.choice(self.validBytes)
