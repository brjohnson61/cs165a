from Bag_of_Words import Bag_of_Words
from Term_Frequency_Inverse_Document_Frequency import Term_Frequency_Inverse_Document_Frequency
from ReviewType import ReviewType
from enum import Enum

class ReviewClassifier:
    
    def __init__(self):
        self.trained = False
        self.bag = Bag_of_Words()
  
    def train(self, file, rType):
        
        listOfReviews = self.niceInputFromFile(file)
        listOfReviewDictionaries = self.getUniqueWordCountDict(listOfReviews)

        print("appending review dictionaries to bag...")
        self.bag.appendReviews(listOfReviewDictionaries, rType)

        print("Positive Words: " + str(len(self.bag.wordListPos)))
        print("Negative Words: " + str(len(self.bag.wordListNeg)))
        

    def evaluate(self, file):
        listOfReviews = self.niceInputFromFile(file)
        listOfReviewDictionaries = self.getUniqueWordCountDict(listOfReviews)
        posProb = 1
        negProb = 1
        negReviews = 0
        posReviews = 0
        #printCounter = 0

        for review in listOfReviewDictionaries:
            for word in review:
                posProb = posProb * self.bag.getProbOfWordGivenClass(word, "pos")
                negProb = negProb * self.bag.getProbOfWordGivenClass(word, "neg")
            if((posProb * (self.bag.posDocuments/self.bag.totalDocuments)) > (negProb * (self.bag.negDocuments/self.bag.totalDocuments))):
                posReviews = posReviews + 1
            else: 
                negReviews = negReviews + 1

            """ if(printCounter < 100):
                print("NegProb: " + str(negProb))
                print("PosProb: " + str(posProb))
                printCounter = printCounter + 1 """
        
        print("Positive Reviews: " + str(posReviews) + " " + str((posReviews/(posReviews + negReviews))*100) + "%.")
        print("Negitive Reviews: " + str(negReviews) + " " + str((negReviews/(posReviews + negReviews))*100) + "%.")


        

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
        trainingReviewsString = trainingReviewsString.replace("í", "i")
        trainingReviewsString = trainingReviewsString.replace("/", " ")
        for stopWord in stopWords:
            trainingReviewsString = trainingReviewsString.replace(stopWord, " ")

        reviewList = trainingReviewsString.split("<br  ><br  >")
        
        # for review in reviewList:
        #     wordSet = set(review.split(" "))
        #     for uniqueWord in wordSet:
        #         reviewDict[uniqueWord] = review.count(uniqueWord)

        #     listOfParsedReveiws.append(reviewDict)
        
        return reviewList

    def getUniqueWordCountDict(self, reviewList):
        listOfParsedReveiws = []
        reviewDict = {}
        for review in reviewList:
            wordSet = set(review.split(" "))
            for uniqueWord in wordSet:
                reviewDict[uniqueWord] = review.count(uniqueWord)

            listOfParsedReveiws.append(reviewDict)
        
        return listOfParsedReveiws

    def getStopWords(self):
        file = open("stop_words.txt", "rt")
        stopWordsList = []

        for stopWord in file:
            stopWordsList.append(stopWord.rstrip("\n"))
        
        return stopWordsList
     
if __name__ == "__main__":
    classifier = ReviewClassifier()
    classifier.train("training_pos.txt", "pos")
    classifier.train("training_neg.txt", "neg")
    fHandle = open("log.txt", "w")
    for item in classifier.bag.wordListNeg:
        fHandle.write(item)

    for item in classifier.bag.wordListPos:
        fHandle.write(str(item))

    classifier.evaluate("test_pos_public.txt")
    classifier.evaluate("test_neg_public.txt")

