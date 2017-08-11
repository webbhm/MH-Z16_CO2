# MH-Z16_CO2
Python code for the Sandbox Electronics CO2 sensor
This code is for integrating the MH-Z16 sensor and I2C interface board (IC SC16I5705) with the OpenAg MVP.

Instructions:
This code requires time and smbus, which should already be in the library.
Copy the NDIR.py file to your python directory
Modify logSensors.py by adding the following code:
> import NDIR
```
try:
    sensor=NDIR.Sensor(0x4D)
    sensor.begin()
    logData("CO2 Concentration", "Success", "co2", str(sensor.getCO2()), '')
 exception (IOError):
    logData("CO2 Concentration", "Failure", "co2", str(IOError))
```
