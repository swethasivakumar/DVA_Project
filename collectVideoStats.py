from nltk import word_tokenize

def isNum(n):
	try:
		n=float(n)
		return float(n)
	except:
		return 0

def getVideoStats(viewCount,likeCount,dislikeCount,favoriteCount,commentCount,fname):
	videoStats=dict()

	with open(fname,'r') as f:
		data=f.readlines()

		for n,movie in enumerate(data):
			videoStats[movie]=dict()
			videoStats[movie]['viewCount']=viewCount[n]
			videoStats[movie]['likeCount']=likeCount[n]
			videoStats[movie]['dislikeCount']=dislikeCount[n]
			videoStats[movie]['favoriteCount']=favoriteCount[n]
			videoStats[movie]['commentCount']=commentCount[n]

	return videoStats



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
					n=isNum(word):
					if n>0:
						viewCount.append(n)



			if "likeCount" in line[0]:
				for word in word_tokenize(line[0]):
					n=isNum(word):
					if n>0:
						likeCount.append(n)

				

			if "dislikeCount" in line[0]:
				for word in word_tokenize(line[0]):
					n=isNum(word):
					if n>0:
						dislikeCount.append(n)
				

			if "favoriteCount" in line[0]:
				for word in word_tokenize(line[0]):
					n=isNum(word):
					if n>0:
						favoriteCount.append(n)

			if "commentCount" in line[0]:
				for word in word_tokenize(line[0]):
					n=isNum(word)
					if n>0:
						commentCount.append(n)
				
	return viewCount,likeCount,dislikeCount,favoriteCount,commentCount

if __name__=="__main__":
	viewCount,likeCount,dislikeCount,favoriteCount,commentCount=main('videoStats20.txt')

	videoStats=getVideoStats(viewCount,likeCount,dislikeCount,favoriteCount,commentCount,'movies20.txt')

	print videoStats