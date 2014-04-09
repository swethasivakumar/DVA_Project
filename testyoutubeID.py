from gdata.youtube import service
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser

USERNAME = 'gtproject2014@gmail.com'
PASSWORD = 'davaproject2014'
DEVELOPER_KEY = "AIzaSyC9ymJowQNoLdgh1kW8aPwiL8wbLRLbKy0"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

client = service.YouTubeService()
client.ClientLogin(USERNAME, PASSWORD)

def youtube_search(options):
	youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)

	'''search_response = youtube.search().list(
    q=options.q,
    part="id,snippet",
    maxResults=options.max_results
  ).execute()'''
	f = open('ID20.txt','a')
	fp = open('trailers20.txt','r')
	for line in fp:
		search_response = youtube.search().list(q=line,part="id",maxResults=options.max_results
,type="video",fields="items/id").execute()

		videos = []

		for search_result in search_response.get("items", []):
			videos.append("%s" % (search_result["id"]["videoId"]))
		f.write("\n".join(videos))
		f.write("\n")

		print "Videos:\n", "\n".join(videos), "\n"

if __name__ == "__main__":
  argparser.add_argument("--q", help="Search term", default="Google")
  argparser.add_argument("--max-results", help="Max results", default=1)
  args = argparser.parse_args()

  try:
    youtube_search(args)
  except HttpError, e:
    print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)
