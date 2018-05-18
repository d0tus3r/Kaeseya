#!/usr/bin/env python3

import argparse
import logging
import requests

API_URL = http://bms.kaseya.com/api/
AUTH = {
       'grant_type=password'
       'username='
       'password='
       'tenant='
        }

def main:

    auth_reponse = requests.post('{0}token'.format(API_URL),
        data=AUTH)

    bearer = { 'Authorization': auth_response.json() }

    headers=bearer
    location_response = requests.post('{0}import/AccountLocations'.format(API_URL),
        json=AccountLocations)





if __name__ ==  "__main__":
    main()
# vim: tabstop=4 softtabstop=4 shiftwidth=4 noexpandtab
