import Utils
from Mode01.BaseClasses.OBDResponse import OBDResponse

class FuelType(OBDResponse):

    def getvalue(self):
        value = int(self.byteA, 16)
        if value==0:
            return 'N/A'
        elif value==1:
            return 'Gasoline'
        elif value==2:
            return 'Methanol'
        elif value==3:
            return 'Ethanol'
        elif value==4:
            return 'Diesel'
        elif value==5:
            return 'LPG'
        elif value==6:
            return 'CNG'
        elif value==7:
            return 'Propane'
        elif value==8:
            return 'Electric'
        elif value==9:
            return 'Bifuel running Gasoline'
        elif value==10:
            return 'Bifuel running Methanol'
        elif value==11:
            return 'Bifueld running Ethanol'
        elif value==12:
            return 'Bifuel running LPG'
        elif value==13:
            return 'Bifuel running CNG'
        elif value==14:
            return 'Bifuel running Propane'
        elif value==15:
            return 'Bifuel running Electricity'
        elif value==16:
            return 'Bifuel running Electric and Combustion'
        elif value==17:
            return 'Hybrid Gasoline'
        elif value==18:
            return 'Hybrid Ethanol'
        elif value==19:
            return 'Hybrid Diesel'
        elif value==20:
            return 'Hybrid Electric'
        elif value==21:
            return 'Hybrid running Electric and Combustion'
        elif value==22:
            return 'Hybrid Regenerative'
        elif value==23:
            return 'Bifuel running Diesel'
        else:
            return None

    def responsecode(self):
        return '41 51'

    def __init__(self):
        self.byteA = Utils.getrandhex()
