import random
from hangman_words import word_list  # Ensure hangman_words.py exists in the same directory
from hangman_art import logo, stages  # Ensure hangman_art.py exists in the same directory

# Print the Hangman logo
print(logo)

# Choose a random word from the word list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Debugging helper to reveal the chosen word (remove in production)
# print(f"Pssst, the solution is {chosen_word}.")

# Initialize variables
end_of_game = False
lives = 6
display = ["_" for _ in range(word_length)]  # Create blanks for the word
guessed_letters = []  # Track guessed letters

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Check if the user already guessed the letter
    if guess in guessed_letters:
        print(f"You've already guessed '{guess}'. Try another letter.")
        continue
    else:
        guessed_letters.append(guess)

    # Check if the guessed letter is in the word
    if guess in chosen_word:
        for position in range(word_length):
            if chosen_word[position] == guess:
                display[position] = guess
    else:
        print(f"You guessed '{guess}', which is not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose! The word was '{chosen_word}'.")

    # Display the current progress
    print(f"{' '.join(display)}")

    # Check if the user has guessed all letters
    if "_" not in display:
        end_of_game = True
        print("You win!")

    # Display the hangman stage
    print(stages[lives])
