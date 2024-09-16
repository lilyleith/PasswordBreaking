import hashlib
import time
import numpy as np


# first we have a frequency table of letters in the alphabet from https://www3.nd.edu/~busiforc/handouts/cryptography/letterfrequencies.html
azFrequencies = {"a":0.084966, "b":0.020720, "c": 0.045388, "d":0.033844, "e":0.111607, "f":0.018121, "g": 0.024705, "h": 0.030034, "i": 0.075448, "j": 0.001965, "k": 0.011016, "l":0.054893, "m": 0.030129, "n":0.066544, "o":0.071635, "p": 0.031671, "q":0.001962, "r":0.075809, "s":0.057351, "t":0.069509, "u":0.036308, "v":0.010074, "w":0.012899, "x":0.002902, "y": 0.017779, "z":0.002722}

azCounts = {}
totalLetters = 0
words = list()
with open("encrypted.txt", "r") as encrypted:
    for line in encrypted:
        words = line.split(" ")
        for word in words:
            for letter in word:
                if letter in azFrequencies.keys():
                    totalLetters += 1
                    if letter not in azCounts:
                        azCounts[letter] = 1
                    else:
                        azCounts[letter] += 1
                else:
                    continue
#print(words)
observedFrequencies = {}
for letter in azCounts:
    observedFrequencies[letter] = azCounts[letter] / totalLetters
observedFrequencies = dict(sorted(observedFrequencies.items(), key= lambda item: item[1], reverse = True))

closestFrequencies = {}

# for letter,frequency in observedFrequencies.items():
#     print(letter,frequency)

# for letter,frequency in azFrequencies.items():
#     print(letter,frequency)
for letter,frequency in observedFrequencies.items():
    diff0 = 1000
    closest = ""
    for az,azFreq in azFrequencies.items():
        diff1 = abs(frequency - azFreq)
        if diff1 < diff0:
            diff0 = diff1
            
            closest = az
            

    closestFrequencies[letter] = closest
# for key, value in closestFrequencies.items():   
#     print(key, value)

newWordList = list()
for word in words:
    newWord = word
    for letter,subLetter in closestFrequencies.items():
        newWord = newWord.replace(letter, subLetter)
    newWordList.append(newWord)

for word in newWordList:
    print(word)

commonTwoLetterWords = ["of","to","in","it","is","be","as","at","so","we","he","by","or","on","do","if","me","my","up","an","go","no","us","am"]
realFreqsOfTLW = {}
totalLettersInTLW = 0
for word in commonTwoLetterWords:
    for letter in word:
        totalLettersInTLW += 1
        if letter not in realFreqsOfTLW:
            realFreqsOfTLW[letter] = 1
        else:
            realFreqsOfTLW[letter] += 1
for letter, count in realFreqsOfTLW.items():
    realFreqsOfTLW[letter] = count/totalLettersInTLW
realFreqsOfTLW = dict(sorted(realFreqsOfTLW.items(),key= lambda item: item[1], reverse=True))
print(realFreqsOfTLW)
observedTwoLetterWords = [word for word in words if len(word) == 2]


observedFreqsOfTLW = {}
totalLettersInTLW = 0
for word in observedTwoLetterWords:
    for letter in word:
            totalLettersInTLW += 1
            if letter not in observedFreqsOfTLW:
                observedFreqsOfTLW[letter] = 1
            else:
                observedFreqsOfTLW[letter] += 1
for letter, count in observedFreqsOfTLW.items():
    observedFreqsOfTLW[letter] = count/totalLettersInTLW
observedFreqsOfTLW = dict(sorted(observedFreqsOfTLW.items(), key= lambda item: item[1], reverse=True))

print(observedFreqsOfTLW)
print(commonTwoLetterWords)
print(observedTwoLetterWords)

testTLW = [tlw for tlw in observedTwoLetterWords]
for index in range(len(testTLW)):
    testTLW[index] = testTLW[index].replace("j", "o")
    testTLW[index] = testTLW[index].replace("q", "f")
    testTLW[index] = testTLW[index].replace("d", "i")
    testTLW[index] = testTLW[index].replace("t", "n")
    testTLW[index] = testTLW[index].replace("n", "t")
    testTLW[index] = testTLW[index].replace("e", "a")
    




print(testTLW)




    
