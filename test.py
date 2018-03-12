from math import sqrt
from time import time
PRIME_NUM = 10101010101
def prime_list():
    prime_list = [2]
    total = PRIME_NUM
    loop = 0
    start = time()
    for x in range(3,int(total)+1):
        loop += 1
        if loop % (PRIME_NUM / 100) == 0:
            print(loop)
        for prime in prime_list:
            if x % prime == 0:
                break
        else:
            prime_list.append(x)
    end = time()
    print(end - start)
    return(end-start)
def prime_check():
    prime_list = [2]
    total = PRIME_NUM
    start = time()
    loop = 0
    for x in range(3,int(total)+1):
        loop += 1
        if loop % (PRIME_NUM / 100) == 0:
            print(loop)
        if x % 2 != 0:
            for n in range(3,int(sqrt(x))+1,2):
                if x % n == 0:
                    break
            else:
                prime_list.append(x)
    end = time()
    print(end-start)
    print(len(prime_list))
    return(end-start)
prime_check()