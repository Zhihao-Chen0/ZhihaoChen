class StringManipulator:
    def __init__(self, text):
        self.text = text

    def find_character(self, char):
        return self.text.lower().find(char.lower())  # Ensure case-insensitive search

    def measure_length(self):
        return len(self.text)
    
    def convert_to_uppercase(self):
        return self.text.upper()
    
def main():
    name = StringManipulator("example")

    while True:
        user_input = input("Enter a word(letter only): ").strip()

        if not user_input:
            print("Empty input. Please enter a valid word.")
            continue
        if not user_input.isalpha():
            print("Invalid input. Letters only.")
            continue

        name.text = user_input
        break

    print("The number of 'e':", name.find_character("e"))
    print("Word length:", name.measure_length())
    print("Uppercase:", name.convert_to_uppercase())

if __name__ == "__main__":
    main()
