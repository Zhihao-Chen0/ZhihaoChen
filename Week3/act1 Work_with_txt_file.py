# File handling class
class file_handler:
    def __init__(self, file_path):
        self.file_path = file_path

# define read file
    def read_file(self):
        with open(self.file_path, 'r') as file:
            content = file.read()
            print("File read successfully.")
            print("Content of the file:")
            print(content)
            return content

# define write file
    def write_file(self, content):
        with open(self.file_path, 'w') as file:
            content = content + "\nThis is a new line added to the file."
            file.write(content)
            print("File written successfully.")

# define append file
    def append_file(self, content):
        with open(self.file_path, 'a') as file:
            file.write(content)
            print("File appended successfully.")

# main function
def main():
   file_path = "Week3/demo.txt"
   file_read_write = file_handler(file_path)

# read file
   content = file_read_write.read_file()
   print(content)

# write file
   new_content = "This is some new content to write to the file."
   file_read_write.write_file(new_content)

# append file
   file_read_write.append_file("\nThis is an appended line.")

if __name__ == "__main__":
    main()