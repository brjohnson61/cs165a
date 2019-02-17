
class Term_Frequency_Inverse_Document_Frequency:
    def __init__(self):
        self.tfidf = {}

    def __len__(self):
        return len(self.tfidf)

    def __next__(self):
        return next(self.tfidf)

    def __iter__(self):
        return iter(self.tfidf)

    def __getitem__(self, key):
        return self.tfidf[key]

    def __setitem__(self, key, value):
        self.tfidf[key] = value

    def __delitem__(self, key):
        del self.tfidf[key]

    def __contains__(self, item):
        if(item in self.tfidf):
            return True
        else:
            return False