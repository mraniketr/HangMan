def guessing() -> None:
    """
    Main game loop to have user guess letters
    and inform them of the results
    """
    guess_taken = 1
    MAX_GUESS = 5
    print_guesses_taken(guess_taken, MAX_GUESS)

    while guess_taken < MAX_GUESS:
        guess = str(e1.get())
        if not guess in ALPHABET: #checking input
            print("Enter a letter from a-z ALPHABET")
            print(guess)
        elif guess in letter_storage: #checking if letter has been already used
            print("You have already guessed that letter!")
        else:
            letter_storage.append(guess)
            if guess in SECRET_WORD:
                print("You guessed correctly!")
                for i in range(0, LENGTH_WORD):
                    if SECRET_WORD[i] == guess:
                        GUESS_WORD[i] = guess
                print_word_to_guess(GUESS_WORD)
                print_guesses_taken(guess_taken, MAX_GUESS)
                if not '-' in GUESS_WORD:
                    print("You won!")
                    print("Game Over!")
                    break
            else:
                print("The letter is not in the word. Try Again!")
                guess_taken += 1
                print_guesses_taken(guess_taken, MAX_GUESS)
                if guess_taken == 5:
                    print(" Sorry Mate, You lost :<! The secret word was {0}".format(SECRET_WORD))
