""" act1_length_calculate.py for analyzing text length and counting uppercase letters. 
1. Calculate the length of a string or list of strings.
2. Count the number of uppercase letters in the string or list of strings."""

class LengthAnalyzer:
    """ Class to analyze the length of strings or lists of strings """
    def __init__(self, text):
        self.text = text

    def get_total_length(self):
        """ Returns the total length of the text """
        if isinstance(self.text, str):
            return len(self.text)
        elif isinstance(self.text, list):
            return sum(len(item) for item in self.text)
        return 0

    def count_uppercase(self):
        """ Counts the number of uppercase letters in the text """
        if isinstance(self.text, str):
            return sum(1 for char in self.text if char.isupper())
        elif isinstance(self.text, list):
            return sum(sum(1 for char in item if char.isupper()) for item in self.text)
        return 0

    def summary(self):
        """ Provides a summary of the analysis """
        return {
            "total_length": self.get_total_length(),
            "uppercase_count": self.count_uppercase()
        }

if __name__ == "__main__":
    analyzer1 = LengthAnalyzer("Hello World!")
    print(analyzer1.summary())
    analyzer2 = LengthAnalyzer(["Hello", "World", "Python3"])
    print(analyzer2.summary())
