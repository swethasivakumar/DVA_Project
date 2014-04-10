from gdata import youtube as yt
from gdata.youtube import service as yts

username = 'gtproject2014@gmail.com'
pwd = 'davaproject2014'
vid = 'zHRQ49cohEw'
client = yts.YouTubeService()
client.ClientLogin(username, pwd) #the pwd might need to be application specific fyi

comments = client.GetYouTubeVideoComments(video_id = vid)
print comments.entry[0]
