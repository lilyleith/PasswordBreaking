from multiprocessing import Pool
import hashlib
import time

def hash(args):
    with open('dictionary.txt', 'r') as fIn:
        words = fIn.read().splitlines()
        hash = hashlib.new(args[0])
     
        with open(args[1],"w") as fOut:
            for word in words:
                hash.update(word.encode())
                fOut.write(hash.hexdigest() + "\n")

    
if __name__ == '__main__':
    start_time = time.perf_counter()
    inF = open('dictionary.txt', 'r')


    outFiles = ['sha1_results.txt', 'sha256_results.txt', 'md5_results.txt']
    hashes = ["sha1", "sha256", "md5"]  
    args = list(zip(hashes, outFiles))

    pool = Pool(3)
    pool.map(hash, args)
    pool.close()
    pool.join()

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print("Elapsed time: ", elapsed_time)
