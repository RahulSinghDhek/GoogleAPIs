#!/usr/bin/python
import argparse
import os
import urllib2
import requests
import json
import base64
import time
import pynotify


def sendAlert(title,message):
    pynotify.init("Test")
    notice = pynotify.Notification(title, message)
    notice.show()
    return
    
def CommandLineParser():
    parser = argparse.ArgumentParser( description="Test Google Map APIs" )
    parser.add_argument("--keyAPI", "-k", required=True, nargs=1, help="Enter your personal Google API key")
    args = parser.parse_args()

    Vector={}
    Vector['keyAPI']=args.keyAPI
    return Vector

def RequestDispatcher(URL,Method):
    response=''
    try:
      	response = requests.get(URL)
      	return response
    except urllib2.HTTPError, e:
       	raise ApiError('GET /tasks/ {}'.format(response.status_code))

def JSONdotRender(response):
    pass

def main():
    vectorCLI = CommandLineParser()
    apiKey = vectorCLI["keyAPI"][0]
    origin = "12.972489,77.7210000"
    destination = "12.9126915,77.6809359"
    departureTime =  time.time() + 10
    departureTime = int(departureTime)
    response=''  
    method = "GET"
    url = "https://maps.googleapis.com/maps/api/directions/json?origin="+origin+"&destination="+destination+"&departure_time="+str(departureTime)+"&key="+apiKey
    response=RequestDispatcher(url,method)
    
    #print  response.json()
    trafficTime =  response.json()["routes"][0]["legs"][0]["duration_in_traffic"]["text"]
    trafficTimeInt = int(trafficTime.split(" ")[0])
    if trafficTimeInt <= 45:
        sendAlert("Traffic Alert", "With the current traffic it will take "+ trafficTime + " to reach Home from Office")
    '''
    from pprint import pprint
    #with open(jsondata) as data_file:    
    #   data = json.load(data_file)
    #pprint(data)   
    with open('/tmp/projectData', 'w') as outfile:
       	json.dump(jsondata, outfile)
    for el in range(len(jsondata["project"])-1):
       	if jsondata["project"]:
            print jsondata["project"][el]["projectSite"][0]["siteName"]
            print jsondata["project"][el]["name"]
    print  response.read() 
'''

if __name__ == '__main__':
   main()

