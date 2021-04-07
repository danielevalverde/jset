import requests
import os
from pprint import pprint
import time
import json
import csv
import random

# get data from source file
# text_file = open("source_new.txt", "r")
text_file = open("interval.txt", "r")
lines = text_file.read().splitlines()
# print (lines)
# print (len(lines))
text_file.close()

params = {
    "state": "open",
}
git_access_token = 'please, add your token'
headers = {'Authorization': f'token {git_access_token}'}

aux={}
#get project data
with open("Output.json", "r") as file:
    aux = json.load(file)
file.close()

# update file with new projects data
with open("Output.json", "w") as file:
    for x in range(len(lines)):
        query_url = f"https://api.github.com/repos/{lines[x]}"
        r = requests.get(query_url, headers=headers, params=params)
        pprint (r.status_code)
        if r.status_code != 200:
            print(r.content)
        else:
            print("celebrate!!!")
            aux.append(r.json())
        # trying not to take github block :)
        time.sleep(random.randint(30,180))
    json.dump(aux,file)
file.close()


