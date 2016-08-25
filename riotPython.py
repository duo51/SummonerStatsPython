from requests import *

REGION = "na" #NA by default, can be changed
URL = "https://" + REGION + ".api.pvp.net"
APIKEY = "051db1a2-6b57-41c4-bc99-1e3a29056047"
RateLimit_perMin = "500" #500 Requests per 10 Minutes
RateLimit_perSec = "10" #10 requests per second


def findByUsername(username):
	# /api/lol/{region}/v1.4/summoner/by-name/{summonerNames}
	r = get(URL+"/api/lol/" + REGION + "/summoner/by-name/" + username)
	return r.url

print(findByUsername("Xavidram") )
