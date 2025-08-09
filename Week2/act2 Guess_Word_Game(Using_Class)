# Guess the Word Game
import random

class Word:
    def __init__(self, word):
        self.word = word
        self.blanked_list = ["_"] * len(word)
        self.guessed_letters = set()

# Function to get a random word
def get_random_word():
    words = ["table", "monkey", "computer", "science", "bottle", "planet", "telephone","bridge", "keyboard", "postcard"]
    return random.choice(words)

# Function to get the blanked version of the word
def get_blanked_word(word):
    positions = list(range(len(word)))
    blanked_list = ["_"] * len(word)
    return blanked_list, positions

def play_game():
    lives = 6
    word = get_random_word()
    blanked_list, positions = get_blanked_word(word)

    # Marked repeated letters
    guessed_letters = set()

    while lives > 0 and "_" in blanked_list:
        print("\nGuess the word. You have", lives, "lives left.")
        print("\nCurrent word:", "".join(blanked_list))

    # Avoid wrong guesses
        while True:
            guess = input("Enter your guess (a single letter): ").strip().lower()
            if not guess:
                print("Please input a letter.")
                continue
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input. Please enter a single letter.")
                continue
            if guess in guessed_letters:
                print("You have already guessed that letter. Try again.")
                continue
            break

        guessed_letters.add(guess)

        # Check if the guess is correct
        hit = False
        for i in positions:
            if word[i].lower() == guess:
                blanked_list[i] = word[i]
                hit = True
        if hit:
            print("Current word:", "".join(blanked_list))
        else:
            lives -= 1
            print("Incorrect! You have", lives, "lives left.")

    if "_" not in blanked_list:
        print("Congratulations! You've guessed the word:", word)
    else:
        print("Game over! The word was:", word) 

# Main entry point
if __name__ == "__main__":
    while True:
        play_game()
        if input("Do you want to play again? (yes/no): ").strip().lower() != "yes":
            print("Thank you for playing!")
            break
