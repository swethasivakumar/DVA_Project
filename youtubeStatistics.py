import requests

baseURL = "https://www.googleapis.com/youtube/v3/videos?id="
API_KEY = 'AIzaSyC9ymJowQNoLdgh1kW8aPwiL8wbLRLbKy0'
parameters = '&part=statistics'
fp = open('55videoStats.txt','a+')
f = open('55youtubeID.txt','r')
for line in f:
	finalURL = baseURL + line + "&key=" + API_KEY + parameters
	print finalURL
	r = requests.get(finalURL)
	fp.write(r.text)
	fp.write("$$$$\n")
