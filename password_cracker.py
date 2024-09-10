import hashlib
from multiprocessing import Pool
import time
""" Program Flow
- get dictionary into a file reader
- initiate list of different hash methods as strings
- 
 """
start_time = time.perf_counter()
dictionary = open("dictionary.txt", "r")

outFiles = ["myout1.txt", "myout2.txt", "myout3.txt"]

hashes = ["sha1", "md5", "sha256"]
passwords = {}
hashedPasswords = {}
with open("shadow", "r") as f2:
    for userPassword in f2:
        userPass = userPassword.split(":")
        passwords[userPass[0]] = userPass[1]
        hashedPasswords[userPass[0]] = ""
    


for user in passwords.keys():
    pws = passwords[user]
    for h in hashes:
        hash = hashlib.new(h)
        hash.update(pws)
        hashedPasswords[user] = hash.hexdigest()
        """ for fOut in outFiles:
            with open(fOut,"w") as out:
                for word in d:
                    hash2 = hashlib.new(h)
                    hash2.update(word.encode())
                    out.write(hash2.hexdigest() + "\n") """

end_time = time.perf_counter()
elapsed_time = end_time - start_time
print("Elapsed time: ", elapsed_time)

