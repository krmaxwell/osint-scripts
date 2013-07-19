# File: ex3.py         
# Date: 05/14/13
# Author: Simon Roses Femerling
# Desc: Build graph from profiles                
#
# VULNEX (C) 2013
# www.vulnex.com

import const
from apiclient.discovery import build
import networkx as nx
import matplotlib.pyplot as plt

def do_query(istart=0):
	if istart == 0:
		res = service.cse().list(
		q=doquery,
		cx=const.cse_id,
		num=10).execute()
	else:
		res = service.cse().list(
		q=doquery,
		cx=const.cse_id,
		num=10,
		start=istart).execute()
	return res

do_stop=10
cnt=1

# Your Google Hacking query here
query=''
query_params=''

doquery=query+query_params

service = build("customsearch","v1",developerKey=const.cse_token)

G=nx.DiGraph()
res=[]
while True:
	if cnt==1:
		res = do_query()
	else:
		if not res['queries'].has_key("nextPage"): break
		res = do_query(res['queries']['nextPage'][0]['startIndex'])
	cnt+=1
	if cnt > do_stop: break
	if res.has_key("items"):
		for item in res['items']:
			name=""
			if not item.has_key('pagemap'): continue
			if not item['pagemap'].has_key('hcard'): continue
			hcard = item['pagemap']['hcard']
			for card in hcard:
				if 'title' in card:
					if 'fn' in card: name = card['fn']
				G.add_edge(name,card["fn"])		
			
plt.figure(figsize=(30,30))
nx.draw(G)
# Set your output filename
plt.savefig('antpji_rela_map.png')

# VULNEX EOF
