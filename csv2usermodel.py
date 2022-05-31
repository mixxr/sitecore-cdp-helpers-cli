#!/usr/bin/python3
# author: Michelangelo Serpico

import csv
import json
import uuid
import sys
from time import time

def append_json(path, data):
    with open(path, 'a', encoding='utf-8-sig') as jsonp:
        json.dump(data, jsonp)
        jsonp.write("\n")

def make_json(csv_path, json_path):
    counter = 0
    with open(csv_path, encoding='utf-8-sig') as csvp:
        csv_reader = csv.DictReader(csvp) # returns a dictionary class

        for row in csv_reader:
            # TODO: make the following option via parameters like -i -s -e
            row["identifiers"] = []
            row["subscriptions"] = []
            row["extensions"] = []

            row_items = list(row.items())
            for k, v in row_items:
                ks = k.split(".")
                v = str(v).strip()
                if len(ks) > 1:  # identifiers.<POS>.id or street.<POS>
                    del row[k]
                    if len(ks) == 3: # identifiers.<POS>.id
                        i_pos = int(ks[1])
                        if not(ks[0] in row): row[ks[0]] = [] 
                        if len(row[ks[0]])<=i_pos: row[ks[0]].append({})
                        row[ks[0]][i_pos][ks[2]] = v
                    else: # street.<POS>
                        if not(ks[0] in row): row[ks[0]] = []
                        row[ks[0]].append(v)
            #data.append(row)
            record = {}
            record["ref"] = str(uuid.uuid4())
            print(f'generated UUID {record["ref"]}' )
            record["schema"] = "guest"
            record["mode"] = "upsert"
            record["value"] = row

            append_json(json_path, record)
            counter += 1
    return counter


csv_path = r'users.csv' if len(sys.argv)==1 else sys.argv[1]
json_path = "%s.json" % csv_path
print(f'reading {csv_path} -> {json_path}...')

start = time()

counter = make_json(csv_path, json_path)

print(f'Completed in {time() - start} seconds for {counter} records.')
