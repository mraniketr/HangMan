from tkinter import *
import random, sys
from typing import List

root =Tk()
# TODO try to load these from a text file
WORD_LIST = [
"lion", "hippopotamus", "zebra", "leopard", "elephant", "jackal", "sealion", "bluewhale",
 "monkey", "dog", "cat", "camel", "girrafe", "dinosaur", "saket"
           ]



GUESS_WORD = []
SECRET_WORD = random.choice(WORD_LIST) # lets randomize single word from the list
LENGTH_WORD = len(SECRET_WORD)
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
letter_storage = []

# Utility functions

def print_word_to_guess(letters: List) -> None:
    """Utility function to print the current word to guess"""
    m2=str("Word to guess: {0}".format(" ".join(letters)))
    l3 = Label(root, text=m2)
    l3.grid(row=3, column=0, columnspan=2)


def print_guesses_taken(current: int, total: int) -> None:
    """Prints how many chances the player has used"""
    m1=str("You are on guess {0}/{1}.".format(current, total))
    l2=Label(root,text=m1)
    l2.grid(row=4, column=0, columnspan=2)


def prepare_secret_word() -> None:
    """Prepare secret word and inform user of it"""
    for character in SECRET_WORD: # printing blanks for each letter in secret word
        GUESS_WORD.append("-")
    m4=("Ok, so the word You need to guess has", LENGTH_WORD, "characters and is a name of an animal")
    m5=str("Be aware that You can enter only 1 letter from a-z\n\n")
    l4 = Label(root, text=m4)
    l4.grid(row=5, column=0, columnspan=2)

    l5 = Label(root, text=m5)
    l5.grid(row=6, column=0, columnspan=2)

    print_word_to_guess(GUESS_WORD)

guess_taken = 1
MAX_GUESS = 5

def guessing() -> None:
    """
    Main game loop to have user guess letters
    and inform them of the results
    """
    global guess_taken
    global MAX_GUESS
    print_guesses_taken(guess_taken, MAX_GUESS)

    guess = str(e1.get())
    if not guess in ALPHABET: #checking input
        m6=str("Enter a letter from a-z ALPHABET")
    elif guess in letter_storage: #checking if letter has been already used
        m6=str("You have already guessed that letter!")
    else:
        letter_storage.append(guess)
        if guess in SECRET_WORD:
            m6=str("You guessed correctly!")
            for i in range(0, LENGTH_WORD):
                if SECRET_WORD[i] == guess:
                    GUESS_WORD[i] = guess
            print_word_to_guess(GUESS_WORD)
            print_guesses_taken(guess_taken, MAX_GUESS)
            if not '-' in GUESS_WORD:
                m6=str("You won! Game Over!")

        else:
            m6=str("The letter is not in the word. Try Again!")
            guess_taken += 1
            print_guesses_taken(guess_taken, MAX_GUESS)
            if guess_taken == 5:
                m6=str(" Sorry Mate, You lost :<! The secret word was {0}".format(SECRET_WORD))
                exit()
    l6 = Label(root, text=m6)
    l6.grid(row=7, column=0, columnspan=2)

prepare_secret_word()


root.title("Hangman")


l1=Label(root,text="Ready, lets start")
e1 = Entry(root, bd=5)

b1=Button(root,text="Enter",command=guessing)

e1.grid(row=1, column=0, columnspan=2)
b1.grid(row=2, column=0, columnspan=2)


mainloop()
