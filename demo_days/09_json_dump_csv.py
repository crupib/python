#!/usr/local/bin/python3
import csv,json
print (json.dumps(list(csv.reader(open('username.csv')))))
