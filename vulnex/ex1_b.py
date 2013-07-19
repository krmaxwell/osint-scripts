# File: ex1_b.py        
# Date: 05/14/13
# Author: Simon Roses Femerling
# Desc: Simple Google Hacking                
#
# VULNEX (C) 2013
# www.vulnex.com

import requests
import json
import urllib
import const

site="https://www.googleapis.com/customsearch/v1?key="

# Your Google Hacking query
query='' 
query_params='' 

url=site+const.cse_token+"&cx="+const.cse_id+"&q=" + urllib.quote(query+query_params)
response = requests.get(url)
print json.dumps(response.json,indent=4)

# VULNEX EOF
