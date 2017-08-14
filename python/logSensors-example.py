#Check sensors and log to file
from logData import logData
from si7021 import getHumidity, getTempC
import NDIR

try:
    humidity = getHumidity()
    logData("si7021", "Success", "humidity", "{:10.1f}".format(humidity), '')
except (IOError):
        logData("si7021", "Failure", "humidity", '', IOError)

try:
    temp = getTempC()
    logData("si7021", "Success", "temperature", "{:10.1f}".format(temp), '')
except (IOError, e):
        logData("si7021", "Failure", "temperature", '', str(e))

try:
    sensor = NDIR.Sensor(0x4D)
    sensor.begin()
    logData("CO2 Concentration", "Success", "co2", str(sensor.getCO2()), '')
except (IOError):
        logData("CO2 Concentration", "Failure", "co2", '', str(IOError))        

       
