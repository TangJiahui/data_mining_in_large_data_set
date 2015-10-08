#!/local/anaconda/bin/python
# IMPORTANT: leave the above line as is.

# run the code by input in terminal >> python mapper.py <training.txt 
import numpy as np
import sys

if __name__ == "__main__":
    # VERY IMPORTANT:
    # Make sure that each machine is using the
    # same seed when generating random numbers for the hash functions.
    np.random.seed(seed=42)
    num_of_hash = 20
    band = 5
    r = num_of_hash/band
    permutations = []

    # generate a list of hash permutations for min-hash
    for i in range(num_of_hash):
        arr = np.arange(20001)
        np.random.shuffle(arr)
        permutations.append(arr) 

    # generate hash function parameters for each band
    a = np.random.randint(1,51,band)
    b = np.random.randint(20,71,band)
    n = np.random.randint(40,91,band)

    # function to yield successive n-sized chunks from list l
    def chunks(l,n):
        for i in xrange(0,len(l),n):
            yield l[i:i+n]


    for line in sys.stdin:
        line = line.strip()
        video_id = int(line[6:15])
        #shingles = np.unique(np.fromstring(line[16:], dtype=int, sep=" "))
        shingles = np.fromstring(line[16:], dtype=int, sep=" ")

        signature = []

        for i in permutations:
            for j in range(len(i)):
                if i[j] in shingles:     
                    signature.append(j+1)
                    break

        # divide signature into b*r
        splited_signature = list(chunks(signature,r))
        
        hash_result = []
        # hash bands
        for i in range(len(splited_signature)):
            result = 0
            for j in splited_signature[i]:
                result += a[i]*j+b[i]
            result = result%n[i]
            hash_result.append(result)    
        

        print (video_id, hash_result)
        
