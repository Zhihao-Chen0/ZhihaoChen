#Develop a project using class and methods to get a sentence from user input and find the number of words in it. Share your GitHub link at the end.

# Word Counter Class
class WordCounter:
    def __init__(self, sentence):
        self.sentence = sentence

# Method to count words in the sentence
    def count_words(self):
        return len(self.sentence.split())

# Main function to run the word counter
def main():
    sentence = input("Please input a sentence: ")
    word_counter = WordCounter(sentence)
    print("The number of words in the sentence is:", word_counter.count_words())

# Entry point for the program
if __name__ == "__main__":
    main()