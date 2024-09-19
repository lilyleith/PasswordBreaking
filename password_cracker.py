import hashlib
import time
from itertools import product


# returns all possible SALT options for the word
def appendSALT(word):
    possibleSALTS = []
    # iterate through numbers in range 0 to 99999
    for num in range(100000):
        # create the salt and append
        SALT = str(num).zfill(5)
        possibleSALTS.append(word + SALT)
    return possibleSALTS


# find and return all possible caesar translations of a given word
def caesarConversion(word):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    # list for all possible caesar translations
    caesarTranslations = []

    # list of letters
    letters = [letter for letter in word]
    for shift in range(1, 26):
        # empty list for the result
        caesar = ["" for i in range(len(word))]
        for index in range(len(word)):
            # iterate through word, if the letter isn't in in the alphabet then skip it
            if letters[index] not in alphabet:
                continue
            # find the new index of the letter 
            newLetterIndex = (alphabet.index(letters[index]) + shift) % 26
            # assign letter to new index
            caesar[index] = alphabet[newLetterIndex] 
        caesarTranslations.append("".join(caesar))
    # return the list of caesar translations
    return caesarTranslations



# translate a word into leetspeak
def leetSpeakConversion(word):
    # list of possible translations, some letters just maps to themselves if I couldn't find a single letter mapping that made sense
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
    # this matrix basically holds all the possible permutations of each unique letter that has more than
    # one mapping 
    binaryPossibilities = [list(x) for x in product([0, 1], repeat=exponent)]
    # from the binary possibilities matrix, create a matrix of dictionaries assigning the 
    # above values to each unique letter with multiple translations
    # this will allow us to test every single possible translation into leetspeak
    matrix = [{letter:binaryPossibilities[i][multipleTranslations.index(letter)]  for letter in multipleTranslations} for i in range(2**exponent)]
    
    # for the single translation letters, replace it (no need to change it alongside the other letters)
    for letter in singleTranslations:
        word = word.replace(letter, translations[letter][0])
    leetWord = word

    # for each combination in the matrix, iterate through
    for row in matrix:
        # for each letter in the permutation replace the letter with its designated translation 
        # determined by the matrix
        for letter in row.keys():
            leetWord = leetWord.replace(letter, translations[letter][row[letter]])
        # append the new possibility to the possibleConverstions list
        possibleConversions.append(leetWord)
        # reset leetWord
        leetWord = word

    # return all possible conversions list
    return possibleConversions

# function returns the encrypted word using the passed mapping
def substitution(mapping, word):
    # create list of the letters
    letterList = [letter for letter in word]
    # iterate through and change the letters based on the mapping
    for index in range(len(letterList)):
        if letterList[index] in mapping:
            letterList[index] = mapping[letterList[index]]
    # return the new word
    return "".join(letterList)


# this function tries to find the hash of a dictionary entry that matches password
# through a variety of substitions and translations
# returns:
# word if the password is found or ""
# haveFoundLeetSpeak = 0 if we have not done the leetSpeak user yet, 1 if we have
# haveFoundSALT = 0 if we have not done the SALT user yet, 1 if we have
# saltsFoundSoFar: a dictionary that we can use to store the SALTS we have found so we save processing
# time any way we can
def hashCheck(password, leetSpeakConversions, caesarShifts, haveFoundLeetSpeak, isUser3, haveFoundSALT, saltsFoundSoFar, isUser7, substitutions, hashFunction):

    # iterate through each word in the dictionary 
    with open("dictionary.txt", "r") as dictionary:
        for word in dictionary:
            # take out newline character from dictionary word
            word = word.replace("\n", "")
            
            # first check if the user is user 3, if so, then create list of all the caesar shifts of
            # the current word
            if isUser3 == 1:
                caesarShiftList = caesarShifts[word]
                # hash each caesar shift translation and check if it matches the password hash
                for caesar in caesarShiftList:
                    hash = hashlib.new(hashFunction)
                    hash.update(caesar.encode())
                    hashedCaesar = hash.hexdigest()
                    # return if we have a match
                    if hashedCaesar == password:
                        return word, haveFoundLeetSpeak, haveFoundSALT, saltsFoundSoFar
                # if the current user is user 7, then we get the list of the substitutions of the current word
            elif isUser7 == 1:
                wordSub = substitutions[word]
                # hash each substitution
                hash = hashlib.new(hashFunction)
                hash.update(wordSub.encode())
                hashedSub = hash.hexdigest()
                # return if we have a match
                if hashedSub == password:
                    return word, haveFoundLeetSpeak, haveFoundSALT, saltsFoundSoFar
            # now check the hashed value of the plain word, if it matches then return it
            hash = hashlib.new(hashFunction)
            hash.update(word.encode())
            hashedWord = hash.hexdigest()
            if hashedWord == password:
                return word, haveFoundLeetSpeak, haveFoundSALT, saltsFoundSoFar
            
            # if we have not found leet speak user, then test leet speak list for the current word
            if haveFoundLeetSpeak == 0:
                leetSpeakList = leetSpeakConversions[word]
                for leetSpeakWord in leetSpeakList:
                    # hash the leetSpeakWord, if it matches then return the original word
                    hash = hashlib.new(hashFunction)
                    hash.update(leetSpeakWord.encode())
                    hashedLeetSpeak = hash.hexdigest()
                    if hashedLeetSpeak == password:
                        return word, 1, haveFoundSALT, saltsFoundSoFar
            
            # if we have not yet found the salt user, then we hash all the possible salts for 
            # the current word
            if haveFoundSALT == 0:
                # if the word is not in the salts dictionary, add it
                if word not in saltsFoundSoFar:
                    saltsFoundSoFar[word] = appendSALT(word)
                # create the list of salts
                SALTList = saltsFoundSoFar[word]
                # hash each salt, if it matches then return it
                for SALT in SALTList:
                    hash = hashlib.new(hashFunction)
                    hash.update(SALT.encode())
                    hashedSALT = hash.hexdigest()
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

    # create a dictionary of all the possible leetspeak conversions of each word in dictionary.txt
    leetSpeakConversions = {}
    # create a dictionary of all the possible caesar shifts of each word in dictionary.txt
    caesarShifts = {}

    # based on work in analysis.py, we have this substitution key for user 7:
    # added mapping from "z"->"a" and from "j"->"z" since these were not included in the encrypted text solution
    currentMapping = {"a":"b", "e":"f", "t":"s", "o":"j", "h":"m", "l":"p", "n":"v", "d":"l", "i":"d", "s":"t", "c":"w", "p":"n", "w":"u", "b":"r", "y":"k", "u":"e", "m":"g", "f":"q", "r":"c", "g":"i", "v":"x", "k":"y", "q":"h", "x":"o", "z":"a", "j":"z"}
    # create a dictionary of the user7 substitutions for each word in dictionary.txt
    mappedWords = {}

    # iterate through the words in dictionary.txt and find the leetspeak conversion, caesar
    # shift conversions, and user7 substitution for each word store in their respective dicts
    for word in dictionary:
        word = word.replace("\n", "")
        leetSpeakConversions[word] = leetSpeakConversion(word)
        caesarShifts[word] = caesarConversion(word)
        #SALTS[word] = appendSALT(word)
        mappedWords[word] = substitution(currentMapping, word)

    # stores salts of dictionary words we have found so far. marginally helps saving runtime
    saltsFoundSoFar = {}

    subs = open("substitutions.txt", "w")
    for word, sub in mappedWords.items():
        subs.write(word + " " + sub + "\n")
    subs.close()
    # leetSpeakPasswordFound is set to 1 and returned within the hashing function if we have successfully found the
    # user that uses leetSpeak
    leetSpeakPasswordFound = 0
    # SALTPasswordFound is set to 1 and returned within the hashing function if we have successfully found the
    # user that uses a SALT
    SALTPasswordFound = 0

    # iterate through each user-password combination in the shadow file
    for userPassword in shadow:
        # derive the user and password hash
        user = userPassword.split(":")[0]
        password = userPassword.split(":")[1].replace("\n","")
        # add each user and password combination to the hashedPasswords dict
        hashedPasswords[user] = password
    
    # track the current user for printing runtimes
    userCount = 1

    # iterate through the dictionary and try a simple hash, leet code conversion and caesar on each one
    for user in hashedPasswords.keys():
        # set an indicator if this is user 3 so we know to do caesar operations in hash function
        isUser3 = 0
        isUser7 = 0
        if user == "user3":
            isUser3 = 1
        elif user == "user7":
            isUser7 = 1
        
        # get password from user password dict
        password = hashedPasswords[user]
        # init truePassword
        truePassword = ""
        
        
        user_start = time.perf_counter()

        # we can expedite the hashing process by checking the length of the hashed password and only
        # performing hash functions that would give an output of the same length
        # for each call of the function we pass through information that helps cut down runtime by
        # not hashing all translations (leetspeak, caesar, etc.) for every password 

        # len md5 = 32 
        if len(password) == 32:
            truePassword, leetSpeakPasswordFound, SALTPasswordFound, saltsFoundSoFar = hashCheck(password, leetSpeakConversions, caesarShifts, leetSpeakPasswordFound, isUser3, SALTPasswordFound, saltsFoundSoFar, isUser7, mappedWords, "md5")
        # len sha1 = 40
        elif len(password) == 40:
            truePassword, leetSpeakPasswordFound, SALTPasswordFound, saltsFoundSoFar = hashCheck(password, leetSpeakConversions, caesarShifts, leetSpeakPasswordFound, isUser3, SALTPasswordFound, saltsFoundSoFar, isUser7,mappedWords, "sha1")
        # len sha224 = 56 and len sha3_224 = 56, check both if sha224 doesn't work
        elif len(password) == 56:
            truePassword, leetSpeakPasswordFound, SALTPasswordFound, saltsFoundSoFar = hashCheck(password, leetSpeakConversions, caesarShifts, leetSpeakPasswordFound, isUser3, SALTPasswordFound, saltsFoundSoFar, isUser7, mappedWords,"sha224")
            if truePassword == "":
                truePassword, leetSpeakPasswordFound, SALTPasswordFound, saltsFoundSoFar = hashCheck(password, leetSpeakConversions, caesarShifts, leetSpeakPasswordFound, isUser3, SALTPasswordFound, saltsFoundSoFar, isUser7, mappedWords, "sha3_224")
        # len sha256 = 64
        elif len(password) == 64:
            truePassword, leetSpeakPasswordFound, SALTPasswordFound, saltsFoundSoFar = hashCheck(password, leetSpeakConversions, caesarShifts, leetSpeakPasswordFound, isUser3, SALTPasswordFound, saltsFoundSoFar, isUser7, mappedWords, "sha256")
        # len sha512 = 128 and len sha3_512 = 128, check both if sha512 doesn't work
        elif len(password) == 128:
            truePassword, leetSpeakPasswordFound, SALTPasswordFound, saltsFoundSoFar = hashCheck(password, leetSpeakConversions, caesarShifts, leetSpeakPasswordFound, isUser3, SALTPasswordFound, saltsFoundSoFar, isUser7, mappedWords, "sha512")
            if truePassword == "":
                truePassword, leetSpeakPasswordFound, SALTPasswordFound, saltsFoundSoFar = hashCheck(password, leetSpeakConversions, caesarShifts, leetSpeakPasswordFound, isUser3, SALTPasswordFound, saltsFoundSoFar, isUser7, mappedWords, "sha3_512")

        # if the password is valid, add it to truePasswords
        if (truePassword != ""):
            truePasswords[user] = truePassword
            user_end = time.perf_counter()
            #print("Elapsed time for user", userCount, user_end-user_start)
            userCount += 1

    # close the files
    dictionary.close()
    shadow.close()
    # write to the passwords file with the results
    with open("passwords.txt", "w") as output:
        for user in truePasswords.keys():
            output.write(user + ":" + truePasswords[user] + "\n")


    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    #print("Total elapsed time: ", elapsed_time)



