class GrammarStats():

    def __init__(self):
        self._correct = 0
        self._incorrect = 0
    
    def check(self, text):
        if text.strip() == "":
            raise Exception("No text provided.")
        if (text[0].isalpha() and text[0] == text[0].upper() and text[-1] in ["!", ".", "?"]):
            self._correct += 1 
        else:
            self._incorrect += 1
        return text[0].isalpha() and text[0] == text[0].upper() and text[-1] in ["!", ".", "?"]

    def percentage_good(self):
        if (self._incorrect + self._correct) == 0:
            raise Exception("Cannot calculate a percentage of checked texts when no texts provided.")
        return int(self._correct/(self._incorrect + self._correct) * 100)