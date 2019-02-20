from Bag_of_Words import Bag_of_Words

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

    def evaluateGaussianBoW(self, file):
        listOfReviews = self.niceInputFromFile(file)
        listOfReviewDictionaries = self.getUniqueWordCountDict(listOfReviews)
        posProb = 0
        negProb = 0
        negReviews = 0
        posReviews = 0
        #vocabularySize = len(self.posBag.wordList.keys()) + len(self.negBag.wordList.keys())

        for review in listOfReviewDictionaries:
            posProb = 0
            negProb = 0
            for keyword in review:
                posProb = posProb + self.posBag.getGaussianProbOfWordGivenClass(keyword, review[keyword])
                negProb = negProb + self.negBag.getGaussianProbOfWordGivenClass(keyword, review[keyword])

            if(posProb > negProb):
                posReviews = posReviews + 1
            elif(negProb > posProb): 
                negReviews = negReviews + 1
        print("###### GAUSSIAN BOW ######")
        print("Positive Reviews: " + str(posReviews) + " " + str((float(posReviews)/float(posReviews + negReviews))*100) + "%.")
        print("Negative Reviews: " + str(negReviews) + " " + str((float(negReviews)/float(posReviews + negReviews))*100) + "%.")

    def evaluateMultinomialNaiveBoW(self, file):
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
                
            if(posProb > negProb):
                posReviews = posReviews + 1
            elif(negProb > posProb): 
                negReviews = negReviews + 1
        print("###### MULTINOMIAL BOW ######")
        print("Positive Reviews: " + str(posReviews) + " " + str((float(posReviews)/float(posReviews + negReviews))*100) + "%.")
        print("Negative Reviews: " + str(negReviews) + " " + str((float(negReviews)/float(posReviews + negReviews))*100) + "%.")

    def evaluateGaussianTFIDF(self, file):
        listOfReviews = self.niceInputFromFile(file)
        listOfReviewDictionaries = self.getUniqueWordCountDict(listOfReviews)
        posTFIDF = 0
        negTFIDF = 0
        negReviews = 0
        posReviews = 0
        index = 0
        
        evalBag = Bag_of_Words()
        evalBag.appendReviews(listOfReviewDictionaries)

        for review in listOfReviewDictionaries:
            posTFIDF = 0
            negTFIDF = 0
            for keyword in review:
                tfidfOfUnknown = evalBag.wordList[keyword].statsListTotal[index]
                posTFIDF = posTFIDF + self.posBag.getGaussianTFIDFOfWordGivenClass(keyword, tfidfOfUnknown)
                negTFIDF = negTFIDF + self.negBag.getGaussianTFIDFOfWordGivenClass(keyword, tfidfOfUnknown)
                
            index = index + 1
            if(posTFIDF > negTFIDF):
                posReviews = posReviews + 1
            elif(negTFIDF > posTFIDF): 
                negReviews = negReviews + 1
            
        print("###### GAUSSIAN TFIDF ######")
        print("Positive Reviews: " + str(posReviews) + " " + str((float(posReviews)/float(posReviews + negReviews))*100) + "%.")
        print("Negative Reviews: " + str(negReviews) + " " + str((float(negReviews)/float(posReviews + negReviews))*100) + "%.")

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

    print("##### TRAINING #####")
    classifier.train("training_pos.txt", "pos")
    classifier.train("training_neg.txt", "neg")
    
    print("\n*******Multinomial Bag of Words Results*******\n")
    print("#### POSITIVE TEST ####")
    classifier.evaluateMultinomialNaiveBoW("test_pos_public.txt")
    print("\n#### NEGATIVE TEST ####")
    classifier.evaluateMultinomialNaiveBoW("test_neg_public.txt")

    print("*******Gaussian Bag of Words Results*******\n")
    print("#### POSITIVE TEST ####")
    classifier.evaluateGaussianBoW("test_pos_public.txt")
    print("\n#### NEGATIVE TEST ####")
    classifier.evaluateGaussianBoW("test_neg_public.txt")

    print("\n*******Gaussian Tf-Idf Results*******\n")
    print("#### POSITIVE TEST ####")
    classifier.evaluateGaussianTFIDF("test_pos_public.txt")
    print("\n#### NEGATIVE TEST ####")
    classifier.evaluateGaussianTFIDF("test_neg_public.txt")
