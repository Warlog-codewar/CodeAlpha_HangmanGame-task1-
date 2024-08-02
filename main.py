import random

def choose_word():
    words = ["callipygian", "mango", "marshmallow", "doodle", "chiggu"]
    return random.choice(words)
def display_word(word, letters_guessed):
    display = ""
    for letter in word:
        if letter in letters_guessed:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    print( "WELCOME  TO HANGMAN !!CHAD ")
    print("ARE   YOU    READYYYY ????")
    print("Let's   Start   The Game")
    print("You have only 5 tries, nothing more, nothing less")

    word = choose_word()
    letters_guessed = []
    incorrect_guess = 0
    max_incorrect_guess = 5

    while incorrect_guess < max_incorrect_guess:
        print("Word:", display_word(word, letters_guessed))
        guess = input("Guess a letter: ").lower()

        if guess in letters_guessed:
            print("You already guessed that letter, try another one dude.")
        elif guess in word:
            print("Hurrah! Yeahhh chad you guessed it correctly.")
            letters_guessed.append(guess)
        else:
            print("Oohhh ohh ! You guessed wrong one .")
            incorrect_guess += 1

        if set(word) <= set(letters_guessed):
            print("Congratulations dude! You guessed the word:", word)
            break

        if incorrect_guess >= max_incorrect_guess:
            print("You ran out of guesses. The word was:", word)

hangman()