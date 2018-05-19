#!/usr/bin/env python3
'''set env path'''
import sys
import json
import requests
from config import CONFIG

#pull creds from ~/.bms.ini
USERNAME = CONFIG.get('BMS', 'USERNAME')
PASSWORD = CONFIG.get('BMS', 'PASSWORD')
GRANT_TYPE = CONFIG.get('BMS', 'GRANT_TYPE')
TENANT = CONFIG.get('BMS', 'TENANT')
API_URL = CONFIG.get('BMS', 'API_URL')
LOCATION_URL = CONFIG.get('BMS', 'LOCATION_URL')
#pass json file when running script, save that parameter to FILE_NAME
FILE_NAME = sys.argv[1]
#for initial login
HEADERS = {
    'content-type': 'application/x-www-form-urlencoded',
    'accept': 'application/json'
}
#paremters for access_token gen
PARAMETERS = {
    'grant_type': GRANT_TYPE,
    'username': USERNAME,
    'password': PASSWORD,
    'tenant': TENANT
}


def main():
    '''Logs into BMS by Kaseya and adds locations (stored as json) to an account'''
    #post header + parameter to receive json data with bearer access_token
    auth_response = requests.post(API_URL, headers=HEADERS, data=PARAMETERS)

    #parse response and pull access token for future posts
    bearer = auth_response.json()
    token = bearer['access_token']

    #Read locations from file
    with open(FILE_NAME) as json_data:
        account_locations = json.load(json_data)
        print(json.dumps(account_locations, sort_keys=True, indent=4))
        #header for posting account locations
        location_header = {
            'accept': 'application/json',
            'content-type': 'application/json',
            'authorization': 'Bearer {0}'.format(token)
        }
       #Post Locations
        location_response = requests.post(LOCATION_URL, json=account_locations,\
			 headers=location_header)

        print(location_response)


if __name__ == "__main__":
    main()
