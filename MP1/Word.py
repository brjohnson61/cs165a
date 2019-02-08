import Term_Frequency_Inverse_Document_Frequency

class Word:
    """Word Class:
    Members:
    name - (string) the string representing the word
    count - (int) the number of times the word has been seen"""
    def __init__(self, name):
        self.name = name
        self.count = 0
        self.tf_idf = None

    def update(self, count):
        self.count = self.count + count

