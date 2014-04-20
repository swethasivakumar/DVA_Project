import requests

baseURL = "https://gdata.youtube.com/feeds/api/videos/"
API_KEY = 'AIzaSyC9ymJowQNoLdgh1kW8aPwiL8wbLRLbKy0'
parameters = '/comments?orderby=published&max-result='
maxResults = 50
fp = open('55comments.txt','a+')
f = open('55youtubeID.txt','r')
for line in f:
        finalURL = baseURL + line + parameters + str(maxResults) + "&key=" + API_KEY
        print finalURL
        r = requests.get(finalURL)
        fp.write(r.text)
        fp.write("$$$$\n")

