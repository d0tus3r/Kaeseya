#!/usr/bin/env python3

import argparse
import logging
import requests
import json

API_URL = 'http://bms.kaseya.com/api/'
AUTH = {
       'grant_type=password'
       'username='
       'password='
       'tenant='
        }

def main():

    #auth_reponse = requests.post('{0}token'.format(API_URL),
    #    data=AUTH)

   # bearer = { 'Authorization': auth_response.json() }

    #Read locations from file
    with open('ocean_blue.json') as json_data:
        AccountLocations = json.load(json_data)
        print(json.dumps(AccountLocations, sort_keys=True, indent=4))

        #Post Locations
       #location_response = requests.post('{0}import/AccountLocations'.format(API_URL),
       #     json=AccountLocations,headers=bearer)
    

if __name__ ==  "__main__":
    main()
# vim: tabstop=4 softtabstop=4 shiftwidth=4 noexpandtab
