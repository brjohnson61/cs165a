from Word import Word
from numpy import log
from numpy import sqrt
from numpy import std
from numpy import pi
from numpy import power
from numpy import mean

class Bag_of_Words:

    def __init__(self):
        self.wordList = {}
        self.totalDocuments = 0
        self.wordCount = 0

    def appendReviews(self, ReviewDictionaries):
        totalNumberOfReviews = len(ReviewDictionaries)
        totalDocsContainingWord = {}
        for review in ReviewDictionaries:
            for keyword in review:
                if(keyword not in totalDocsContainingWord):
                    totalDocsContainingWord[keyword] = 1
                else:
                    totalDocsContainingWord[keyword] = totalDocsContainingWord[keyword] + 1
        for review in ReviewDictionaries:
            totalWordsInReview = 0
            for keyword in review:
                totalWordsInReview = totalWordsInReview + review[keyword]
            for keyword in review:
                word = Word(keyword, review[keyword], totalDocsContainingWord[keyword], totalWordsInReview, totalNumberOfReviews, self.totalDocuments)
                self.append(word)
            self.totalDocuments = self.totalDocuments + 1

    def append(self, word):
        if(word.name in self.wordList):
            self.updateWord(word)
        else:
            self.appendWord(word)

    def updateWord(self, word):
        self.wordList[word.name].update(word)
        self.wordCount = self.wordCount + word.count

    def appendWord(self, word):
        self.wordList[word.name] = word
        self.wordCount = self.wordCount + word.count


    def getProbOfWordGivenClass(self, word, vocabularySize):
        prob = 0
        alpha = 1
        number = 0
        if(word in self.wordList): 
            number = self.wordList[word].count

        prob = (float(number + alpha)/float(self.wordCount + alpha*vocabularySize))
    
        return log(prob)

    def getGaussianProbOfWordGivenClass(self, word, frequency):
        prob = 0
        if(word in self.wordList):
            sigma = self.wordList[word].statsList.std()
            mu = self.wordList[word].statsList.mean()
            v = frequency
            if(sigma != 0):
                prob = log(1/(sqrt(2*pi*(sigma**2)))) - (((v - mu)**2)/(2*sigma))

        return prob
    
    def getGaussianTFIDFOfWordGivenClass(self, word, tfidfOther):
        prob = 0
        if(word in self.wordList):
            tfidf = self.wordList[word].statsListTotal
            sigma = tfidf.std()
            mu = tfidf.mean()
            v = tfidfOther
            if(sigma !=0):
                prob = log(1/(sqrt(2*pi*(sigma**2)))) - (((v - mu)**2)/(2*sigma))
       
        return prob
    