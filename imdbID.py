import requests
import json

baseURL = "http://www.omdbapi.com/?t="
parameters = '&part=statistics'
fp = open('250imdbID.txt','a+')
f = open('250movies.txt','r')
for line in f:
	lineArray = [ ]
	parameters= ""
	lineArray = line.split(" ")
	for i in range (0,len(lineArray)):
		if lineArray[i] is not "\n":
			lineArray[i] = lineArray[i].strip()
			parameters = parameters + lineArray[i] + "%20"
	finalURL = baseURL + parameters
	#print finalURL
	r = requests.get(finalURL)
	data = json.loads(r.text)
	fp.write(data["imdbID"])
	fp.write("\n")
