import hashlib
from multiprocessing import Pool
import time
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

# translate a word into leetspeak
def leetSpeakConversion(word, iteration):
# 2 iterations as of right now
    translations = {"a": ["4","@"], "b":["8", "8"], "c":["c", "["], "d":["d", ")"], "e":["3", "&"], "f":["f"], "g":["6", "&"], "h":["h", '#'], "i":["i", "!"], "j":["j", "j"], "k":["k", "k"], "l":["1","!"], "m":["m", "m"],"n":["n", "n"], "o":["0", "0"], "p":["p", "p"], "q":["q", "q"], "r":["r", "r"], "s":["5", "$"], "t":["7", "+"], "u":["u", "u"], "v":["v", "v"], "w":["w", "w"], "x":["x", "x"], "y":["y", "y"], "z":["2", "2"], "q":["9"]}
   
# MAX INDEX = 2 LEN 3 INDEX - INDEX LEN MINUS LEN
    leetWord = "".join([translations[letter][0] for letter in word])

    for i in range(2):




    

    if forward == 1:
        word = word.replace("a", "4")
        word = word.replace("b", "8") # this is a maybe
        word = word.replace("e", "3")
        word = word.replace("g", "6") # maybe
        word = word.replace("l", "1")
       # word = word.replace("i", "!")
        word = word.replace("o", "0")
        word = word.replace("s", "5")
        word = word.replace("t", "7")
        word = word.replace("z", "2")
        word = word.replace("q", "9")
    else:
        word = word.replace("4", "a")
        word = word.replace("8", "b") # this is a maybe
        word = word.replace("3", "e")
        word = word.replace("6", "g") # maybe
        word = word.replace("1", "l")
       # word = word.replace("!", "i")
        word = word.replace("0", "o")
        word = word.replace("5", "s")
        word = word.replace("7", "t")
        word = word.replace("2", "z")
    return word

# this function checks the simplest case in which the password is only encrypted with one hash function
def checkSimpleHashes(password):

    # iterate through each word in the dictionary 
    with open("dictionary.txt", "r") as dictionary:
        for word in dictionary:
            # take out newline character from dictionary word
            word = word.replace("\n", "")
            
            # get the leet speak conversion
            leetSpeakWord = leetSpeakConversion(word, 1)
            #print(leetSpeakWord)
            # the length of md5 output is 32, so we can specify to check md5 for passwords of length 32
            # check the md5 hash for both the leet speak version and the regular word
            if len(password) == 32:
                hashedWord = md5(word)
                hashedLeetSpeak = md5(leetSpeakWord)

                if hashedWord == password:
                    return word
                
                if hashedLeetSpeak == password:
                    return leetSpeakWord
            # the length of sha1 output is 40, so we can specify to check sha1 for passwords of length 40
            # check if sha1 gives result, if it does then set the key-value pair in truePasswords  
            if len(password) == 40:
                hashedWord = sha1(word)
                hashedLeetSpeak = sha1(leetSpeakWord)
                if hashedWord == password:
                    return word
            
                if hashedLeetSpeak == password:
                    return leetSpeakWord
                
            # the length of sha224 output is 28, so we can specify to check sha224 for passwords of length 28
            # check if sha224 gives result, if it does then set the key-value pair in truePasswords
            if len(password) == 28:
                hashedWord = sha224(word)
                hashedLeetSpeak = sha224(leetSpeakWord)
                if hashedWord == password:
                    return word
                if hashedLeetSpeak == password:
                    return leetSpeakWord
                    
            # the length of sha256 output is 64, so we can specify to check sha256 for passwords of length 64
            # check if sha256 gives result, if it does then set the key-value pair in truePasswords
            if len(password) == 64:
                hashedWord = sha256(word)
                hashedLeetSpeak = sha256(leetSpeakWord)
                if hashedWord == password:
                    return word
                if hashedLeetSpeak == password:
                    return leetSpeakWord
    return ""




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

   
    # iterate through each user-password combination in the shadow file
    for userPassword in shadow:
        # derive the user and password hash
        user = userPassword.split(":")[0]
        password = userPassword.split(":")[1].replace("\n","")
        
        # add each user and password combination to the hashedPasswords dict
        hashedPasswords[user] = password
        leetSpeakWords = {}
        dictionary = open("dictionary.txt","r")
        for word in dictionary:
            leetSpeakWords[word] = []
            for i in range(2):
                leetSpeakWord = leetSpeakConversion(word, i)
                leetSpeakWords[word][i] = leetSpeakWord
        
        
        # add result of the checkSimpleHashes() function to the truePasswords dict if it's a valid
        # password
        simpleResult = checkSimpleHashes(password)
        if (simpleResult != ""):
            truePasswords[user] = simpleResult
        
        
    print(truePasswords)

       
        
    
    


    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print("Elapsed time: ", elapsed_time)



