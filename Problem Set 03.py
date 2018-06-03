########################
# Problem Set 03
########################


##############################
#Part 01 - RAdiation Exposure#
##############################

def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.

    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to
      between start and stop times.
    '''
    time=start
    totalRad = 0.0
    while time < stop:
        totalRad = totalRad + (f(time)*step)
        time = time + step
    return totalRad

##################################################################################
##################################################################################

#Since this Problem set is a full hangman game, and the exercises before the final 
#are just creating the functions you will end up calling from the main script
#I'll just post the hangman.py the complete code you can play with
#solutions will be posted not earlier than Sep 17, 2015 at 23:30 UTC, which is the official deadline

#Solution Follows

# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "D:\Google Drive\MITx\hangman\words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    count = 0
    for i in secretWord:
        for j in lettersGuessed:
            if i == j:
                count += 1
                break
    if count == len(secretWord):
        test = True
    else:
        test = False
    return test


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    temp = list(secretWord)
    temp2 =[]
    for i in secretWord:
        if i not in lettersGuessed:
            temp2.append(i)

    for i in range(len(secretWord)):
        for j in range(len(temp2)):
            if temp[i] == temp2[j]:
                temp[i] = ' _ '
    return ''.join(temp)


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    allletters = list(string.ascii_lowercase)
    for i in lettersGuessed:
        if i in allletters:
            allletters.remove(i)
    return ''.join(allletters)

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    lettersGuessed = ['']
    mistakesMade = 0
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is ", len(secretWord)," letters long."
    while mistakesMade < 8:
        flag = 0
        print "------------"
        print "You have ", 8-mistakesMade, "guesses left"
        print "Available Letters: ", getAvailableLetters(lettersGuessed)
        letter = raw_input("Please guess a letter: ")
        if letter in lettersGuessed:
            print "Oops! You've already guessed that letter: ", getGuessedWord(secretWord,lettersGuessed)
            flag = 1
        lettersGuessed.append(letter)
        if isWordGuessed(secretWord,lettersGuessed) == True:
            print "Good guess: ", getGuessedWord(secretWord,lettersGuessed)
            print "------------"
            print "Congratulations, you won!"
            break
        if letter in secretWord and flag == 0:
            print "Good guess: ", getGuessedWord(secretWord,lettersGuessed)
        elif letter not in secretWord and flag == 0:
            print "Oops! That letter is not in my word: ", getGuessedWord(secretWord,lettersGuessed)
            mistakesMade += 1
    if isWordGuessed(secretWord,lettersGuessed) == False:
        print "-----------"
        print "Sorry, you ran out of guesses. The word was ", secretWord, "."


        # if lettersGuessed not in secretWord:
        #     print "Oops! That letter is not in my word: ", getGuessedWord(secretWord, lettersGuessed)
        # else:
        #     print "Good guess: ", getGuessedWord(secretWord, lettersGuessed)
        #mistakesMade += 1


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)


