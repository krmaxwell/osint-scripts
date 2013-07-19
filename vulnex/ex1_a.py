# File: ex1_a.py
# Date: 05/14/13
# Author: Simon Roses Femerling
# Desc: Basic Google Hacking 
#
# VULNEX (C) 2013
# www.vulnex.com

import const
from apiclient.discovery import build
import pprint

# your google hacking query
query=''
query_params=''

doquery=query+query_params

service = build("customsearch","v1",developerKey=const.cse_token)

res = service.cse().list(
	q=doquery,
	cx=const.cse_id,
	num=10).execute()

pprint.pprint(res)

# VULNEX EOF
