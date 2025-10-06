""" act2_length_calculate_enhance.py for analyzing text length and counting uppercase letters. 
1. Calculate the length of a string or list of strings.
2. Count the number of uppercase letters in the string or list of strings.
3. Count the number of digits in the string or list of strings.
4. Count the number of special characters in the string or list of strings."""

class LengthAnalyzer:
    """ Class to analyze the length of strings or lists of strings """
    def __init__(self, text):
        self.text = text

    def get_total_length(self):
        """ Returns the total length of the text """
        if isinstance(self.text, str):
            return len(self.text)
        if isinstance(self.text, list):
            return sum(len(item) for item in self.text)
        return 0

    def count_uppercase(self):
        """ Counts the number of uppercase letters in the text """
        if isinstance(self.text, str):
            return sum(1 for char in self.text if char.isupper())
        if isinstance(self.text, list):
            return sum(sum(1 for char in item if char.isupper()) for item in self.text)
        return 0
    
    def count_digits(self):
        """ Counts the number of digits in the text """
        if isinstance(self.text, str):
            return sum(1 for char in self.text if char.isdigit())
        if isinstance(self.text, list):
            return sum(sum(1 for char in item if char.isdigit()) for item in self.text)
        return 0

    def count_special_characters(self):
        """ Counts the number of special characters in the text """
        special_characters = "!@#$%^&*()-+?_=,<>/"
        if isinstance(self.text, str):
            return sum(1 for char in self.text if char in special_characters)
        if isinstance(self.text, list):
            return sum(sum(1 for char in item if char in special_characters) for item in self.text)
        return 0

    def summary(self):
        """ Provides a summary of the analysis """
        return {
            "total_length": self.get_total_length(),
            "uppercase_count": self.count_uppercase(),
            "digit_count": self.count_digits(),
            "special_character_count": self.count_special_characters()
        }

if __name__ == "__main__":
    analyzer1 = LengthAnalyzer("Hello World!")
    print(analyzer1.summary())
    analyzer2 = LengthAnalyzer(["Hello", "World", "Python3"])
    print(analyzer2.summary())
    analyzer3 = LengthAnalyzer("Hello World! 123")
    print(analyzer3.summary())
    analyzer4 = LengthAnalyzer(["Hello!", "World@2024", "Python3#"])
    print(analyzer4.summary())