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

    bearer = {'Authorization': auth_response.json()}

    print(bearer)


if __name__ == "__main__":
    main()
