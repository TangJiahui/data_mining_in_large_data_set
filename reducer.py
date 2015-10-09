#!/local/anaconda/bin/python
# IMPORTANT: leave the above line as is.

import numpy as np
import sys


def print_duplicates(videos, all_shingles):
    unique = np.unique(videos)
    for i in xrange(len(unique)):
        for j in xrange(i + 1, len(unique)):
            minVal = min(unique[i], unique[j])
            maxVal = max(unique[i], unique[j])
            if calculate_similarity(all_shingles[minVal], all_shingles[maxVal]) >= 0.90:
                print "%d\t%d" % (minVal, maxVal)

def calculate_similarity(set1, set2):
    s1 = set(set1)
    s2 = set(set2)
    intersection = len(s1 & s2)
    union = len(s1 | s2)
    if intersection == 0:
        return 0.0
    return float(intersection) / float(union)

last_key = None
key_count = 0
duplicates = []
all_shingles = dict()

for line in sys.stdin:
    line = line.strip()
    key, value = line.split("\t")
    video_id, shingleStr = value.split(";")
    shingles = shingleStr.split("?")

    shingles = [int(x) for x in shingles]

    if last_key is None:
        last_key = key

    if key == last_key:
        duplicates.append(int(video_id))
        all_shingles[int(video_id)] = shingles
    else:

        # Key changed (previous line was k=x, this line is k=y)
        print_duplicates(duplicates, all_shingles)
        duplicates = [int(video_id)]
        all_shingles = {int(video_id): shingles}
        last_key = key

if len(duplicates) > 0:
    print_duplicates(duplicates, all_shingles)
