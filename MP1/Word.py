import Term_Frequency_Inverse_Document_Frequency
from math import log1p

class Word:
    """Word Class:
    Members:
    name - (string) the string representing the word
    count - (int) the number of times the word has been seen"""
    def __init__(self, name = "", count = 0, documents = 0):
        self.name = name
        self.count = count
        self.documents = documents

    def __eq__(self, other):
        return self.name == other.name

    def __eq__(self, other):
        return self.name == other

    def __ne__(self, other):
        return self.name != other.name

    def __ne__(self, other):
        return self.name != other.name

    def __hash__(self):
        return hash(self.name)

    def update(self, other):
        self.count = self.count + other.count
        self.documents = self.documents + other.documents

    def getTF(self):
        return (log1p(self.count/self.documents))
        

