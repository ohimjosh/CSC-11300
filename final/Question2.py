#Question2

class SchedulerSPM():
    def __init__(self):
        return 0
    def configure(self):
        return 0

class AedesAegypti(SchedulerSPM):
    def __init__(self,lifeStage,energyLevel):
        self.lifeStage = lifeStage
        self.energyLevel = energyLevel

    def Birth(self):
        return 0

    def Metamorphosis(self):
        return 0

    def Death(self):
        return 0

    def FlyingRandomly(self):
        return 0

    def LookingForRestingPlace(self):
        return 0

    def LookForPlanet(self):
        return 0

    def Feeding(self):
        return 0

    def Mating(self):
        return  0

    def Ovipositting(self):
        return 0

class Mammal(SchedulerSPM):
    def __init__(self, traceintensity):
        self.traceintensity = traceintensity

    def MovingRandomly(self):
        return 0

    def UpdateTrace(self):
        return 0

class Vegetation(SchedulerSPM):
    def __init__(self, traceintensity):
        self.traceintensity = traceintensity

    def UpdateTrace(self):
        return 0

class Container(SchedulerSPM):
    def __init__(self, percentageLiquid, volatilityLiquid, percentageExposure, traceIntensity):
        self.percentageLiquid = percentageLiquid
        self.volatilityLiquid = volatilityLiquid
        self.percentageExposure = percentageExposure
        self.traceInensity = traceIntensity

    def updateVolume(self):
        return 0

    def UpdateTrace(self):
        return 0


class Meteorology(SchedulerSPM):
    def __init__(self, windDirection, windDirectionMaxSpeed, acummRainfall, accumSolarRadiation, globalSolarRadiation, airTemp, highAirTemp, lowAirTemp, airRelativeHumidity, windSpeed, highWindspeed):
        self.windDirection = windDirection
        self.windDirectionMaxSpeed = windDirectionMaxSpeed
        self.acummRainfall = acummRainfall
        self.accumSolarRadiation = accumSolarRadiation
        self.globalSolarRadiation = globalSolarRadiation
        self.airTemp = airTemp
        self.highAirTemp = highAirTemp
        self.lowAirTemp = lowAirTemp
        self.airRelativeHumidity = airRelativeHumidity
        self.windSpeed = windSpeed
        self.highWindspeed = highWindspeed

    def updateDate(self):
        return 0