# File: ex5.py         
# Date: 05/14/13
# Author: Simon Roses Femerling
# Desc: Check usernames on 160 social network sites               
#
# VULNEX (C) 2013
# www.vulnex.com

import requests
import json
import urllib
import const
import pprint

site="http://search.twitter.com/search.json?q="

# Your query here
query=""

url=site+urllib.quote(query)

print "Recolectando alias en Twitter: %s\n" % query
response = requests.get(url)

users = []

for res in response.json["results"]:
	if res.has_key('to_user'):
		if not res['to_user'] in users: users.append(str(res["to_user"]))
	if res.has_key('from_user'):
		if not res['from_user'] in users: users.append(str(res["from_user"]))

print "ALIAS-> %s" % users

print "\nComprobrando alias en 160 websites\n"
for username in users:	
	for service in const.services:  
      		try:    
			res1 = requests.get('http://checkusernames.com/usercheckv2.php?target=' + service + '&username=' + username, headers={'X-Requested-With': 'XMLHttpRequest'}).text
			if 'notavailable' in res1: 
				print ""
				print username + " -> " + service 
				print "" 
      		except Exception as e:  
           		print e 

# VULNEX EOF
