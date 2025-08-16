# File handling class
class FileHandler:
    def __init__(self, file_path):
        self.file_path = file_path

# define the word count function
    def word_count(self):
        with open(self.file_path, 'r') as file:
            content = file.read()
            words = content.split()
            return len(words)

# main function
def main():
    file_path = "demo.txt"
    count_word = FileHandler(file_path)
    print("Word count:", count_word.word_count())

# entry point
if __name__ == "__main__":
    main()
