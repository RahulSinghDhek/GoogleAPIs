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
    parser = argparse.ArgumentParser( description="Test User Quota Rest APIs" )
    parser.add_argument("--serviceUser", "-su", required=False, nargs=1, help="user Account")
    parser.add_argument("--passwd", "-p", required=False, nargs=1, help="Access account password ")
    args = parser.parse_args()

    Vector={}
    Vector['serviceUser']=args.serviceUser
    Vector['passwd']=args.passwd
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
    apiKey = "Your Google API key"
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
    sendAlert("Traffic Alert", "With the current traffic it will take "+ trafficTime + " to reach Home from Office")
    
if __name__ == '__main__':
   main()

