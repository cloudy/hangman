#!/usr/bin/env python3
#purpose: simple implementation of a terminal-based hangman game
#author: Joe Cloud: git@joe.cloud

import getpass

def main():
    num_guess = 6 # Number of guesses that a player can guess incorrectly
    letters_found = 0 # count of letters found out of a word of specified length
    secret = getpass.getpass("Enter the desired word: ").lower()
    secret_length = len(secret) # Length of the word selected
    prev_letters = [] # list of letters previously used

    while num_guess > 0 and letters_found != secret_length:
        printWordStatus(secret, prev_letters)
        guess = getGuess(prev_letters)
        
        matches = secret.count(guess)
        letters_found += matches
        if matches == 0:
            print("Sorry! The letter was not found.")
            num_guess -= 1
        else:
            print("Good! This letter is used %d times." % matches)

        printMan(num_guess)
        prev_letters.append(guess)

    if letters_found == secret_length:
        print("Congratulations! You won.")
    else:
        print("Sorry! You lost. The correct word was %s." % secret)

def printWordStatus(secret, prev_letters):
    print('Word:',end='')
    for letter in secret:
        if letter in prev_letters:
            print(letter,end='')
        else:
            print('-',end='')
    print('')

def getGuess(prev_letters):
    num_letters = 0
    while num_letters != 1:
        guess = input("Guess a letter: ").lower()
        num_letters = len(guess)
        if num_letters != 1:
            print("Only enter one letter!")
        if guess in prev_letters:
            print("Don't enter previous letters!")
            num_letters = 0
    return guess

def hangMan(status):
    head = 'o' if status < 6 else ' '
    left_arm = '\\' if status < 4 else ' '
    torso = '|' if status < 5 else ' '
    right_arm = '/' if status < 3 else ' '
    left_leg = '/' if status < 2 else ' '
    right_leg = '\\' if status < 1 else ' '
    return ([['\u250c', '\u23e4', '\u23e4', '\u23e4', '\u23e4', '\u2510',       ' '],
             [     '|',      ' ',      ' ',      ' ',      ' ',     head,       ' '],
             [     '|',      ' ',      ' ',      ' ', left_arm,    torso, right_arm],
             [     '|',      ' ',      ' ',      ' ',      ' ',    torso,       ' '],
             [     '|',      ' ',      ' ',      ' ', left_leg,      ' ', right_leg],
             ['\u22a5',      ' ',      ' ',      ' ',      ' ',      ' ',       ' ']])

def printMan(status):
    for r in hangMan(status):
        for l in r:
            print(l,end='')
        print('')

if __name__=='__main__':
    main()
