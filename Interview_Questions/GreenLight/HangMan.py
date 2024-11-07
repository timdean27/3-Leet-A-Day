import random

# List of words to choose from
word_list = ["python", "hangman", "computer", "programming", "developer"]
word = random.choice(word_list)  # Randomly select a word from the list
guessed_word = ["_"] * len(word)  # Start with underscores for each letter
incorrect_guesses = []
max_attempts = 6  # Number of incorrect guesses allowed
attempts = 0


while attempts < max_attempts:

    # Ask player for a guess
    guess = input("Guess a letter: ").lower()

    # Check if the input is valid (single letter)
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Please enter a single letter.")
        continue
    #Check if letter is guessed
    if guess in guessed_word or guess in incorrect_guesses:
        print(f"You've already guessed '{guess}'. Try a different letter.")
        continue

    # Check if the guess is in the word
    if guess in word:
        print(f"Good guess! '{guess}' is in the word.")
        # Update the guessed_word list with the correct guess
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
        print(guessed_word)
    else:
        print(f"Sorry, '{guess}' is not in the word.")
        incorrect_guesses.append(guess)
        attempts += 1

    # Check if the player has guessed the word
    if "_" not in guessed_word:
        print("\nCongratulations! You've guessed the word:", word)
        break

# check if player is out of turns 
if attempts == max_attempts:
    print("\nGame over! You've run out of attempts.")
    print(f"The word was: {word}")