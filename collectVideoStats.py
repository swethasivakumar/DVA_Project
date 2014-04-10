from nltk import word_tokenize
import cPickle as pickle

def isNum(n):
	try:
		n=float(n)
		return float(n)
	except:
		return -1

def getVideoStats(viewCount,likeCount,dislikeCount,favoriteCount,commentCount,fname):
	videoStats=dict()

	with open(fname,'r') as f:
		data=f.readlines()

		#print data
		n=0
		for movie in data:
			print movie
			print n
			movie=movie.strip('\n')
			videoStats[movie]=dict()
			videoStats[movie]['viewCount']=viewCount[n]
			videoStats[movie]['likeCount']=likeCount[n]
			videoStats[movie]['dislikeCount']=dislikeCount[n]
			videoStats[movie]['favoriteCount']=favoriteCount[n]
			videoStats[movie]['commentCount']=commentCount[n]
			n+=1

	return videoStats


def getPickledFile(videoStats,fname):
	pickle.dump(videoStats,open(fname,'wb'))
	

def main(fname):
	with open(fname,'r') as f:
		data=f.readlines()
		lineBlock=[]
		videoStats=dict()
		Stats=[]
		viewCount=[]
		likeCount=[]
		dislikeCount=[]
		favoriteCount=[]
		commentCount=[]
		
		for line in data:
			line=line.split('$$$$')
			if "viewCount" in line[0]:
				for word in word_tokenize(line[0]):
					n=isNum(word)
					if n!=-1:
						viewCount.append(n)



			if "likeCount" in line[0]:
				for word in word_tokenize(line[0]):
					n=isNum(word)
					if n!=-1:
						likeCount.append(n)

				

			if "dislikeCount" in line[0]:
				for word in word_tokenize(line[0]):
					n=isNum(word)
					if n!=-1:
						dislikeCount.append(n)
				

			if "favoriteCount" in line[0]:
				for word in word_tokenize(line[0]):
					n=isNum(word)
					if n!=-1:
						favoriteCount.append(n)

			if "commentCount" in line[0]:
				for word in word_tokenize(line[0]):
					n=isNum(word)
					if n!=-1:
						commentCount.append(n)
				
	return viewCount,likeCount,dislikeCount,favoriteCount,commentCount

if __name__=="__main__":
	viewCount,likeCount,dislikeCount,favoriteCount,commentCount=main('videoStats20.txt')

	videoStats=getVideoStats(viewCount,likeCount,dislikeCount,favoriteCount,commentCount,'movies20.txt')

	getPickledFile(videoStats,'videoStats20.p')


	#print videoStats