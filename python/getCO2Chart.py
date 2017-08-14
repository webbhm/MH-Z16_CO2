# Author: Howard Webb
# Data: 7/25/2017

import pygal
import requests
import json

def getDepthChart():
        "Create chart of water level"
        #Query the database for data
        #Order descending so the last rows are first
        #These modifiers get humidity and return only 60 rows
        r = requests.get('http://127.0.0.1:5984/mvp_sensor_data/_design/doc/_view/attribute_value?startkey=["co2",{}]&endkey=["co2"]&descending=true&limit=120')
#        print(r)
        #Iterate over the rows and xtract the values and timestamp into Python lists
        v_lst = [float(x['value']['value']) for x in r.json()['rows']]
        ts_lst = [x['value']['timestamp'] for x in r.json()['rows']]

#        print(v_lst)
        #Build the chart from the lists
        line_chart = pygal.Line(range=(200, 1500))
        line_chart.title = 'CO2'
        line_chart.y_title="ppm"
        line_chart.x_title="Timestamp (hover over to display)"
        # reverse order for proper time sequence
        ts_lst.reverse()
        line_chart.x_labels = ts_lst

        #revrese order for proper time sequence
        v_lst.reverse()
        line_chart.add('ppm', v_lst)

        #Save the chart as SVG to the web directory
        line_chart.render_to_file('/home/pi/MVP/web/co2_chart.svg')

getDepthChart()

