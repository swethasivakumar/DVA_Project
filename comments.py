# This sample assumes a client object has been created.
# To learn more about creating a client, check out the starter:
#  https://developers.google.com/+/quickstart/python
from gdata.youtube import service

USERNAME = 'gtproject2014@gmail.com'
PASSWORD = 'davaproject2014'
VIDEO_ID = 'mE295ggKbHU'

client = service.YouTubeService()
client.ClientLogin(USERNAME, PASSWORD)


comments_resource = service.comments()
comments_document = comments_resource.list( \
    maxResults=5,activityId=VIDEO_ID).execute()

if 'items' in comments_document:
  print 'got page with %d' % len( comments_document['items'] )
  for comment in comments_document['items']:
    print comment['id'], comment['object']['content']
