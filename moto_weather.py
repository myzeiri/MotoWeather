import urllib.request
import xml.etree.ElementTree as ET

MIN_TEMP = 40

def printWeather(dict):
	print(dict['day'] + " " + dict['date'])
	print(" Low: " + dict['low'])
	print(" High: " + dict['high'])
	print(" Conditions: " + dict['text'] + "\n")

def isSuitable(condition):
	#From https://developer.yahoo.com/weather/archive.html#codes
	return int(condition) >= 26 and int(condition) <= 34

def isWarmEnough(temp):
	return temp >= MIN_TEMP


yql_url = "https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text=%22columbus,%20oh%22)"

with urllib.request.urlopen(yql_url) as response:
   data = response.read()

tree = ET.fromstring(data)

print("\nAcceptable Days to Ride:\n")

i = 6
while i < 16:
	info = tree[0][0][12][i].attrib
	condition = info['code']
	low = info['low']

	if isSuitable(condition) and isWarmEnough(int(low)):
		#print(info['day'] + " " + info['date'])
		printWeather(info)

	i += 1
