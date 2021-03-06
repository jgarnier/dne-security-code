# SOLUTION SECTION #4 GET REQUEST LAB 3-HandsOn-Enforcement-API-CustomBlockList

# import necessary libraries / modules
import requests
import json

# copy paste API key from previous section within the quotes
enforcement_api_key = "<insert-enforcement-api-key-here>"

# URL needed to do GET requests
domain_url = "https://s-platform.api.opendns.com/1.0/domains"

url_get = domain_url+'?customerKey='+enforcement_api_key

# create empty list to contain all domains already in Umbrella
domain_list = []

# keep doing GET requests, until looped through all domains
while True:
    req = requests.get(url_get)
    json_file = req.json()
    for row in json_file["data"]:
        domain_list.append(row["name"])
    # GET requests will only list 200 domains, if more than that, it will request next bulk of 200 domains
    if bool(json_file["meta"]["next"]):
        Url = json_file["meta"]["next"]
    # break out of loop when finished
    else:    
        break

# error handling if true then the request was HTTP 200, so successful 
if(req.status_code == 200):
  print("SUCCESS: the following domain(s) are in your current custom Block List:")
  print(domain_list)
else:
  print("An error has ocurred with the following code %(error)s, please consult the following link: https://enforcement-api.readme.io/" % {'error': req.status_code})