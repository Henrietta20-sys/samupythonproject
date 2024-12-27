import random

# Word list for the game
WORDS = [
    "python", "hangman", "programming", "computer", 
    "developer", "software", "algorithm", "function"
]

# Function to choose a random word
def get_random_word(word_list):
    return random.choice(word_list)


# Function to display the current state of the word
def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])


# Function to play Hangman
def play_hangman():
    print("Welcome to Hangman!")
    word_to_guess = get_random_word(WORDS)
    guessed_letters = set()
    attempts_left = 6  # Maximum number of wrong attempts

    while attempts_left > 0:
        print("\n" + display_word(word_to_guess, guessed_letters))
        print(f"Attempts left: {attempts_left}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try a different letter.")
            continue

        guessed_letters.add(guess)

        if guess in word_to_guess:
            print(f"Good job! '{guess}' is in the word.")
            if all(letter in guessed_letters for letter in word_to_guess):
                print(f"\nCongratulations! You guessed the word: {word_to_guess}")
                break
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            attempts_left -= 1
    else:
        print(f"\nGame Over! The word was: {word_to_guess}")


if __name__ == "__main__":
    play_hangman()
