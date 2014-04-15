import collections
import sys
import csv
import pickle


wordFinalScore = {}
swnFilePath = "/home/swetha/Downloads/SentiWordNet_3.0.0_20130122.txt "
objFile = "wordScore.p"

def createSample():
	c = collections.Counter()
	movies = {}
	
	c['good'] = 3
	c['awesome'] = 5
	c['amazing'] = 10
	c['okay'] = 3
	c['what'] = 3
	c['random'] = 1
	
	movies['harry potter'] = c
	print movies
	
	c1 = collections.Counter()
	c1['horrible'] = 2
	c1['bad'] = 5
	c1['okay'] = 3
	movies['random'] = c1
	print movies
	return movies



def readSentiWordNet(swnFilePath):
	wordScore = {}
	for line in open("SentiWordNet_3.0.0_20130122.txt", 'r'):
	#for line in open("sample.txt", 'r'):
		#check if a line is a comment
		if line[0] != '#':
			fields = line.split("\t")
			#check if the line is formatted correctly	
			if len(fields) != 6:
				print "Parsing error, the file does not have 6 columns"
			#denotes if a word is a noun (n), adj (a), adverb (r) or a verb(v)  
			wordType = fields[0]
			posScore = float(fields[2])
			negScore = float(fields[3])
			score = posScore - negScore
			#split the synset into individual words and combine it with the wordType to store as key in the dictionary
			synSet = fields[4].split(" ")
			for words in synSet:
				rankScore = {}
				wordAndRank = words.split('#')
				wordKey = wordAndRank[0]+'#'+wordType
				rank = int(wordAndRank[1])
				#check if the word is already present in the wordScore dict. Then get its value in a temp rankScore dictionary. Check if the current rank already exists and add the score otherwise.
				print wordKey
				if wordKey in wordScore.keys():
					rankScore = wordScore[wordKey]
					rankScore[rank] = score
					wordScore[wordKey] = rankScore
				else:
					rankScore = {}
					rankScore[rank] = score
                                        wordScore[wordKey] = rankScore
	return wordScore
			
			
	
#This method combines the different ranks and scores for each word and calculates a final score
def calculateScore(wordScore):
	print "wordScore", wordScore
	finalScoreDict = {}
	for word, rankScore in wordScore.items():
		finalScore = 0
		Sum = 0
		for rank, score in rankScore.items():
			s = float(score)
			r = float(rank)
			finalScore += float(s/r)
			Sum += 1.0/r
		finalScore = finalScore/Sum
		finalScoreDict[word] = finalScore
	return finalScoreDict


def serialize(wordFinalScore, objFile):
	pickle.dump( wordFinalScore, open( objFile, "wb" ) ) 


def deserialize(objFile):
	wordFinalScore = pickle.load( open( objFile, "rb" ) )	
	return wordFinalScore



if __name__ == '__main__':
	movies = createSample()
	wordScore = readSentiWordNet (swnFilePath)
	#print "wordScore inside main", wordScore
	wordFinalScore = calculateScore (wordScore)
	serialize (wordFinalScore, objFile)
	#sample = deserialize("wordScore.p")
	#print "SAMPLE", sample


	
