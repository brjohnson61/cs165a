import Term_Frequency_Inverse_Document_Frequency
from math import log1p

class Word:
    def __init__(self, name = "", count = 0, documents = 0):
        self.name = name
        self.count = count
        self.documents = documents

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
        self.documents = self.documents + other.documents

    def getTF(self):
        return (log1p(self.count/self.documents))
    
    def getName(self):
        return self.name
        