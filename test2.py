import numpy as np
from itertools import product

def oldLeetSpeakConversion(word):
    translations = {"a": ["4","@"], "b":["b", "8"], "c":["c", "["], "d":["d", ")"], "e":["3", "&"], "f":["f"], "g":["6", "&"], "h":["h", '#'], "i":["1", "!"], "j":["j", "j"], "k":["k", "k"], "l":["1","!"], "m":["m", "m"],"n":["n", "n"], "o":["0", "0"], "p":["p", "9"], "q":["q", "q"], "r":["r", "r"], "s":["5", "$"], "t":["7", "+"], "u":["u", "u"], "v":["v", "v"], "w":["w", "w"], "x":["x", "x"], "y":["y", "y"], "z":["2", "2"], "q":["9"]}
   
    leetWord = word

    possibleConversions = []

    # iterate through each letter and replace with possible leet speak substitutions and add each possible
    # translation to possibleConversions
    for a in range(2):
        leetWord = leetWord.replace("a", translations["a"][a])
        if leetWord not in possibleConversions:
            possibleConversions.append(leetWord)
        for b in range(2):
            leetWord = leetWord.replace("b", translations["b"][b])
            if leetWord not in possibleConversions:
                possibleConversions.append(leetWord)
            for c in range(2):
                leetWord = leetWord.replace("c", translations["c"][c])
                if leetWord not in possibleConversions:
                    possibleConversions.append(leetWord)
                for d in range(2):
                    leetWord = leetWord.replace("d", translations["d"][d])
                    if leetWord not in possibleConversions:
                        possibleConversions.append(leetWord)
                    for e in range(2):
                        leetWord = leetWord.replace("e", translations["e"][e])
                        if leetWord not in possibleConversions:
                            possibleConversions.append(leetWord)
                        for g in range(2):
                            leetWord = leetWord.replace("g", translations["g"][g])
                            if leetWord not in possibleConversions:
                                possibleConversions.append(leetWord)
                            for h in range(2):
                                leetWord =leetWord.replace("h", translations["h"][h])
                                if leetWord not in possibleConversions:
                                    possibleConversions.append(leetWord)
                                for i in range(2):
                                    leetWord = leetWord.replace("i", translations["i"][i])
                                    if leetWord not in possibleConversions:
                                        possibleConversions.append(leetWord)
                                    for l in range(2):
                                        leetWord = leetWord.replace("l", translations["l"][l])
                                        if leetWord not in possibleConversions:
                                            possibleConversions.append(leetWord)
                                        leetWord = leetWord.replace("o", "0")
                                        if leetWord not in possibleConversions:
                                            possibleConversions.append(leetWord)
                                        for p in range(2):
                                            leetWord = leetWord.replace("p", translations["p"][p])
                                            if leetWord not in possibleConversions:
                                                possibleConversions.append(leetWord)
                                            for s in range(2):
                                                leetWord = leetWord.replace("s", translations["s"][s])
                                                if leetWord not in possibleConversions:
                                                    possibleConversions.append(leetWord)
                                                for t in range(2):
                                                    leetWord = leetWord.replace("t", translations["t"][t])
                                                    if leetWord not in possibleConversions:
                                                        possibleConversions.append(leetWord)
                                                    for z in range(2):
                                                        leetWord = leetWord.replace("z", translations["z"][z])
                                                        if leetWord not in possibleConversions:
                                                            possibleConversions.append(leetWord)
                                                        leetWord = word
                                                            
    return possibleConversions
    

def leetSpeakConversion(word):
# 2 iterations as of right now
    translations = {"a": ["4","@"], "b":["b", "8"], "c":["c", "["], "d":["d", ")"], "e":["3", "&"], "f":["f"], "g":["6", "&"], "h":["h", '#'], "i":["1", "!"], "j":["j", "j"], "k":["k", "k"], "l":["1","!"], "m":["m", "m"],"n":["n", "n"], "o":["0", "0"], "p":["p", "9"], "q":["q", "q"], "r":["r", "r"], "s":["5", "$"], "t":["7", "+"], "u":["u", "u"], "v":["v", "v"], "w":["w", "w"], "x":["x", "x"], "y":["y", "y"], "z":["2", "2"], "q":["9"]}

    leetWord = word

    possibleConversions = []

    # iterate through each letter and replace with possible leet speak substitutions and add each possible
    # translation to possibleConversion
    for a in range(2):
        leetWord = leetWord.replace("a", translations["a"][a])
        if leetWord not in possibleConversions:
            possibleConversions.append(leetWord)
        for b in range(2):
            leetWord = leetWord.replace("b", translations["b"][b])
            if leetWord not in possibleConversions:
                possibleConversions.append(leetWord)
            for c in range(2):
                leetWord = leetWord.replace("c", translations["c"][c])
                if leetWord not in possibleConversions:
                    possibleConversions.append(leetWord)
                for d in range(2):
                    leetWord = leetWord.replace("d", translations["d"][d])
                    if leetWord not in possibleConversions:
                        possibleConversions.append(leetWord)
                    for e in range(2):
                        leetWord = leetWord.replace("e", translations["e"][e])
                        if leetWord not in possibleConversions:
                            possibleConversions.append(leetWord)
                        for g in range(2):
                            leetWord = leetWord.replace("g", translations["g"][g])
                            if leetWord not in possibleConversions:
                                possibleConversions.append(leetWord)
                            for h in range(2):
                                leetWord =leetWord.replace("h", translations["h"][h])
                                if leetWord not in possibleConversions:
                                    possibleConversions.append(leetWord)
                                for i in range(2):
                                    leetWord = leetWord.replace("i", translations["i"][i])
                                    if leetWord not in possibleConversions:
                                        possibleConversions.append(leetWord)
                                    for l in range(2):
                                        leetWord = leetWord.replace("l", translations["l"][l])
                                        if leetWord not in possibleConversions:
                                            possibleConversions.append(leetWord)
                                        leetWord = leetWord.replace("o", "0")
                                        if leetWord not in possibleConversions:
                                            possibleConversions.append(leetWord)
                                        for p in range(2):
                                            leetWord = leetWord.replace("p", translations["p"][p])
                                            if leetWord not in possibleConversions:
                                                possibleConversions.append(leetWord)
                                            for s in range(2):
                                                leetWord = leetWord.replace("s", translations["s"][s])
                                                if leetWord not in possibleConversions:
                                                    possibleConversions.append(leetWord)
                                                for t in range(2):
                                                    leetWord = leetWord.replace("t", translations["t"][t])
                                                    if leetWord not in possibleConversions:
                                                        possibleConversions.append(leetWord)
                                                    for z in range(2):
                                                        leetWord = leetWord.replace("z", translations["z"][z])
                                                        if leetWord not in possibleConversions:
                                                            possibleConversions.append(leetWord)
                                                        leetWord = word
                                                            
    return possibleConversions


def newTest(word):
    translations = {"a": ["4","@"], "b":["b", "8"], "c":["c", "["], "d":["d", ")"], "e":["3", "&"], "f":["f"], "g":["6", "&"], "h":["h", '#'], "i":["1", "!"], "j":["j"], "k":["k"], "l":["1","!"], "m":["m"],"n":["n"], "o":["0"], "p":["p", "9"], "q":["q"], "r":["r"], "s":["5", "$"], "t":["7", "+"], "u":["u"], "v":["v"], "w":["w"], "x":["x"], "y":["y"], "z":["2"], "q":["9"]}

    leetWord = word

    possibleConversions = []

    substitutionTracker = {}
    # iterate through each letter and replace with possible leet speak substitutions and add each possible
    # translation to possibleConversions

    
    letters = [char for char in word]
    uniqueLetters = []
    for letter in letters:
        if letter not in uniqueLetters:
            uniqueLetters.append(letter)

        substitutionTracker[letter] = 0

    exponent = 0
    multipleTranslations = []
    singleTranslations = []
    for letter in uniqueLetters:
        if len(translations[letter]) > 1:
            exponent += 1
            multipleTranslations.append(letter)
        else:
            singleTranslations.append(letter)

    binaryPossibilities = [list(x) for x in product([0, 1], repeat=3)]
    

    matrix = [{letter:binaryPossibilities[i][multipleTranslations.index(letter)]  for letter in multipleTranslations} for i in range(2**exponent)]
    

    
    for letter in singleTranslations:
        word = word.replace(letter, translations[letter][0])
    leetWord = word

    for row in matrix:
        for letter in row.keys():
            leetWord = leetWord.replace(letter, translations[letter][row[letter]])
        possibleConversions.append(leetWord)
        leetWord = word

    return possibleConversions

def appendSALT(word):
    possibleSALTS = []
    for num in range(100000):
        SALT = str(num).zfill(5)
        possibleSALTS.append(word + SALT)
    return possibleSALTS

binaryPossibilities = [list(x) for x in product([0, 1], repeat=9)]
print(binaryPossibilities)
print(newTest("hello"))

print(appendSALT("hello"))

