from gdata.youtube import service

USERNAME = 'gtproject2014@gmail.com'
PASSWORD = 'davaproject2014'
#VIDEO_ID = 'mE295ggKbHU'

def comments_generator(client, video_id):
    comment_feed = client.GetYouTubeVideoCommentFeed(video_id=video_id)
    while comment_feed is not None:
        for comment in comment_feed.entry:
             yield comment
        next_link = comment_feed.GetNextLink()
        if next_link is None:
             comment_feed = None
        else:
             comment_feed = client.GetYouTubeVideoCommentFeed(next_link.href)

client = service.YouTubeService()
client.ClientLogin(USERNAME, PASSWORD)
fp = open('comments20.txt','a+')
f = open('ID20.txt', 'r')
for line in f:
	VIDEO_ID = line
	print line
	for comment in comments_generator(client, VIDEO_ID):
    		author_name = comment.author[0].name.text
    		text = comment.content.text
    		fp.write("{}: {}".format(author_name, text))
	fp.write("$$$$")
