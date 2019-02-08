import Bag_of_Words

class ReviewClassifier:
    
    def __init__(self):
        self.trained = False
        self.bag = Bag_of_Words.Bag_of_Words()

        
    
    def train(self, file, type):
        listOfReviews = self.niceInputFromFile(file)

        for review in listOfReviews:
            for keyword in review:
                if(keyword in bag):
                    #update bag
                    

                else if(keyword not in bag):
                    #add to bag
                
                #update tf-idf




    def evaluate(self, file):
        print("stub!")

    def evaluateAndTrain(self, file):
        print("stub!")

    def niceInputFromFile(self, file):
        listOfParsedReveiws = []
        stopWords = self.getStopWords()
        fileHandle = open(file, "rt")
        for line in fileHandle:
            lineDict = {}
            line = line.lower()
            line = line.replace(",", "")
            line = line.replace("/", " ")
            line = line.replace("-", " ")
            line = line.replace("?", "")
            line = line.replace("!", "")
            line = line.replace("<br", "")
            line = line.replace("<", "")
            line = line.replace(">", "")
            line = line.replace("'s", "")
            line = line.replace("{", "")
            line = line.replace("}", "")
            line = line.replace("[", "")
            line = line.replace("]", "")
            line = line.replace("*", "")
            line = line.replace("|", "")
            line = line.replace("$", "")
            line = line.replace("_", "")
            line = line.replace("^", "")
            line = line.replace("&", "")
            line = line.replace("(", "")
            line = line.replace(")", "")
            line = line.replace("{", "")
            line = line.replace("+", "")
            line = line.replace("=", "")
            line = line.replace("@", "")
            line = line.replace("\"", "")
            line = line.replace("\'", "")
            line = line.replace(".", "")

            lineList = line.split()
            lineSet = set(lineList)
            

            for uniqueWord in lineSet:
                if(uniqueWord not in stopWords):
                    lineDict[uniqueWord] = lineList.count(uniqueWord)

            listOfParsedReveiws.append(lineDict)

        #print(listOfParsedReveiws[10]))


    def getStopWords(self):
        file = open("stop_words.txt", "rt")
        stopWordsList = []

        for stopWord in file:
            stopWordsList.append(stopWord.rstrip("\n"))
        
        return stopWordsList
        

if __name__ == "__main__":
    classifier = ReviewClassifier()
    classifier.niceInputFromFile("training_pos.txt")

