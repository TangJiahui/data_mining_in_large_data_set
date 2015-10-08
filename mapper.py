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
    num_of_hash = 10
    band = 2
    r = num_of_hash/band
    permutations = []

    for i in range(num_of_hash):
        arr = np.arange(20001)
        np.random.shuffle(arr)
        permutations.append(arr) # a list of hash permutations

    # function to yield successive n-sized chunks from list l
    def chunks(l,n):
        for i in xrange(0,len(l),n):
            yield l[i:i+n]

    for line in sys.stdin:
        line = line.strip()
        video_id = int(line[6:15])
        shingles = np.unique(np.fromstring(line[16:], dtype=int, sep=" "))

        signature = []

        for i in permutations:
            for j in range(len(i)):
                if i[j] in shingles:     
                    signature.append(j+1)
                    break

        splited_signature = list(chunks(signature,r))
        

        print (video_id, splited_signature)
        
