currentMapping = {"a":"b", "e":"f", "t":"s", "o":"j", "h":"m", "l":"p", "n":"v", "d":"l", "i":"d", "s":"t", "c":"w", "p":"n", "w":"u", "b":"r", "y":"k", "u":"e", "m":"g", "f":"q", "r":"c", "g":"i", "v":"x", "k":"y", "q":"h", "x":"o"}
alpha = [key for key in currentMapping.keys()]
beta = [value for value in currentMapping.values()]
alpha.sort()
beta.sort()
print("plaintext: ", alpha)
print("ciphertext: ", beta)
