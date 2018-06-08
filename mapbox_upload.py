from mapbox import Uploader
from time import sleep
from random import randint
import os
import sys

filename = sys.argv[-1]
service = Uploader()
service.session.params['access_token'] == os.environ['MAPBOX_ACCESS_TOKEN']

basename = os.path.basename(filename)
mapid = basename[:32]

with open(filename, 'rb') as src:
    upload_resp = service.upload(src, mapid)

if upload_resp.status_code == 422:
	for i in range(5):
		sleep(5)
		with open(filename, 'rb') as src:
			upload_resp = service.upload(src, mapid)
		if upload_resp.status_code != 422:
			break


