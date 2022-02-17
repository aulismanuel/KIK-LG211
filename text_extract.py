print("Hello world!")
import nltk
import urllib
from urllib import request
from nltk.tokenize import word_tokenize
import bs4
from bs4 import BeautifulSoup
import requests
import json
import pandas as pd
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
print("Okay, it seems that the times are seconds from midnight. Now trying to easily extract them.")
