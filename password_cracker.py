import hashlib
from multiprocessing import Pool
import time
""" Program Flow
- get dictionary into a file reader
- initiate list of different hash methods as strings
- 
 """
start_time = time.perf_counter()
d = open("dictionary.txt", "r")
outFiles = ["myout1.txt", "myout2.txt", "myout3.txt"]

hashes = ["sha1", "md5", "sha256"]


for h in hashes:
    hash = hashlib.new(h)
    for fOut in outFiles:
        with open(fOut,"w") as out:
            for word in d:
                hash.update(word.encode())
                out.write(hash.hexdigest() + "\n")

end_time = time.perf_counter()
elapsed_time = end_time - start_time
print("Elapsed time: ", elapsed_time)

