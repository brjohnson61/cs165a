import Word
import Term_Frequency_Inverse_Document_Frequency

class Bag_of_Words:

    def __init__(self):
        self.wordList = []
        self.totalDocuments = 0

    def __next__(self):
        return next(self.wordList)

    def __iter__(self):
        return iter(self.wordList)