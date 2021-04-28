from collections import Counter

def sockMerchant(n, ar):
    dictionary_count = Counter(ar)
    return sum([ int(value/2) for key, value in dictionary_count.items()])
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    fptr.write(str(result) + '\n')
    fptr.close()
