import math
import os
import random
import re
import sys

def jumpingOnClouds(c):
    cnt = i = 0
    while(i < len(c) - 2):
        if c[i + 2] == 0:
            cnt += 1
            i += 2
        elif c[i + 1] == 0:
            cnt += 1
            i += 1
    if i == len(c)-2:
        cnt += 1
    return cnt


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c)
    fptr.write(str(result) + '\n')
    fptr.close()
