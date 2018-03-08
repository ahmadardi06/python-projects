#!/usr/bin/python

import json, urllib

url = "https://api.github.com/users/ahmadardi06"
output = json.load(urllib.urlopen(url))

#print(output)
print "ID:", output['id']
print "Username: ", output['login']
print "Name: ", output['name']
print "Location: ", output['location']
