# MH-Z16_CO2
Python code for the Sandbox Electronics CO2 sensor
This code is for integrating the MH-Z16 sensor and I2C interface board (IC SC16I5705) with the OpenAg MVP.

Instructions:
This code requires time and smbus, which should already be in the python library.
Copy the python files to your python directory.
  - NDIR.py
  - getCO2Chart.py
For ver 1.0 the python directory is `/home/pi/Documents/OpenAg-MVP/python`
For later versions, the directory is `/home/pi/MVP/python`
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
To get the data into the UI charts requires modifying the render.sh script, and the index.html.
In version 1.0 the script will be in /home/pi/MVP_UI/scripts/
For later versions it will be in /home/pi/MVP/scripts

index.html, for version 1.0 is in /home/pi/Documents/OpenAg-MVP/web
for later versions, it is in /home/pi/MVP/web
python "
The render script collects the data and runs the code to build the charts.  In this case it will be the co2_chart.svg.
If not already at the top of the script file, add (for ver 1.0):

> python_dir="/home/pi/Directory/OpenAg-MVP/python/

Then at the bottom of the file add:

>python "$python_dir"getCO2Chart.py

To the index.html, make the following modification:
Under the <div class="tab">, add a line like the others, but with the CO2 information.  NOTE: the sequence of these lines determines the order of the tabs.  This line creates a button that invokes the java script to display the the appropriate html.
> <button class="tablinks" onclick="openTab(event, 'CO2')">CO2</button>
The following is the html that will be displayed, copy it anywhere with the other tab division code:
```
<div id="CO2" class="tabcontent">
    <h3>CO2 Concentration</h3>
    <p>Reading of the CO2 sensor</p>
      <object type="image/svg-xml" data="co2_chart.svg"/>
        "Your browser does not support SVG
      </object>
</div>
```

### Testing
To test the sensor and code, double click on the NDIR.py file to open in in the python IDE.  Then run it by clicking on "Run"/"Run Module".  You will not see any return information, but just a prompt.  At the prompt, type in the following:
```
s=Sensor()
s.test()
```
You shuold see several lines of CO2 readings.
Work your way up the stack by then running from the command line:
  - python getCO2Chart.py
  - bash render.sh
  - double click on index.html to display it in a browser view the chart
