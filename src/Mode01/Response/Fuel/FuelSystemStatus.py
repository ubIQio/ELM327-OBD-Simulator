import random

from Mode01.BaseClasses.OBDResponse import OBDResponse


class FuelSystemStatus(OBDResponse):

    validBytes = ['01', '02', '04', '08', '10']

    def getvalue(self):
        return ['System1=' + self.determinestatus(self.byteA),
                'System2=' + self.determinestatus(self.byteB)]

    def determinestatus(self, byte):
        if byte=='01':
            return 'Open loop due to insufficient engine temperature'
        elif byte=='02':
            return 'Closed loop, using oxygen sensor feedback to determine fuel mix'
        elif byte=='04':
            return 'Open loop due to engine load OR fuel cut due to deceleration'
        elif byte=='08':
            return 'Open loop due to system failure'
        elif byte=='10':
            return 'Closed loop, using at least one oxygen sensor but there is a fault in the feedback system'
        else:
            return None

    def responsecode(self):
        return '41 03'

    def __init__(self):
        self.byteA = random.choice(self.validBytes)
        self.byteB = random.choice(self.validBytes)