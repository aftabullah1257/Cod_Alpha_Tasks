import random

def hangman():
    # Predefined list of 5 words
    words = ["python", "intern", "alpha", "coding", "script"]
    word = random.choice(words)
    guessed_letters = []
    attempts = 6  # Limit incorrect guesses to 6

    print("Welcome to Hangman!")

    while attempts > 0:
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"
        
        print(f"\nWord: {display_word}")
        print(f"Attempts left: {attempts}")

        if "_" not in display_word:
            print("Congratulations! You won!")
            break

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that.")
        elif guess in word:
            print("Good job!")
            guessed_letters.append(guess)
        else:
            print("Wrong guess.")
            attempts -= 1
            guessed_letters.append(guess)

    if attempts == 0:
        print(f"Game Over! The word was: {word}")

hangman()