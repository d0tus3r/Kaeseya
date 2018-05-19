# bms_scripts
collection of python scripts for automating tasks in kaseya's BMS system

We recently started using BMS by Kaseya for our CRM. While migrating to this new CRM we realized that we couldn't easily merge locations from our previous ticket system. We are a Wireless ISP and service bulk hoa contracts for WiFi and as such one 'account' will have 100s of sub 'locations.' Unfortunately Kaseya doesn't allow a web gui based way to import locations so we created a script to handle the task.


This script pulls login credentials from an INI file located in ~/ and follows the general format of:

[BMS]

USERNAME = bms_username

PASSWORD = bms_pass

TENANT = company_name

GRANT_TYPE = password

API_URL = api_url

LOCATION_URL = kaseya account api/import/AccountLocations



You'll need to pass a json file with the account locations you wish to add:



[

  {
  
    "AccountName": "Account Name",
    
    "LocationName": "Unit #",
    
    "isMain": "false"
    
  },
  
  {
  
    "AccountName": "Account Name",
    
    "LocationName": "Unit #",
    
    "isMain": "false"
    
  }
  
]


Call the script (depending on env)

$python3 bms_locations.py jsonfilename.json
