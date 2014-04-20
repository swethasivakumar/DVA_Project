from gdata.youtube import service

USERNAME = 'gtproject2014@gmail.com'
PASSWORD = 'davaproject2014'
#VIDEO_ID = 'r5X-hFf6Bwo'
MAX_RESULTS = 1
def comments_generator(client, video_id):
    comment_feed = client.GetYouTubeVideoCommentFeed(video_id=video_id)
    i = 0
    while (comment_feed is not None and i < MAX_RESULTS):
        for comment in comment_feed.entry:
             yield comment
        next_link = comment_feed.GetNextLink()
        if next_link is None:
             comment_feed = None
        else:
             comment_feed = client.GetYouTubeVideoCommentFeed(next_link.href)
	
	i = i+1

client = service.YouTubeService()
client.ClientLogin(USERNAME, PASSWORD)
fp = open('55comments.txt','a+')
f = open('temp.txt', 'r')
for line in f:
	#VIDEO_ID = str(line)
#	if(str(line) == VIDEO_ID):
#		print "1"
	lineArray = line.split();
	print lineArray
	videoID = lineArray[0]
	print videoID
	VIDEO_ID = str(videoID)
	print VIDEO_ID
	for comment in comments_generator(client, VIDEO_ID):
		print "reaches here"
    		author_name = comment.author[0].name.text
    		text = comment.content.text
    		fp.write("{}".format(text))
		fp.write("\n");
	fp.write("$$$$")
	fp.write("\n");
fp.close()
