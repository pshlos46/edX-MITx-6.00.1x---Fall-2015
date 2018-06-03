########################
# Problem Set 04
#########################



def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    score = 0
    for i in range(0,len(word)):
        score += SCRABBLE_LETTER_VALUES[word[i]]
    score *= len(word)
    if len(word) == n:
        score += 50
    return score


def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    handCopy = hand.copy()
    for i in range(len(word)):
        if word[i] in handCopy.keys():
            handCopy[word[i]] -= 1
        if handCopy[word[i]] == 0:
            handCopy.pop(word[i])
    return handCopy


def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    handCopy = hand.copy()
    if word in wordList:
        for i in range(len(word)):
            if word[i] in handCopy.keys():
                handCopy[word[i]] -= 1
            else:
                return False
        if any(i < 0 for i in handCopy.values()):
            return False
        else:
            return True
    else:
        return False


def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    temp=0
    for key in hand.keys(): 
        if hand[key] <= 0:
            del hand[key]
        else:
            temp += hand[key]-1
    return len(hand)+temp


def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Keep track of the total score
    score = 0
    #score += getWordScore(word,n)
    # As long as there are still letters left in the hand:
    while calculateHandlen(hand) > 0:
        # Display the hand
        print "Current Hand: ", 
        displayHand(hand)
        # Ask user for input
        word = raw_input("Enter word, or a \".\" to indicate that you are finished: ")
        # If the input is a single period:
        if word == ".":
            # End the game (break out of the loop)
            break
        # Otherwise (the input is not a single period):
        else:
            # If the word is not valid:
            if isValidWord(word, hand, wordList) == False:
                # Reject invalid word (print a message followed by a blank line)
                print "Invalid word, please try again."
                print
            # Otherwise (the word is valid):
            else:
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                score += getWordScore(word,n)
                print '"' + word + '"' + " earned ", getWordScore(word,n), " points. Total: ", score, "points"
                print
                # Update the hand 
                hand = updateHand(hand,word)
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    if word == ".":
        print "Goodbye! Total score: ", score, " points."
    else:
        print "Run out of letters. Total score: ", score, " points."


def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1
    """
    helper1 = True
    hand = ''
    usrInp = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
    while helper1 == True: #usrInp == 'e' or usrInp == 'r' or usrInp == 'n':
        if usrInp == 'n':
            hand = dealHand(HAND_SIZE)
            playHand(hand,wordList,HAND_SIZE)
            usrInp = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        elif usrInp == 'r':
            if hand != '':
                playHand(hand,wordList,HAND_SIZE)
                usrInp = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
            else:
                print "You have not played a hand yet. Please play a new hand first!"
                print
                usrInp = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        elif usrInp == 'e':
            break
        else:
            print "Invalid command."
            usrInp = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")


def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """

    # Create a new variable to store the maximum score seen so far (initially 0)
    maxScore = 0
    # Create a new variable to store the best word seen so far (initially None)  
    maxWord = None
    # For each word in the wordList
    for word in wordList:
        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        helper1 = isValidWord(word, hand, wordList)
        # handCopy = hand.copy()
        # for i in range(len(word)):
        #     if word[i] in handCopy.keys():
        #         handCopy[word[i]] -= 1
        #     else:
        #         helper1 = False
        # if any(i < 0 for i in handCopy.values()):
        #     helper1 = False
        # else:
        #     helper1 = True
            # Find out how much making that word is worth
        if helper1 == True:
            score = getWordScore(word, n)
            # If the score for that word is higher than your best score
            if score > maxScore:
                # Update your best score, and best word accordingly
                maxScore = score
                maxWord = word
    # return the best word you found.
    print maxWord


def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """

    # Create a new variable to store the maximum score seen so far (initially 0)
    maxScore = 0
    # Create a new variable to store the best word seen so far (initially None)  
    maxWord = None
    # For each word in the wordList
    for word in wordList:
        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        helper1 = isValidWord(word, hand, wordList)
        # handCopy = hand.copy()
        # for i in range(len(word)):
        #     if word[i] in handCopy.keys():
        #         handCopy[word[i]] -= 1
        #     else:
        #         helper1 = False
        # if any(i < 0 for i in handCopy.values()):
        #     helper1 = False
        # else:
        #     helper1 = True
            # Find out how much making that word is worth
        if helper1 == True:
            score = getWordScore(word, n)
            # If the score for that word is higher than your best score
            if score > maxScore:
                # Update your best score, and best word accordingly
                maxScore = score
                maxWord = word
    # return the best word you found.
    return maxWord

#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # TO DO ... <-- Remove this comment when you code this function
    # Keep track of the total score
    score = 0
    #score += getWordScore(word,n)
    # As long as there are still letters left in the hand:
    while calculateHandlen(hand) > 0:
        # Display the hand
        print "Current Hand: ",
        displayHand(hand)
        # Ask user for input
        word = compChooseWord(hand, wordList, n)
        # If the input is a single period:
        if word is None:
            # End the game (break out of the loop)
            break
        # Otherwise (the input is not a single period):
        else:
            # If the word is not valid:
            # if isValidWord(word, hand, wordList) == False:
            #     # Reject invalid word (print a message followed by a blank line)
            #     print "Invalid word, please try again."
            #     print
            # # Otherwise (the word is valid):
            # else:
            # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
            score += getWordScore(word, n)
            print '"' + word + '"' + " earned ", getWordScore(word, n), " points. Total: ", score, "points"
            print
            # Update the hand
            hand = updateHand(hand, word)
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    print "Total score: ", score, " points."


def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
          But if no hand was played, output "You have not played a hand yet. 
          Please play a new hand first!"
        
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    helper1 = True
    hand = ''
    usrInp = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
    while helper1 == True: #usrInp == 'e' or usrInp == 'r' or usrInp == 'n':
        if usrInp == 'n':
            usrInp2 = raw_input("Enter u to have yourself play, c to have the computer play: ")
            if usrInp2 == 'u':
                hand = dealHand(HAND_SIZE)
                playHand(hand,wordList,HAND_SIZE)
                usrInp = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
            elif usrInp2 == 'c':
                hand = dealHand(HAND_SIZE)
                compPlayHand(hand,wordList,HAND_SIZE)
                usrInp = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
            else:
                print "Invalid command."
        elif usrInp == 'r':
            if hand != '':
                usrInp2 = raw_input("Enter u to have yourself play, c to have the computer play: ")
                if usrInp2 == 'u':
                    playHand(hand,wordList,HAND_SIZE)
                    usrInp = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
                elif usrInp2 == 'c':
                    compPlayHand(hand,wordList,HAND_SIZE)
                    usrInp = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
                else:
                    print "Invalid command."
            else:
                print "You have not played a hand yet. Please play a new hand first!"
                print
                usrInp = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        elif usrInp == 'e':
            break
        else:
            print "Invalid command."
            usrInp = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")


