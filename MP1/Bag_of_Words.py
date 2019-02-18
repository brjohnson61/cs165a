from Word import Word
import Term_Frequency_Inverse_Document_Frequency
from numpy import log

class Bag_of_Words:

    def __init__(self):
        self.wordList = {}
        self.totalDocuments = 0
        self.wordCount = 0

    def appendReviews(self, ReviewDictionaries):
        for review in ReviewDictionaries:
            totalWordsInReview = 0
            for keyword in review:
                totalWordsInReview = totalWordsInReview + review[keyword]
            for keyword in review:
                word = Word(keyword, review[keyword], 1, totalWordsInReview)
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

    def getTF_IDF(self, word):
        if(word in self.wordList):
            return self.wordList[word].getTF() * self.totalDocuments
        else:
            return 0

    def getProbOfWordGivenClass(self, word, vocabularySize):
        prob = 0
        alpha = 1
        number = 0
        if(word in self.wordList): 
            number = self.wordList[word].count

        prob = (float(number + alpha)/float(self.wordCount + alpha*vocabularySize))
    
        return log(prob)

    def getTFIDFOfWordGivenClass(self, word, vocabularySize):
        prob = 0
        alpha = 1
        number = 0
        
        if(word in self.wordList):
            number = self.getTF_IDF(word)
        else:
            number = 0
        prob = (float(number + alpha)/float(alpha*vocabularySize))
       
        return log(prob)
    