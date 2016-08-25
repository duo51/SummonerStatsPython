from requests import *
import json

REGION = "na" #NA by default, can be changed
URL = "https://" + REGION + ".api.pvp.net"
APIKEY = ""
RateLimit_perMin = "500" #500 Requests per 10 Minutes
RateLimit_perSec = "10" #10 requests per second


def findByUsername(username):
	# /api/lol/{region}/v1.4/summoner/by-name/{summonerNames}
	r = get(URL+"/api/lol/" + REGION + "/v1.4/summoner/by-name/" + username +"?api_key=" + APIKEY)
	return json.loads(r.text)

def getSummonerID(username):
	r = get(URL+"/api/lol/" + REGION + "/v1.4/summoner/by-name/" + username +"?api_key=" + APIKEY)
	return json.loads(r.text)[username]["id"]

def getSummonerLevel(username):
	r = get(URL+"/api/lol/" + REGION + "/v1.4/summoner/by-name/" + username +"?api_key=" + APIKEY)
	return json.loads(r.text)[username]["summonerLevel"]

def findBySummonerID(ID):
	#/api/lol/{region}/v1.4/summoner/{summonerIds}
	r = get(URL + "/api/lol/" + REGION + "/v1.4/summoner/" + ID + "?api_key=" + APIKEY)
	return r.text

def getMasteries(username):
	#/api/lol/{region}/v1.4/summoner/{summonerIds}/masteries
	r = get(URL+"/api/lol/" + REGION + "/v1.4/summoner/by-name/" + username +"?api_key=" + APIKEY)
	masteries = get(URL + "/api/lol/" + REGION + "/v1.4/summoner/" + str(json.loads(r.text)[username]["id"]) + "/masteries" + "?api_key=" + APIKEY)
	return masteries.text



print(findByUsername("xavidram") )