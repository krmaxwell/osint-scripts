# File: ex2.py         
# Date: 05/14/13
# Author: Simon Roses Femerling
# Desc: Download picture and extract metadata               
#
# VULNEX (C) 2013
# www.vulnex.com

import const
from apiclient.discovery import build
import pprint
import os
from PIL import Image
from StringIO import StringIO
from PIL.ExifTags import TAGS
import requests
import markup

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

pic_id=1
do_stop=10
cnt=1

page=markup.page()

# Set page title
page.init(title="ANTPJI OSINT") 
page.h1("ANTPJI OSINT")

# Set output directory
out_dir = "pics_gepl"

# Your Google Hacking query 
query=''
query_params=''

doquery=query+query_params

service = build("customsearch","v1",developerKey=const.cse_token)

if not os.path.exists(out_dir):
	os.makedirs(out_dir)

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
				pic_url=""
				if 'title' in card:
					if 'fn' in card: name = card['fn']
					if 'photo' in card: pic_url = card['photo']
				if pic_url != "":	
					image = requests.get(pic_url)
					pic_n = os.path.join(out_dir,"%s.jpg") % pic_id
					file = open(pic_n,"w")
					pic_id+=1
					try:
						i = Image.open(StringIO(image.content))
						if hasattr(i,"_getexif"):
							ret = {}
							info = i._getexif()
							if info:
								for k,v in info.items():
									decode = TAGS.get(k,v)
									ret[decode] = v
								print ret
						i.save(file,"JPEG")
						page.p(name.encode('ascii','ignore')) 
						page.img(src=pic_n)
						page.br()
						page.br()
					except IOError, e:
						print "error: %s" % e
					file.close()			

# Set your output filename
with open('index_gepl.html','w') as fp:
	fp.write(str(page))

# VULNEX EOF
