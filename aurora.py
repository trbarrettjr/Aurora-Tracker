#!/usr/bin/python3
import http.client
import json

server = {
    'server': 'services.swpc.noaa.gov', 
    'directory': '/json/ovation_aurora_latest.json'
    }

request_headers = {
    "user-agent": "Aurorafinder/1.0",
    "accept": "applicaiton/json", # Not required, but if they collect server data it will tell them what we are looking for.
    }

myLocation = {
    "latitude": 0.000, 
    "longitude": 0.000
    }

def main():
    # Completing the HTTP Request to get the latest JSON file for aurora prediction from Ovation
    h1 = http.client.HTTPSConnection(server['server'])
    h1.request('GET', server["directory"], headers=request_headers)
    resp = h1.getresponse()
    if resp.status in range(200, 299):
        data = json.load(resp) # Load the JSON as data variable
    else:
        print(f"Something is wrong: {resp.status}  {resp.reason}")

    # According to the Data Format in the JSON file, the data format is [Longitude, Latitude, Aurora]
    # Therefore, we will need to format where the Longitude is searched first, then latitude
    # An issue with longitude it is numbered {0..359} therefore will need to research to figure out how to handle
    # West coordinates or negative coordinates.

    # the data['coordinates'][0][2] is the aurora Kp index
    # See https://www.swpc.noaa.gov/content/space-weather-glossary#k then "Kp index"

    # Data is in full integers, floats will not work

    if myLocation["longitude"] < 0:
        myLocation["longitude"] = int(myLocation["longitude"] + 360)

    # Latitude is {-90..90} this appears to be a true North-south coordinates





if __name__ == "__main__":
    main()