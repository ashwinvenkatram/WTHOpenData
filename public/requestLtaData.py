#http://www.lihaoyi.com/post/PlanningBusTripswithPythonSingaporesSmartNationAPIs.html#conclusion

import requests
import json
import sys

headers = { 'AccountKey' :'insertAccKey' ,
 'accept' : 'application/json'}


jsonBusStops = []


def dataMallQuery(urlReq,jsonBusStops):
	#Each URL call on retrieves 50 datapoints params={'$skip': 50}).json()['value']
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



if __name__=="__main__":
	headers['AccountKey']=sys.argv[1]
	urlReq = sys.argv[2]
	saveFile = "busStops.json"
	dataMallQuery(urlReq,jsonBusStops)
	saveToFile(jsonBusStops,saveFile)