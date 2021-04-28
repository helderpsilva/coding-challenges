import math
import os
import random
import re
import sys

def countingValleys(steps, path):        
    altitude = [0]
    hike = [1 if i == 'U' else -1 for i in ''.join([path[i] for i in range(steps)])]

    for i in hike:
        altitude.append(altitude[-1] + i)

    return sum([1 if (altitude[i] == 0 and altitude[i+1] < 0) else 0 for i in range(len(altitude)-1)])
   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    steps = int(input().strip())
    path = input()
    result = countingValleys(steps, path)
    fptr.write(str(result) + '\n')
    fptr.close()
