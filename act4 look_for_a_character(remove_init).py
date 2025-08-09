class StringManipulator:
    def find_character(self, char):
        return self.text.find(char)

    def measure_length(self):
        return len(self.text)
    
    def convert_to_uppercase(self):
        return self.text.upper()
    
def main():
    name = StringManipulator()
    name.text = "example"

    print(name.find_character("e"))
    print(name.measure_length())
    print(name.convert_to_uppercase())

if __name__ == "__main__":
    main()
