from Mode01.Response.Other.AuxInputStatus import AuxInputStatus
from Mode01.Response.Other.BatteryVoltage import BatteryVoltage
from Mode01.Response.Load.CalculatedEngineLoad import CalculatedEngineLoad
from Mode01.Response.Load.AbsoluteLoadValue import AbsoluteLoadValue
from Mode01.Response.Catalyst.CatalystSensors import B2S2
from Mode01.Response.Catalyst.CatalystSensors import B1S2
from Mode01.Response.Catalyst.CatalystSensors import B2S1
from Mode01.Response.Catalyst.CatalystSensors import B1S1
from Mode01.Response.DTC_Info.DistTraveledSinceCodesCleared import DistTraveledSinceCodesCleared
from Mode01.Response.DTC_Info.DistanceWithMIL import DistanceWithMIL
from Mode01.Response.DTC_Info.FreezeDTC import FreezeDTC
from Mode01.Response.DTC_Info.MonitorStatus import MonitorStatus
from Mode01.Response.DTC_Info.MonitorStatusThisDriveCycle import MonitorStatusThisDriveCycle
from Mode01.Response.DTC_Info.NumWarmUpsSinceCodesCleared import NumWarmUpsSinceCodesCleared
from Mode01.Response.DTC_Info.RunTimeSinceEngineStart import RunTimeSinceEngineStart
from Mode01.Response.DTC_Info.TimeSinceCodesCleared import TimeSinceCodesCleared
from Mode01.Response.DTC_Info.TimeWithMILOn import TimeWithMILOn
from Mode01.Response.EGR.EGR import EGR
from Mode01.Response.EGR.EGRError import EGRError
from Mode01.Response.Other.EngineRPM import EngineRPM
from Mode01.Response.Evap.EvapPressureAbsolute import EvapPressureAbsolute
from Mode01.Response.Evap.EvapPurge import EvapPurge
from Mode01.Response.Evap.EvapSystemVaporPressure import EvapSystemVaporPressure
from Mode01.Response.Evap.EvapVaporPressure import EvapVaporPressure
from Mode01.Response.Fuel.EngineFuelRate import EngineFuelRate
from Mode01.Response.Fuel.EthanolFuelPercent import EthanolFuelPercent
from Mode01.Response.Fuel.FuelInjectionTiming import FuelInjectionTiming
from Mode01.Response.Fuel.FuelLevel import FuelLevel
from Mode01.Response.Fuel.FuelPressure import FuelPressure
from Mode01.Response.Fuel.FuelRailPressureAbsolute import FuelRailPressureAbsolute
from Mode01.Response.Fuel.FuelRailPressureDirect import FuelRailPressureDirect
from Mode01.Response.Fuel.FuelRailPressureRelative import FuelRailPressureRelative
from Mode01.Response.Fuel.FuelSystemStatus import FuelSystemStatus
from Mode01.Response.Fuel.FuelTrim.FuelTrims import LTFuelTrimB2
from Mode01.Response.Fuel.FuelTrim.FuelTrims import STFuelTrimB2
from Mode01.Response.Fuel.FuelTrim.FuelTrims import LTFuelTrimB1
from Mode01.Response.Fuel.FuelTrim.FuelTrims import STFuelTrimB1
from Mode01.Response.Fuel.FuelType import FuelType
from Mode01.Response.Other.HybridBatteryLifeRemaining import HybridBatteryLifeRemaining
from Mode01.Response.Air.MAFAirFlowRate import MAFAirFlowRate
from Mode01.Response.Air.IntakeManifoldPressure import IntakeManifoldPressure
from Mode01.Response.Air.BarometricPressure import BarometricPressure
from Mode01.Response.Air.MaxValueMAF import MaxValueMAF
from Mode04.ClearStoredDTCs import ClearStoredDTCs
from Mode01.Response.O2Sensors.AirFuelRatio import AirFuelRatio
from Mode01.Response.O2Sensors.Lambda.O2_Lambda import O2S8L
from Mode01.Response.O2Sensors.Lambda.O2_Lambda import O2S7L
from Mode01.Response.O2Sensors.Lambda.O2_Lambda import O2S6L
from Mode01.Response.O2Sensors.Lambda.O2_Lambda import O2S5L
from Mode01.Response.O2Sensors.Lambda.O2_Lambda import O2S4L
from Mode01.Response.O2Sensors.Lambda.O2_Lambda import O2S3L
from Mode01.Response.O2Sensors.Lambda.O2_Lambda import O2S2L
from Mode01.Response.O2Sensors.Lambda.O2_Lambda import O2S1L
from Mode01.Response.O2Sensors.NarrowBand.O2_Narrow import O2_B2S2n, O2_B2S4n, O2_B2S3n
from Mode01.Response.O2Sensors.NarrowBand.O2_Narrow import O2_B2S1n
from Mode01.Response.O2Sensors.NarrowBand.O2_Narrow import O2_B1S4n
from Mode01.Response.O2Sensors.NarrowBand.O2_Narrow import O2_B1S3n
from Mode01.Response.O2Sensors.NarrowBand.O2_Narrow import O2_B1S2n
from Mode01.Response.O2Sensors.NarrowBand.O2_Narrow import O2_B1S1n
from Mode01.Response.O2Sensors.O2SensorsPresent import O2SensorsPresent
from Mode01.Response.O2Sensors.OxygenSensorsPresent import OxygenSensorsPresent
from Mode01.Response.O2Sensors.Secondary.O2_Secondary import LTB2B4
from Mode01.Response.O2Sensors.Secondary.O2_Secondary import STB2B4
from Mode01.Response.O2Sensors.Secondary.O2_Secondary import LTB1B3
from Mode01.Response.O2Sensors.Secondary.O2_Secondary import STB1B3
from Mode01.Response.O2Sensors.WideBand.O2_Wide import O2S8w
from Mode01.Response.O2Sensors.WideBand.O2_Wide import O2S7w
from Mode01.Response.O2Sensors.WideBand.O2_Wide import O2S6w
from Mode01.Response.O2Sensors.WideBand.O2_Wide import O2S5w
from Mode01.Response.O2Sensors.WideBand.O2_Wide import O2S4w
from Mode01.Response.O2Sensors.WideBand.O2_Wide import O2S3w
from Mode01.Response.O2Sensors.WideBand.O2_Wide import O2S2w
from Mode01.Response.O2Sensors.WideBand.O2_Wide import O2S1w
from Mode01.Response.Error.OBDError import OBDError
from Mode01.Response.OBD_Info.OBDStandards import OBDStandards
from Mode01.Response.OBD_Info.ControlModuleVoltage import ControlModuleVoltage
from Mode01.Response.OBD_Info.MaxValues import MaxValues
from Mode01.Response.PIDs_Supported.PIDs import PIDsSupported1, PIDsSupported21, PIDsSupported41, PIDsSupported61
from Mode01.Response.Protocol.OBDProtocol import OBDProtocol
from Mode01.Response.Air.SecondaryAirStatus import SecondaryAirStatus
from Mode01.Response.Temperature.Temperatures import CoolantTemp, IntakeAirTemp, AmbientAirTemp, EngineOilTemp
from Mode01.Response.Throttle.ThrottlePositions import ThrottlePositionA, ThrottleActuator, AcceleratorPositionF, AcceleratorPositionE, \
    AcceleratorPositionD, ThrottlePositionC, ThrottlePositionB, ThrottlePositionRelative, AcceleratorPositionRelative
from Mode01.Response.Other.TimingAdvance import TimingAdvance
from Mode01.Response.OBD_Info.VehicleEmissionsRequirements import VehicleEmissionsRequirements
from Mode01.Response.Other.VehicleSpeed import VehicleSpeed


def readinputbytes(query):
    """Accepts a byte query (as a string), identifies the type of query,
    and returns an appropriate response (a subclass of OBDResponse)"""
    if isinstance(query, str):
        pass
    else:
        try:
            query = hex(query)[2:].rjust(2, '0').upper()
        except:
            return OBDError()

    mode = query[:2]

    if mode=='01':
        return getmode01response(query)
    elif mode=='02':
        return getmode02response(query)
    elif mode=='03':
        return getmode03response(query)
    elif mode=='04':
        return getmode04response(query)
    elif mode=='AT':
        return getmodeATresponse(query)
    else:
        return OBDError()

def getmode01response(query):
    pid = query[2:4]
    if pid=='00':
        return PIDsSupported1()
    elif pid=='01':
        return MonitorStatus()
    elif pid=='02':
        return FreezeDTC()
    elif pid=='03':
        return FuelSystemStatus()
    elif pid=='04':
        return CalculatedEngineLoad()
    elif pid=='05':
        return CoolantTemp()
    elif pid=='06':
        return STFuelTrimB1()
    elif pid=='07':
        return LTFuelTrimB1()
    elif pid=='08':
        return STFuelTrimB2()
    elif pid=='09':
        return LTFuelTrimB2()
    elif pid=='0A':
        return FuelPressure()
    elif pid=='0B':
        return IntakeManifoldPressure()
    elif pid=='0C':
        return EngineRPM()
    elif pid=='0D':
        return VehicleSpeed()
    elif pid=='0E':
        return TimingAdvance()
    elif pid=='0F':
        return IntakeAirTemp()
    elif pid=='10':
        return MAFAirFlowRate()
    elif pid=='11':
        return ThrottlePositionA()
    elif pid=='12':
        return SecondaryAirStatus()
    elif pid=='13':
        return OxygenSensorsPresent()
    elif pid=='14':
        return O2_B1S1n()
    elif pid=='15':
        return O2_B1S2n()
    elif pid=='16':
        return O2_B1S3n()
    elif pid=='17':
        return O2_B1S4n()
    elif pid=='18':
        return O2_B2S1n()
    elif pid=='19':
        return O2_B2S2n()
    elif pid=='1A':
        return O2_B2S3n()
    elif pid=='1B':
        return O2_B2S4n()
    elif pid=='1C':
        return OBDStandards()
    elif pid=='1D':
        return O2SensorsPresent()
    elif pid=='1E':
        return AuxInputStatus()
    elif pid=='1F':
        return RunTimeSinceEngineStart()
    elif pid=='20':
        return PIDsSupported21()
    elif pid=='21':
        return DistanceWithMIL()
    elif pid=='22':
        return FuelRailPressureRelative()
    elif pid=='23':
        return FuelRailPressureDirect()
    elif pid=='24':
        return O2S1w()
    elif pid=='25':
        return O2S2w()
    elif pid=='26':
        return O2S3w()
    elif pid=='27':
        return O2S4w()
    elif pid=='28':
        return O2S5w()
    elif pid=='29':
        return O2S6w()
    elif pid=='2A':
        return O2S7w()
    elif pid=='2B':
        return O2S8w()
    elif pid=='2C':
        return EGR()
    elif pid=='2D':
        return EGRError()
    elif pid=='2E':
        return EvapPurge()
    elif pid=='2F':
        return FuelLevel()
    elif pid=='30':
        return NumWarmUpsSinceCodesCleared()
    elif pid=='31':
        return DistTraveledSinceCodesCleared()
    elif pid=='32':
        return EvapVaporPressure()
    elif pid=='33':
        return BarometricPressure()
    elif pid=='34':
        return O2S1L()
    elif pid=='35':
        return O2S2L()
    elif pid=='36':
        return O2S3L()
    elif pid=='37':
        return O2S4L()
    elif pid=='38':
        return O2S5L()
    elif pid=='39':
        return O2S6L()
    elif pid=='3A':
        return O2S7L()
    elif pid=='3B':
        return O2S8L()
    elif pid=='3C':
        return B1S1()
    elif pid=='3D':
        return B2S1()
    elif pid=='3E':
        return B1S2()
    elif pid=='3F':
        return B2S2()
    elif pid=='40':
        return PIDsSupported41()
    elif pid=='41':
        return MonitorStatusThisDriveCycle()
    elif pid=='42':
        return ControlModuleVoltage()
    elif pid=='43':
        return AbsoluteLoadValue()
    elif pid=='44':
        return AirFuelRatio()
    elif pid=='45':
        return ThrottlePositionRelative()
    elif pid=='46':
        return AmbientAirTemp()
    elif pid=='47':
        return ThrottlePositionB()
    elif pid=='48':
        return ThrottlePositionC()
    elif pid=='49':
        return AcceleratorPositionD()
    elif pid=='4A':
        return AcceleratorPositionE()
    elif pid=='4B':
        return AcceleratorPositionF()
    elif pid=='4C':
        return ThrottleActuator()
    elif pid=='4D':
        return TimeWithMILOn()
    elif pid=='4E':
        return TimeSinceCodesCleared()
    elif pid=='4F':
        return MaxValues()
    elif pid=='50':
        return MaxValueMAF()
    elif pid=='51':
        return FuelType()
    elif pid=='52':
        return EthanolFuelPercent()
    elif pid=='53':
        return EvapPressureAbsolute()
    elif pid=='54':
        return EvapSystemVaporPressure()
    elif pid=='55':
        return STB1B3()
    elif pid=='56':
        return LTB1B3()
    elif pid=='57':
        return STB2B4()
    elif pid=='58':
        return LTB2B4()
    elif pid=='59':
        return FuelRailPressureAbsolute()
    elif pid=='5A':
        return AcceleratorPositionRelative()
    elif pid=='5B':
        return HybridBatteryLifeRemaining()
    elif pid=='5C':
        return EngineOilTemp()
    elif pid=='5D':
        return FuelInjectionTiming()
    elif pid=='5E':
        return EngineFuelRate()
    elif pid=='5F':
        return VehicleEmissionsRequirements()
    elif pid=='60':
        return PIDsSupported61()
    else:
        return OBDError()

def getmode02response(query):
    return OBDError()

def getmode03response(query):
    return OBDError()

def getmode04response(query):
    return ClearStoredDTCs()

def getmodeATresponse(query):
    pid = query[2:]
    if pid=='DP':
        return OBDProtocol()
    elif pid=='RV':
        return BatteryVoltage()
    else:
        return OBDError()
