
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
    exponent = 0
    for letter in letters:
        if len(translations[letter]) > 1:
            exponent += 1
    print(exponent)





leetSpeakConversion("hello")
newTest("hello")
print(leetSpeakConversion("hello"))