#!/usr/bin/env python3
import requests
import json
import argparse
import logging
from config import CONFIG

#pull creds from ~/.bms.ini
USERNAME = CONFIG.get('BMS', 'USERNAME')
PASSWORD = CONFIG.get('BMS', 'PASSWORD')
GRANT_TYPE = CONFIG.get('BMS', 'GRANT_TYPE')
TENANT = CONFIG.get('BMS', 'TENANT')
API_URL = CONFIG.get('BMS', 'API_URL')
LOCATION_URL = CONFIG.get('BMS', 'LOCATION_URL')
#for initial login
HEADERS = {
    'content-type': 'application/x-www-form-urlencoded',
    'accept': 'application/json'
}

PARAMETERS = {
    'grant_type': GRANT_TYPE,
    'username': USERNAME,
    'password': PASSWORD,
    'tenant': TENANT
}


def main():
    '''Logs into BMS by Kaseya and adds locations (stored as json) to an account'''
    auth_response = requests.post(API_URL, headers=HEADERS, data=PARAMETERS)

    bearer = auth_response.json()
    token = bearer['access_token']
    #print(token)


    #Read locations from file
    with open('forest_dunes.json') as json_data:
        AccountLocations = json.load(json_data)
        print(json.dumps(AccountLocations, sort_keys=True, indent=4))

        location_header = {
            'accept': 'application/json',
            'content-type': 'application/json',
            'authorization': token
        }
       #Post Locations
        location_response = requests.post(LOCATION_URL, json=AccountLocations, headers=location_header)

        print(location_response)


if __name__ == "__main__":
    main()
