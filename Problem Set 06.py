########################
# Problem Set 06
#########################



import string

def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    dict = { }
    if type(shift) == int and shift >= 0 and shift < 26:
        for i in range(len(string.ascii_lowercase)-shift):
            dict[string.ascii_lowercase[i]] = string.ascii_lowercase[i+shift]
            last=i+1
        for i in range(shift):
            dict[string.ascii_lowercase[last+i]] = string.ascii_lowercase[i]
        for i in range(len(string.ascii_uppercase)-shift):
            dict[string.ascii_uppercase[i]] = string.ascii_uppercase[i+shift]
            last=i+1
        for i in range(shift):
            dict[string.ascii_uppercase[last+i]] = string.ascii_uppercase[i]
        return dict
    else:
        return "dumbass"


def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    text2=''
    for letter in text:
        if letter in coder:
            letter = coder[letter]
            text2 += letter
        else:
            text2 += letter
    text = ''.join(text2)
    return text


def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    ### TODO.
    ### HINT: This is a wrapper function.
    return applyCoder(text,buildCoder(shift))


def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    scoremax = 0
    key = 0
    vwcount = 0
    for i in range(0,26,1):
        text2 = applyShift(text,i)
        text2 = text2.split(' ')
        for j in range(len(text2)):
            if isWord(wordList,text2[j]) == True:
                vwcount += 1
        if vwcount > scoremax:
            scoremax = vwcount
            key = i
    return key


def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Once you decrypt the message, be sure to include as a comment
    your decryption of the story.

    returns: string - story in plain text
    """
    text = getStoryString()
    wordList = loadWords()
    bestShift = findBestShift(wordList, text)
    decoded = applyShift(text,bestShift)

    return decoded



