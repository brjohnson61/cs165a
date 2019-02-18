from Bag_of_Words import Bag_of_Words
from Term_Frequency_Inverse_Document_Frequency import Term_Frequency_Inverse_Document_Frequency
from ReviewType import ReviewType
from enum import Enum
from numpy import log1p

class ReviewClassifier:
    
    def __init__(self):
        self.posBag = Bag_of_Words()
        self.negBag = Bag_of_Words()
  
    def train(self, file, rType):
        listOfReviews = self.niceInputFromFile(file)
        listOfReviewDictionaries = self.getUniqueWordCountDict(listOfReviews)

        if(rType == "pos"):
            bag = self.posBag
        elif(rType == "neg"):
            bag = self.negBag

        print("appending " + str(len(listOfReviewDictionaries)) + " reviews dictionaries to " + rType + " bag...")
        bag.appendReviews(listOfReviewDictionaries)

    def evaluateNaiveBoW(self, file):
        listOfReviews = self.niceInputFromFile(file)
        listOfReviewDictionaries = self.getUniqueWordCountDict(listOfReviews)
        posProb = 0
        negProb = 0
        negReviews = 0
        posReviews = 0
        vocabularySize = len(self.posBag.wordList.keys()) + len(self.negBag.wordList.keys())

        for review in listOfReviewDictionaries:
            posProb = 0
            negProb = 0
            for word in review:
                posProb = posProb + self.posBag.getProbOfWordGivenClass(word, vocabularySize)
                negProb = negProb + self.negBag.getProbOfWordGivenClass(word, vocabularySize)
                if(word == "dieflgkdfljgldksjdlkjslvkjaldvjlkajlkadjvlvjlf"):
                    print("Positive occurrences: " + str(self.posBag.wordList[word].count))
                    print("P(" + word + " | positive) = " + str(self.posBag.getProbOfWordGivenClass(word, vocabularySize)))
                    print("Negative occurrences: " + str(self.negBag.wordList[word].count))
                    print("P(" + word + " | negative) = " + str(self.negBag.getProbOfWordGivenClass(word, vocabularySize)))
                    print()
            
            #print()
            #print("posProbTotal: " + str(posProb))
            #print("negProbTotal: " + str(negProb))
            if(posProb > negProb):
                posReviews = posReviews + 1
            elif(negProb > posProb): 
                negReviews = negReviews + 1
        print("###### NAIVE BOW ######")
        print("Positive Reviews: " + str(posReviews) + " " + str((posReviews/(posReviews + negReviews))*100) + "%.")
        print("Negative Reviews: " + str(negReviews) + " " + str((negReviews/(posReviews + negReviews))*100) + "%.")

    def evaluateNaiveTFIDF(self, file):
        listOfReviews = self.niceInputFromFile(file)
        listOfReviewDictionaries = self.getUniqueWordCountDict(listOfReviews)
        posTFIDF = 0
        negTFIDF = 0
        negReviews = 0
        posReviews = 0
        vocabularySize = len(self.posBag.wordList.keys()) + len(self.negBag.wordList.keys())

        for review in listOfReviewDictionaries:
            posTFIDF = 0
            negTFIDF = 0
            for word in review:
                posTFIDF = posTFIDF + review[word]*self.posBag.getTFIDFOfWordGivenClass(word, vocabularySize)
                negTFIDF = negTFIDF + self.negBag.getTFIDFOfWordGivenClass(word, vocabularySize)
    
            #print()
            #print("posTFIDF: " + str(posTFIDF))
            #print("negTFIDF: " + str(negTFIDF))
            
            if(posTFIDF > negTFIDF):
                posReviews = posReviews + 1
            elif(negTFIDF > posTFIDF): 
                negReviews = negReviews + 1
        
        print("###### NAIVE TFIDF ######")
        print()
        print("Positive Reviews: " + str(posReviews) + " " + str((posReviews/(posReviews + negReviews))*100) + "%.")
        print("Negative Reviews: " + str(negReviews) + " " + str((negReviews/(posReviews + negReviews))*100) + "%.")
  
    def evaluateAndTrain(self, file):
        print("stub!")

    def niceInputFromFile(self, file):
        stopWords = self.getStopWords()
        fileHandle = open(file, "rt")
        trainingReviewsString = ""

        for line in fileHandle:
            trainingReviewsString = trainingReviewsString + line

        trainingReviewsString = trainingReviewsString.lower()
        trainingReviewsString = trainingReviewsString.replace(",", " ")
        trainingReviewsString = trainingReviewsString.replace("-", " ")
        trainingReviewsString = trainingReviewsString.replace("?", " ")
        trainingReviewsString = trainingReviewsString.replace("!", " ")
        trainingReviewsString = trainingReviewsString.replace("\'s", " ")
        trainingReviewsString = trainingReviewsString.replace("{", " ")
        trainingReviewsString = trainingReviewsString.replace("}", " ")
        trainingReviewsString = trainingReviewsString.replace("[", " ")
        trainingReviewsString = trainingReviewsString.replace("]", " ")
        trainingReviewsString = trainingReviewsString.replace("*", " ")
        trainingReviewsString = trainingReviewsString.replace("|", " ")
        trainingReviewsString = trainingReviewsString.replace("$", " ")
        trainingReviewsString = trainingReviewsString.replace("_", " ")
        trainingReviewsString = trainingReviewsString.replace("^", " ")
        trainingReviewsString = trainingReviewsString.replace("&", " ")
        trainingReviewsString = trainingReviewsString.replace("(", " ")
        trainingReviewsString = trainingReviewsString.replace(")", " ")
        trainingReviewsString = trainingReviewsString.replace("{", " ")
        trainingReviewsString = trainingReviewsString.replace("+", " ")
        trainingReviewsString = trainingReviewsString.replace("=", " ")
        trainingReviewsString = trainingReviewsString.replace("@", " ")
        trainingReviewsString = trainingReviewsString.replace("\"", " ")
        trainingReviewsString = trainingReviewsString.replace("\'", " ")
        trainingReviewsString = trainingReviewsString.replace("\n", " ")
        trainingReviewsString = trainingReviewsString.replace(".", " ")
        trainingReviewsString = trainingReviewsString.replace(":", " ")
        trainingReviewsString = trainingReviewsString.replace(";", " ")
        trainingReviewsString = trainingReviewsString.replace("~", " ")
        trainingReviewsString = trainingReviewsString.replace("`", " ")
        #trainingReviewsString = trainingReviewsString.replace("", "i")
        trainingReviewsString = trainingReviewsString.replace('', "")
        trainingReviewsString = trainingReviewsString.replace(" d ", " ")
        trainingReviewsString = trainingReviewsString.replace("/", " ")
        for stopWord in stopWords:
            trainingReviewsString = trainingReviewsString.replace(" " + stopWord + " ", " ")

        reviewList = trainingReviewsString.split("<br  ><br  >")

        #print("ReviewListLength: " + str(len(reviewList)))
        return reviewList

    def getUniqueWordCountDict(self, reviewList):
        listOfParsedReviews = []
        for review in reviewList:
            reviewDict = {}
            wordSet = set(review.split(" "))
            for uniqueWord in wordSet:
                if(uniqueWord):
                    reviewDict[uniqueWord] = review.count(uniqueWord)

            listOfParsedReviews.append(reviewDict)
        
        return listOfParsedReviews

    def getStopWords(self):
        stopWordsList = []
        with open("stop_words.txt", "rt") as file:
            for stopWord in file:
                stopWordsList.append(stopWord.rstrip("\n"))
        return stopWordsList
     
if __name__ == "__main__":
    classifier = ReviewClassifier()
    classifier.train("training_pos.txt", "pos")
    classifier.train("training_neg.txt", "neg")

    classifier.evaluateNaiveBoW("test_neg_public.txt")
    classifier.evaluateNaiveBoW("test_pos_public.txt")

