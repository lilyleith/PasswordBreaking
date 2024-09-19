import hashlib
import time
import numpy as np


# this function returns 1 if there is a double letter combination in a word, and 0 if there is not
def doubleLetter(word):
    currLetter = ""
    # look at all adjacent letters, check if they are the same
    for index in range(1, len(word)):
        if word[index - 1] == word[index]:
            return 1
        else:
            continue
    return 0

# translate the one letter words using the current mapping
def translateOneLetterWords(currentMapping, oneLetterWords):
    # can directly key in because there is only one unique one letter word "b"
    oneLetterWords["b"] = currentMapping["b"]
    return oneLetterWords

# translate the wordDict using currentMapping 
def translateWordDict(currentMapping, wordDict):
    
    for encryptedWord in wordDict.keys():
        # split the word into a list so that we can translate each letter independently
        # stops us from updating already translated letters to incorrect mappings
        letterList = [letter for letter in encryptedWord]
        index = 0
        # iterate through each letter
        for letter in letterList:
            # if the letter defined in the mapping, then replace it with its mapping
            
            if letter in currentMapping.keys():
                
                letterList[index] = currentMapping[letter]
            # update the index
            index += 1
        
        # store translation in the wordList dictionary
        wordDict[encryptedWord] = "".join(letterList)
    # return the wordList
    return wordDict

# creates a fully translated list of the encryptedWords passed using the currentMapping
def translateWordList(currentMapping, encryptedWords):
    wordList = []
    for word in encryptedWords:
        # split the word into a list so that we can translate each letter independently
        # stops us from updating already translated letters to incorrect mappings
        letterList = [letter for letter in word]
        index = 0
        # iterate through each letter
        for letter in letterList:
            # if the letter defined in the mapping, then replace it with its mapping
            if letter in currentMapping.keys():
                letterList[index] = currentMapping[letter]
            # update the index
            index += 1
        wordList.append("".join(letterList))
    return wordList
    
        
# create and return a dict with keys that are unique words of len length from the encrypted text
# the dict is ordered by the frequency with which the words appear in the text
def createWordDictByLength(encryptedWords, length):
    # create dict
    wordList = {}
    for word in encryptedWords:
        if len(word) == length:
            # we will start by making the values in the dict the frequency of the word so that we can order 
            # the list. Later we change the values to translations in another function.
            if word not in wordList:
                wordList[word] = 1
            else:
                wordList[word] +=1
    # sort and return
    wordList = dict(sorted(wordList.items(), key = lambda item:item[1], reverse = True))
    return wordList
            
            

# return a dictionary mapping each letter to the number of times it appears in the encrypted text
def countLetters(encryptedWords):
    # create letterCounts dictionary
    letterCounts = {}
    # iterate through each word
    for word in encryptedWords:
        # iterate through each letter in the word
        for letter in word:
            # if not in the dictionary, then initiate value to 1
            if letter not in letterCounts:
                letterCounts[letter] = 1
            # if in the dict, increment the value by 1
            else:
                letterCounts[letter] += 1
    # order the letters in descending order of frequency and return as a dict
    letterCounts = dict(sorted(letterCounts.items(), key = lambda item:item[1], reverse = True))
    return letterCounts

# main function
if __name__ == '__main__':
    
    # a list of the encrypted words in the encryption.txt file stripped of punctuation
    encrytedWords = []

    # a dictionary mapping each encrypted word in the file to its translation, including punctuation for context
    fullTranslation = []
    encryptedWordsWithPunctuation = []

    # first step in the process was getting a list of all the words stripped of punctuation 
    with open("encrypted.txt") as encrypted:
        line = encrypted.readline()
        # add the word with punctuation to the fullTranslation dictionary
        # remove periods, semicolons, apostrophes and commas from each word and store in encrypted word list
        for word in line.split(" "):
            encryptedWordsWithPunctuation.append(word)
            word = word.replace(",","")
            word = word.replace(".","")
            word = word.replace("'","")
            word = word.replace(";","")
            encrytedWords.append(word)
    
    # took inventory of all the one letter words, two letter words, three letter words, and four letter words
    
    oneLetterWords = createWordDictByLength(encrytedWords, 1)
    twoLetterWords = createWordDictByLength(encrytedWords, 2)
    threeLetterWords = createWordDictByLength(encrytedWords, 3)
    fourLetterWords = createWordDictByLength(encrytedWords, 4)

    # created dict of all the double letter words: 
    doubleLetterWords = {}
    for word in encrytedWords:
        if doubleLetter(word):
            doubleLetterWords[word] = ""

    # printed out the dicts I just created. commented out for submission

    # print("One letter words: ", list(oneLetterWords.keys()))
    # print("Two letter words: ", list(twoLetterWords.keys()))
    # print("Three letter words: ", list(threeLetterWords.keys()))
    # print("Four letter words: ", list(fourLetterWords.keys()))
    # print("Double letter words: ", list(fourLetterWords.keys()))

    # after looking at the results of the print statements, I chose my first mapping.
    # current mapping holds the mapping that I'm testing out. In the beginning of working on this file,
    # currentMapping contained only a few mappings based on findings for each round.
    currentMapping = {"b":"a", "f":"e", "s":"t", "j":"o", "m":"h", "p":"l", "v":"n", "l":"d", "d":"i", "t":"s", "w":"c", "n":"p", "u":"w", "r":"b", "k":"y", "e":"u", "g":"m", "q":"f", "c":"r", "i":"g", "x":"v", "y":"k", "h":"q", "o":"x"}
    # set letter mapping for one letter words 
    oneLetterWords = translateOneLetterWords(currentMapping, oneLetterWords)

    # now I test the current mapping against the two, three, four and double letter words to find any pattern

    # starting with the two letter words
    twoLetterWords = translateWordDict(currentMapping, twoLetterWords)

    # and then double letter words
    doubleLetterWords = translateWordDict(currentMapping, doubleLetterWords)

    # three letter words
    threeLetterWords = translateWordDict(currentMapping, threeLetterWords)

    # four letter words 
    fourLetterWords = translateWordDict(currentMapping, fourLetterWords)

    # translate the entire file
    fullTranslation = translateWordList(currentMapping, encryptedWordsWithPunctuation)

    # count the instances of each letter in the encrypted text to determine which might map to 
    # uncommon english letters
    letterCounts = countLetters(encrytedWords)

    fullTranslation.append("\n")

    # now I print these dicts and see if I can sense any pattern or success emerging
    # print statements are commented out for submission of analysis.py

    # print("Translated one letter words:\n", oneLetterWords)
    # print("Translated two letter words:\n", twoLetterWords)
    # print("Translated three letter words:\n", threeLetterWords)
    # print("Translated four letter words:\n", fourLetterWords)
    # print("Translated double letter words:\n", doubleLetterWords)
    # print()
    # print("full translated text:\n", " ".join(fullTranslation))
    # print("Letters ordered by decreasing frequency: ", letterCounts.keys())

    # after printing and looking at the dicts I updated the mapping and ran the program again

    # I have found the full translation of the ciphertext. write it into a file for submission. 
    # commented out for submission
    # plain = open("plaintext.txt", "w")
    # plaintext = " ".join(fullTranslation)
    # plain.write(plaintext.strip(" "))
    # plain.close()




