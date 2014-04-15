from nltk import word_tokenize,sent_tokenize
import cPickle as pickle

def isNum(n):
	try:
		n=float(n)
		return float(n)
	except:
		return -1

def getProcessedComments(movieNames,commentsList,unwantedSyms):
	n=0
	comments=dict()
	for movieComments in commentsList:
		processedComments=[]
		string=''
		for sent in movieComments:
			for word in word_tokenize(sent):
				word=word.strip(' ')
				flag=0
				for sym in unwantedSyms:
					if sym in word:
						flag=1
						break
				if flag==0:
					string+=word+' '
		#processedComments.append(string)
		comments[movieNames[n]]=string
		n=n+1
	return comments



def getPickledFile(comments,fname):
	pickle.dump(comments,open(fname,'wb'))
	

def main(fname):
	with open(fname,'r') as f:
		data=f.readlines()		
		combinedComments=[]
		comments=[]
		for line in data:
			if "$$$$" in line:
				comments.append(combinedComments)
				combinedComments=[]
			else:
				combinedComments.append(line)

	return comments

if __name__=="__main__":
	commentsList=main('comments20.txt')
	
	unwantedSyms=['?','(',')',',',':',';','{','}','[',']','\\','\'','\"','.','!','@','#','$','%','^','&','*','/','+','-','_','|','~','`','=']

	with open('movies20.txt','r') as f:
		names=f.readlines()
		movieNames=[]
		for name in names:
			name=name.strip('\n')
			movieNames.append(name)
	
	comments=getProcessedComments(movieNames,commentsList,unwantedSyms)
	
	getPickledFile(comments,'comments20.p')
