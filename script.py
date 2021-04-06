import requests
import os
from pprint import pprint
import subprocess
import time
import json
import csv

# text_file = open("source_new.txt", "r")
text_file = open("interval.txt", "r")
lines = text_file.readlines()
# print (lines)
# print (len(lines))

params = {
    "state": "open",
}
git_access_token = 'please, add your token'
headers = {'Authorization': f'token {git_access_token}'}
# # repoinfo="danielevalverde/jnose-tests"

with open("Output.json", "r+") as file:
    aux = json.load(file)
    for x in range(len(lines)):
        query_url = f"https://api.github.com/repos/{lines[x]}"
        r = requests.get(query_url, headers=headers, params=params)
        pprint (r.status_code)
        if r.status_code == 404:
            print(r.content)
        else:
            print("celebrate!!!")
            # pprint(lines[x])
            # pprint(r.json())
            # aux.update(r.json())
            aux.append(r.json())
            json.dump(aux,file)
        time.sleep(10)
    
text_file.close()


