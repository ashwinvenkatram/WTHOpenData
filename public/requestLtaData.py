#http://www.lihaoyi.com/post/PlanningBusTripswithPythonSingaporesSmartNationAPIs.html#conclusion

import requests
import json
import sys

headers = { 'AccountKey' :'insertAccKey' ,
 'accept' : 'application/json'}


jsonBusStops = []


def dataMallQuery(urlReq,jsonBusStops):
	#Each URL call retrieves 50 datapoints. Hence params={'$skip': 50}).json()['value']
	while True:
		content = requests.get(
			urlReq,
			headers=headers, 
			params={'$skip': len(jsonBusStops)}
			).json()['value']
		if content==[]:
			break
		else:
			jsonBusStops += content

def saveToFile(jsonObj,saveFile):
	with open(saveFile,"w") as outfile:
 		json.dump(jsonObj, outfile, sort_keys=True, indent=4,ensure_ascii=False)

if __name__=="__main__":
	headers['AccountKey']=sys.argv[1]
	urlReq = sys.argv[2]
	saveFile = "busStops.json"
	dataMallQuery(urlReq,jsonBusStops)
	saveToFile(jsonBusStops,saveFile)