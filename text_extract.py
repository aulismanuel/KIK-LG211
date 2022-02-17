print("Hello world! (Edit: I chose to leave this here because it's cute and this is my")
print("first work ever like this (more than 10 lines of code))")
print("")
print("I left a few trials and errors visible.")
print("On the bottom you will find a real-time table of next departures from Töölöntori")
print("tram stop to northeast. I didn't quite use HTML or any reg-ex but in the end I")
print("think this was far more challenging, so I hope it's OK! :)")
print("")
print("So, what I did, was that I studied HSL/Digitransit GraphQL API documentation")
print("(not familiar with it or any GraphQL API before this) and after days of trial")
print("and error I managed to pull some data and show it in an understandable form.")
print("")
import nltk
import urllib
from urllib import request
from nltk.tokenize import word_tokenize
import bs4
from bs4 import BeautifulSoup
import requests
import json
import pandas as pd
import math
url = "https://api.digitransit.fi/routing/v1/routers/hsl/index/graphql"
query = """query {
    stop(id: "HSL:1140447") {
        name
        stoptimesWithoutPatterns {
            serviceDay
            scheduledDeparture
            realtimeDeparture
            trip {
                routeShortName
            }
            headsign
        }
    }  
} """
Headers = { "Content-Type": "application/json" }
req = requests.post(url, json={'query': query}, headers=Headers)
#print(req.status_code)
if (req.status_code == 200):
    print("Succesfully connected to Digitransit API! (Status code 200)")
elif (req.status_code == 404):
    print("Couldn't reach Digitransit API. (Status code 404)")
else:
    print("No response from Digitransit API. (Status code other than 200 or 404)")
ndep = req.json()
print("")
print("Next departures from Töölöntori:")
for dep in ndep['data']['stop']['stoptimesWithoutPatterns']:
    print(dep)
print("")
print("Now trying to extract the time:")
for dep in ndep['data']['stop']['stoptimesWithoutPatterns']:
    print(
        "Scheduled: " +
        str(dep['serviceDay'] + dep['scheduledDeparture']) +
        "Actual: " +
        str(dep['serviceDay'] + dep['realtimeDeparture'])
    )
print("")
print("Okay, it seems that the times are seconds from midnight. Now trying to extract them.")
print("")
def showTime(secondsFromMidnight):
    sec = secondsFromMidnight
    ss = str(sec % 60)
    if (len(ss) == 1):
        ss = str(0) + ss
    min = math.floor(sec / 60)
    mm = str(min % 60)
    if (len(mm) == 1):
        mm = str(0) + mm
    hh = str(math.floor(min / 60))
    if (len(hh) == 1):
        hh = str(0) + hh
    return hh + ":" + mm + ":" + ss
print("")
print("A'ight, let's see how this works.")
print("")
print("|-------------------------------------------------------------|")
print("| NEXT DEPARTURES FROM TÖÖLÖNTORI:                            |")
print("|-------------------------------------------------------------|")
print("| Scheduled: | Actual:   | Route:  | Destination:             |")
print("|------------|-----------|---------|--------------------------|")
for dep in ndep['data']['stop']['stoptimesWithoutPatterns']:
    print(
        "| " +
        showTime(dep['scheduledDeparture']) + "   | " +
        showTime(dep['realtimeDeparture']) + "  | " +
        "Tram " + dep['trip']['routeShortName'] + "  | " +
        dep['headsign']
    )
print("|-------------------------------------------------------------|")
