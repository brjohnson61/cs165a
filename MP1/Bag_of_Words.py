from Word import Word
import Term_Frequency_Inverse_Document_Frequency
from math import log1p

class Bag_of_Words:

    def __init__(self):
        self.wordListPos = {}
        self.wordListNeg = {}
        self.totalDocuments = 0
        self.posDocuments = 0
        self.negDocuments = 0
        self.posWords = 0
        self.negWords = 0

    def appendReviews(self, ReviewDictionaries, rType):
        if(rType == "pos"):
            for review in ReviewDictionaries[:1000]:
                for keyword in review:
                    word = Word(keyword, review[keyword], 1)
                    self.append(word, rType)
                self.posDocuments = self.posDocuments + 1
        elif(rType == "neg"):
            for review in ReviewDictionaries[:1000]:
                for keyword in review:
                    word = Word(keyword, review[keyword], 1)
                    self.append(word, rType)
                self.negDocuments = self.negDocuments + 1
                    
        self.totalDocuments = self.totalDocuments + 1

    def append(self, word, rType):
        if(rType == "pos"):
            if(word in self.wordListPos):
                self.updateWord(word, rType)
            else:
                self.appendWord(word, rType)
        elif(rType == "neg"):
            if(word in self.wordListNeg):
                self.updateWord(word, rType)
            else:
                self.appendWord(word, rType)

    def updateWord(self, word, rType):
        if(rType == "pos"):
            self.wordListPos[word.name].update(word)
            self.posWords = self.posWords + word.count
        elif(rType == "neg"):
            self.wordListNeg[word.name].update(word)
            self.negWords = self.negWords + word.count

    def appendWord(self, word, rType):
        if(rType == "pos"):
            self.wordListPos[word.name] = word
            self.posWords = self.posWords + word.count
        elif(rType == "neg"):
            self.wordListNeg[word.name] = word
            self.negWords = self.negWords + word.count

    def getTF_IDF(self, word, rType):
        if(rType == "pos"):
            if(word in self.wordListPos):
                return self[word.name].getTF() * self.totalDocuments
            else:
                return 0
        elif(rType == "neg"):
            if(word in self.wordListNeg):
                return self[word.name].getTF() * self.totalDocuments
            else:
                return 0

    def getProbWordsGivenClass(self, rType):
        bagSublist = {}
        totalWordsInBag = 0
        prob = 1
        totalWordsInBag = 0
        alpha = 1
        if(rType == "pos"):
            bagSublist = self.wordListPos
            totalWordsInBag = self.posWords
        elif(rType == "neg"):
            bagSublist = self.wordListNeg
            totalWordsInBag = self.negWords
        else:
            print("Error: Type of sublist not specified")

        if(len(bagSublist) == 0 or totalWordsInBag == 0):
            return 0
        else:
            for word in bagSublist:
                prob = prob * ((word.count + alpha)/(totalWordsInBag + (alpha*(self.posWords + self.negWords))))
            return log1p(prob)
        