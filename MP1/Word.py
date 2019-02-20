from numpy import zeros
from numpy import log

class Word:
    def __init__(self, name = "", count = 0, documents = 0, numberOfOtherWordsInReview = 0, totalReviews = 0, reviewIndex = 0):
        self.name = name
        self.count = count
        self.documents = documents
        self.reviewIndex = reviewIndex
        self.statsList = zeros(totalReviews)
        self.statsList[reviewIndex] = count
        self.statsListTotal = zeros(totalReviews)
        self.statsListTotal[reviewIndex] = log(float(self.statsList[reviewIndex])/numberOfOtherWordsInReview) + log(float(totalReviews)/self.documents)


    def __str__(self):
        return ("{\n""name = " + self.name + "\n" + "count = " + str(self.count) + "\n" + "documents = " + str(self.documents) + "\n}\n")

    def __eq__(self, other):
        return self.getName() == other.getName()

    def __ne__(self, other):
        return self.getName() != other.getName()

    def __hash__(self):
        return hash(self.name)

    def update(self, other):
        self.count = self.count + other.count
        self.statsList[other.reviewIndex] = other.count
        self.statsListTotal[other.reviewIndex] = other.statsListTotal[other.reviewIndex]

    def getName(self):
        return self.name
        