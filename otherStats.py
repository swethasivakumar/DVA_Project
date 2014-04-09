import gdata.youtube
import gdata.youtube.service
from gdata.youtube import service



USERNAME = 'gtproject2014@gmail.com'
PASSWORD = 'davaproject2014'
DEVELOPER_KEY = "AIzaSyC9ymJowQNoLdgh1kW8aPwiL8wbLRLbKy0"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

client = service.YouTubeService()
client.ClientLogin(USERNAME, PASSWORD)


yt_service = gdata.youtube.service.YouTubeService()
entry = yt_service.GetYouTubeVideoEntry(video_id='the0KZLEacs')
PrintEntryDetails(entry)
'''def GetAndPrintVideoFeed(uri):
  yt_service = gdata.youtube.service.YouTubeService()
  feed = yt_service.GetYouTubeVideoFeed(uri)
  for entry in feed.entry:
    PrintEntryDetails(entry)
'''
def PrintEntryDetails(entry):
  print 'Video title: %s' % entry.media.title.text
  print 'Video published on: %s ' % entry.published.text
  print 'Video description: %s' % entry.media.description.text
 # print 'Video category: %s' % entry.media.category[[]0].text
  print 'Video tags: %s' % entry.media.keywords.text
  print 'Video watch page: %s' % entry.media.player.url
  print 'Video flash player URL: %s' % entry.GetSwfUrl()
  print 'Video duration: %s' % entry.media.duration.seconds

  # non entry.media attributes
  print 'Video geo location: %s' % entry.geo.location()
  print 'Video view count: %s' % entry.statistics.view_count
  print 'Video rating: %s' % entry.rating.average

  # show alternate formats
  for alternate_format in entry.media.content:
    if 'isDefault' not in alternate_format.extension_attributes:
      print 'Alternate format: %s | url: %s ' % (alternate_format.type,
                                                 alternate_format.url)

  # show thumbnails
  for thumbnail in entry.media.thumbnail:
    print 'Thumbnail url: %s' % thumbnail.url
