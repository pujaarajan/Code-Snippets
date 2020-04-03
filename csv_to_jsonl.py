import csv
import json

in_filename = 'in_filename.csv' #replace this
out_filename = 'out_filename.jsonl' #replace this

with open(in_filename, 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    with open(out_filename, 'w') as json_file:
        rows = list(reader)
        for r in rows:
            json_file.write(json.dumps(r)+'\n')
