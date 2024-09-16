import hashlib

import time
import numpy as np
from itertools import product
""" Program Flow
- get dictionary into a file reader
- get user names and passwords into a dictionary
- create second dictionary for hashed passwords
- hash passwords FIRST
- initiate list of different hash methods as strings
- 
- 
 """



# # first hash all the passwords and store them in hashedPasswords
# for userPassword in shadow:
#     user = userPassword.split(":")[0]
#     password = userPassword.split(":")[1]


# passwords = {}

# with open("shadow", "r") as f2:
#     for userPassword in f2:
#         userPass = userPassword.split(":")
#         passwords[userPass[0]] = userPass[1]
#         hashedPasswords[userPass[0]] = ""
    


# for user in passwords.keys():
#     pws = passwords[user]
#     for h in hashes:
#         hash = hashlib.new(h)
#         hash.update(pws)
#         hashedPasswords[user] = hash.hexdigest()
#         """ for fOut in outFiles:
#             with open(fOut,"w") as out:
#                 for word in d:
#                     hash2 = hashlib.new(h)
#                     hash2.update(word.encode())
#                     out.write(hash2.hexdigest() + "\n") """

def md5(plaintext):
    hash = hashlib.new("md5")
    hash.update(plaintext.encode())
    return hash.hexdigest()

def sha1(plaintext):
    hash = hashlib.new("sha1")
    hash.update(plaintext.encode())
    return hash.hexdigest()

def sha224(plaintext):
    hash = hashlib.new("sha224")
    hash.update(plaintext.encode())
    return hash.hexdigest()

def sha256(plaintext):
    hash = hashlib.new("sha256")
    hash.update(plaintext.encode())
    return hash.hexdigest()

def sha384(plaintext):
    hash = hashlib.new("sha384")
    hash.update(plaintext.encode())
    return hash.hexdigest()

def sha512(plaintext):
    hash = hashlib.new("sha512")
    hash.update(plaintext.encode())
    return hash.hexdigest()

def sha3_224(plaintext):
    hash = hashlib.new("sha3_224")
    hash.update(plaintext.encode())
    return hash.hexdigest()

# returns all possible SALT options for the word
def appendSALT(word):
    possibleSALTS = []
    for num in range(100000):
        SALT = str(num).zfill(5)
        possibleSALTS.append(word + SALT)
    return possibleSALTS


# find and return all possible caesar translations of a given word
def caesarConversion(word):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    # list for all possible caesar translations
    caesarTranslations = []

    letters = [letter for letter in word]
    for shift in range(1, 26):
        caesar = ["" for i in range(len(word))]
        for index in range(len(word)):
            if letters[index] not in alphabet:
                continue
            newLetterIndex = (alphabet.index(letters[index]) + shift) % 26
            caesar[index] = alphabet[newLetterIndex] 
        caesarTranslations.append("".join(caesar))
    return caesarTranslations



# translate a word into leetspeak
def leetSpeakConversion(word):
# 2 iterations as of right now
    translations = {"a": ["4","@"], "b":["b", "8"], "c":["c", "["], "d":["d", ")"], "e":["3", "&"], "f":["f"], "g":["6", "&"], "h":["h", '#'], "i":["1", "!"], "j":["j"], "k":["k"], "l":["1","!"], "m":["m"],"n":["n"], "o":["0"], "p":["p", "9"], "q":["q"], "r":["r"], "s":["5", "$"], "t":["7", "+"], "u":["u"], "v":["v"], "w":["w"], "x":["x"], "y":["y"], "z":["2"], "q":["9"]}

    # list for all possible leet speak translations of the word
    possibleConversions = []
   
    # iterate through the letters and create a list of each unique letter
    letters = [char for char in word]
    uniqueLetters = []
    for letter in letters:
        if letter not in uniqueLetters:
            uniqueLetters.append(letter)

    # set exponent to 0
    exponent = 0

    # create list of letters with multiple possible translations and letters with just one possible translation, 
    multipleTranslations = []
    singleTranslations = []

    # iterate through each unique letter
    for letter in uniqueLetters:
        # if the letter has a translation in the dict
        if letter in translations.keys():
            # if the letter has multiple translations, then add to multiple translations list
            if len(translations[letter]) > 1:
                exponent += 1
                multipleTranslations.append(letter)
            # if not then add it to the single translations list
            else:
                singleTranslations.append(letter)

    # create a matrix with 2^exponent rows of all binary combinations of (exponent) values
    binaryPossibilities = [list(x) for x in product([0, 1], repeat=exponent)]
    # from the binary possibilities matrix, create a matrix of dictionaries assigning the 
    # above values to each unique letter with multiple translations
    # this will allow us to test every single possible translation into leetspeak
    matrix = [{letter:binaryPossibilities[i][multipleTranslations.index(letter)]  for letter in multipleTranslations} for i in range(2**exponent)]
    
    # for the single translation letter, replace it (no need to change it alongside the other letters)
    for letter in singleTranslations:
        word = word.replace(letter, translations[letter][0])
    leetWord = word

    # for each combination in the matrix, iterate through
    for row in matrix:
        # for each letter in the combination set replace the letter with its designated translation 
        # determined by the matrix
        for letter in row.keys():
            leetWord = leetWord.replace(letter, translations[letter][row[letter]])
        # append the new possibility to the possibleConverstions list
        possibleConversions.append(leetWord)
        # reset leetWord
        leetWord = word

    # return all possible conversions list
    return possibleConversions

# this function checks the simplest case in which the password is only encrypted with one hash function
# passed are the hashed password from shadow, the list of all leetSpeakConversions of every word in dictionary,
# and a boolean value indicating if we have already found the user that is using the leetspeak, so we don't
# repeat work
def checkSimpleHashes(password, leetSpeakConversions, caesarShifts, haveFoundLeetSpeak, isUser3, haveFoundSALT, saltsFoundSoFar):

    
    # iterate through each word in the dictionary 
    with open("dictionary.txt", "r") as dictionary:
        for word in dictionary:
            # take out newline character from dictionary word
            word = word.replace("\n", "")
            
            # the length of md5 output is 32, so we can specify to check md5 for passwords of length 32
            # check the md5 hash for both the leet speak versions and the regular word
            if len(password) == 32:
                hashedWord = md5(word)
                if hashedWord == password:
                    return word, haveFoundLeetSpeak, haveFoundSALT, saltsFoundSoFar
                
                # if we have not found leet speak user, then test leet speak list
                if haveFoundLeetSpeak == 0:
                    leetSpeakList = leetSpeakConversions[word]
                    for leetSpeakWord in leetSpeakList:
                        hashedLeetSpeak = md5(leetSpeakWord)
                        if hashedLeetSpeak == password:
                            return word, 1, haveFoundSALT, saltsFoundSoFar
                if isUser3 == 1:
                    
                    caesarShiftList = caesarShifts[word]
                    for caesar in caesarShiftList:
                        hashedCaesar = md5(caesar)
                        if hashedCaesar == password:
                            return word, haveFoundLeetSpeak, haveFoundSALT, saltsFoundSoFar

                if haveFoundSALT == 0:
                    if word not in saltsFoundSoFar:
                        saltsFoundSoFar[word] = appendSALT(word)
                    SALTList = saltsFoundSoFar[word]
                    for SALT in SALTList:
                        hashedSALT = md5(SALT)
                        if hashedSALT == password:
                            return word, haveFoundLeetSpeak, 1, saltsFoundSoFar
                
                
            # the length of sha1 output is 40, so we can specify to check sha1 for passwords of length 40
            # check the sha1 hash for both the leet speak versions and the regular word 
            if len(password) == 40:
                hashedWord = sha1(word)
                if hashedWord == password:
                    return word, haveFoundLeetSpeak, haveFoundSALT, saltsFoundSoFar
                # if we have not found leet speak user, then test leet speak list
                if haveFoundLeetSpeak == 0:
                    leetSpeakList = leetSpeakConversions[word]
                    for leetSpeakWord in leetSpeakList:
                        hashedLeetSpeak = sha1(leetSpeakWord)
                        if hashedLeetSpeak == password:
                            return word, 1, haveFoundSALT, saltsFoundSoFar
                if isUser3 == 1:
                    caesarShiftList = caesarShifts[word]
                    for caesar in caesarShiftList:
                        hashedCaesar = sha1(caesar)
                        if hashedCaesar == password:
                            return word, haveFoundLeetSpeak, haveFoundSALT, saltsFoundSoFar
                
                if haveFoundSALT == 0:
                    if word not in saltsFoundSoFar:
                        saltsFoundSoFar[word] = appendSALT(word)
                    SALTList = saltsFoundSoFar[word]
                    for SALT in SALTList:
                        hashedSALT = sha1(SALT)
                        if hashedSALT == password:
                            return word, haveFoundLeetSpeak, 1, saltsFoundSoFar


                
                
            # the length of sha224 and sha3_224 output is 56, so we can specify to check sha224 and sha3_224for 
            # passwords of length 56
            # check the sha224 hash for both the leet speak versions and the regular word
            if len(password) == 56:
                hashedWord1 = sha224(word)
                hashedWord2 = sha3_224(word)
                if hashedWord1 == password or hashedWord2 == password:
                    return word, haveFoundLeetSpeak, haveFoundSALT, saltsFoundSoFar
                # if we have not found leet speak user, then test leet speak list
                if haveFoundLeetSpeak == 0:
                    leetSpeakList = leetSpeakConversions[word]
                    for leetSpeakWord in leetSpeakList:
                        hashedLeetSpeak = sha224(leetSpeakWord)
                        if hashedLeetSpeak == password:
                            return word, 1, haveFoundSALT, saltsFoundSoFar
                if isUser3 == 1:
                    caesarShiftList = caesarShifts[word]
                    for caesar in caesarShiftList:
                        hashedCaesar = sha224(caesar)
                        if hashedCaesar == password:
                            return word, haveFoundLeetSpeak, haveFoundSALT, saltsFoundSoFar
                if haveFoundSALT == 0:
                    if word not in saltsFoundSoFar:
                        saltsFoundSoFar[word] = appendSALT(word)
                    SALTList = saltsFoundSoFar[word]
                    for SALT in SALTList:
                        hashedSALT = sha224(SALT)
                        if hashedSALT == password:
                            del saltsFoundSoFar[word]
                            return word, haveFoundLeetSpeak, 1, saltsFoundSoFar
                    del saltsFoundSoFar[word]
                
             # the length of sha256 output is 64, so we can specify to check sha256 for passwords of length 64
            # check the sha256 hash for both the leet speak versions and the regular word
            if len(password) == 64:
                hashedWord = sha256(word)
                if hashedWord == password:
                    return word, haveFoundLeetSpeak, haveFoundSALT, saltsFoundSoFar
                # if we have not found leet speak user, then test leet speak list
                if haveFoundLeetSpeak == 0:
                    leetSpeakList = leetSpeakConversions[word]
                    for leetSpeakWord in leetSpeakList:
                        hashedLeetSpeak = sha256(leetSpeakWord)
                        if hashedLeetSpeak == password:
                            return word, 1, haveFoundSALT, saltsFoundSoFar
                if isUser3 == 1:
                    caesarShiftList = caesarShifts[word]
                    for caesar in caesarShiftList:
                        hashedCaesar = sha256(caesar)
                        if hashedCaesar == password:
                            return word, haveFoundLeetSpeak, haveFoundSALT, saltsFoundSoFar
                if haveFoundSALT == 0:
                    if word not in saltsFoundSoFar:
                        saltsFoundSoFar[word] = appendSALT(word)
                    SALTList = saltsFoundSoFar[word]
                    for SALT in SALTList:
                        hashedSALT = sha256(SALT)
                        if hashedSALT == password:
                            return word, haveFoundLeetSpeak, 1, saltsFoundSoFar
                        
            # the length of sha384 output is 96, so we can specify to check sha384 for passwords of length 96
            # check the sha384 hash for both the leet speak versions and the regular word
            if len(password) == 96:
                hashedWord = sha384(word)
                if hashedWord == password:
                    return word, haveFoundLeetSpeak, haveFoundSALT, saltsFoundSoFar
                # if we have not found leet speak user, then test leet speak list
                if haveFoundLeetSpeak == 0:
                    leetSpeakList = leetSpeakConversions[word]
                    for leetSpeakWord in leetSpeakList:
                        hashedLeetSpeak = sha384(leetSpeakWord)
                        if hashedLeetSpeak == password:
                            return word, 1, haveFoundSALT, saltsFoundSoFar
                if isUser3 == 1:
                    
                    caesarShiftList = caesarShifts[word]
                    for caesar in caesarShiftList:
                        hashedCaesar = sha384(caesar)
                        if hashedCaesar == password:
                            return word, haveFoundLeetSpeak, haveFoundSALT, saltsFoundSoFar
                        
                if haveFoundSALT == 0:
                    if word not in saltsFoundSoFar:
                        saltsFoundSoFar[word] = appendSALT(word)
                    SALTList = saltsFoundSoFar[word]
                    for SALT in SALTList:
                        hashedSALT = sha384(SALT)
                        if hashedSALT == password:
                            return word, haveFoundLeetSpeak, 1, saltsFoundSoFar
            
                
            # the length of sha512 output is 128, so we can specify to check sha512 for passwords of length 128
            # check the sha512 hash for both the leet speak versions and the regular word, and for the caesar cipher
            # if the isUser3 argument is 1
            if len(password) == 128:
                hashedWord = sha512(word)
                if hashedWord == password:
                    return word, haveFoundLeetSpeak, haveFoundSALT, saltsFoundSoFar
                # if we have not found leet speak user, then test leet speak list
                if haveFoundLeetSpeak == 0:
                    leetSpeakList = leetSpeakConversions[word]
                    for leetSpeakWord in leetSpeakList:
                        hashedLeetSpeak = sha512(leetSpeakWord)
                        if hashedLeetSpeak == password:
                            return word, 1, haveFoundSALT, saltsFoundSoFar
                if isUser3 == 1:
                    
                    caesarShiftList = caesarShifts[word]
                    for caesar in caesarShiftList:
                        hashedCaesar = sha512(caesar)
                        if hashedCaesar == password:
                            return word, haveFoundLeetSpeak, haveFoundSALT, saltsFoundSoFar
                        
                if haveFoundSALT == 0:
                    if word not in saltsFoundSoFar:
                        saltsFoundSoFar[word] = appendSALT(word)
                    SALTList = saltsFoundSoFar[word]
                    for SALT in SALTList:
                        hashedSALT = sha512(SALT)
                        if hashedSALT == password:
                            return word, haveFoundLeetSpeak, 1, saltsFoundSoFar
                
    return "", haveFoundLeetSpeak, haveFoundSALT, saltsFoundSoFar




if __name__ == '__main__':
    start_time = time.perf_counter()

    # open the dictionary file and the shadow file with read permissions
    dictionary = open("dictionary.txt", "r")
    shadow = open("shadow", "r")

    # create dictionary in which the keys are "user1", "user2", etc. and the values are the hashed passwords
    # in the shadow file
    hashedPasswords = {}
    
    # create dictionary in which the keys are "user1", "user2", etc. and the values are the unencrypted
    # password
    truePasswords = {}

    # create dictionary in which the keys are the word from the dictionary file and the values are
    # their hashed value
    hashedWords = {}
    i = 0

    # create a dictionary of all the possible leetspeak conversions of each word in the dictionary
    leetSpeakConversions = {}
    # create a dictionary of all the possible caesar shifts of each word in dictionary.txt
    caesarShifts = {}
    # create a dictionary of all the possible SALT appendages of each word in dictionary.txt
    #SALTS = {}

    # iterate through the words in dictionary.txt and find the leetspeak conversion, caesar
    # shift conversions and SALTS for each word, store in their respective dicts
    for word in dictionary:
        word = word.replace("\n", "")
        leetSpeakConversions[word] = leetSpeakConversion(word)
        caesarShifts[word] = caesarConversion(word)
        #SALTS[word] = appendSALT(word)
    saltsFoundSoFar = {}
        
    leetSpeakPasswordFound = 0
    SALTPasswordFound = 0
    # iterate through each user-password combination in the shadow file
    for userPassword in shadow:
        # derive the user and password hash
        user = userPassword.split(":")[0]
        password = userPassword.split(":")[1].replace("\n","")
        # add each user and password combination to the hashedPasswords dict
        hashedPasswords[user] = password
        
       
    # iterate through the dictionary and try a simple hash, leet code conversion and caesar on each one
    for user in hashedPasswords.keys():
        # set an indicator if this is user 3 so we know to do caesar operations in hash function
        isUser3 = 0
        if user == "user3":
            isUser3 = 1
        
        password = hashedPasswords[user]
        # add result of the checkSimpleHashes() function to the truePasswords dict if it's a valid
        # password
        
        simpleResult, leetSpeakPasswordFound, SALTPasswordFound, saltsFoundSoFar = checkSimpleHashes(password, leetSpeakConversions, caesarShifts, leetSpeakPasswordFound, isUser3, SALTPasswordFound, saltsFoundSoFar)
        if (simpleResult != ""):
            truePasswords[user] = simpleResult
    dictionary.close()
    shadow.close()

    with open("passwords.txt", "w") as output:
        for user in truePasswords.keys():
            output.write(user + ":" + truePasswords[user] + "\n")

        
 
    
    # # now we start other methods of password breaking beyond the simple hash, caesar and leet code
    # # for the passwords that weren't cracked in the first try
    # # this avoids doing long computations like SALT for every single user attempt

    # for user in hashedPasswords.keys():
    #     if user not in truePasswords:
    #         password = hashedPasswords[user]

        
        
        
        
    #print(truePasswords)

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    #print("Elapsed time: ", elapsed_time)



