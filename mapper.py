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
    num_of_hash = 5
    permutations = []
    for i in range(1, num_of_hash):
        permutations.append(np.random.randint(0,20001,20001)) # a list of hash permutations

    for line in sys.stdin:
        line = line.strip()
        video_id = int(line[6:15])
        shingles = np.fromstring(line[16:], sep=" ")

        signature = []

        for i in permutations:
            for j in range(len(i)+1):
                if float(i[j]) in shingles:
                    signature.append(j+1)
                    break

        print (video_id, signature)


        