from gdata import youtube as yt
from gdata.youtube import service as yts

username = 'gtproject2014@gmail.com'
pwd = 'davaproject2014'

client = yts.YouTubeService()
client.ClientLogin(username, pwd) #the pwd might need to be application specific fyi

fp = open('comments20.txt','a+')
f = open('ID20.txt', 'r')
for line in f:
        VIDEO_ID = line
        print line
	comments = client.GetYouTubeVideoComments(video_id=VIDEO_ID)
	i = 0
	while(i<2):
		print comments.entry[i]
