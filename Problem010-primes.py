"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million."""

number_limit = 5000000

import time
start_time = time.time()


import math

# 5m -> 48 sec
def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

# 5m -> 49 sec
def isPrime(num):
    if num in (2, 3, 5, 7): return True
    if not num % 2 or not num % 3: return False
    n = 5
    lim = int(math.sqrt(num)) + 1
    while n <= lim:
        if num % n == 0: return False
        if num % (n + 2) == 0: return False
        n += 6
    return True
# 5m -> 43
def isPrime_v2(num):
    # !!!! num >10, num not odd
    if num % 3 == 0: return False
    n = 5
    lim = int(math.sqrt(num)) + 1
    while n <= lim:
        if not num % n or not num % (n + 2): return False
        n += 6
    return True

# 5m -> 43
def isPrime_v3(num):
    # !!!! num >10, num not odd
    # if num % 3 == 0: return 0
    n = 5
    lim = int(math.sqrt(num)) + 1
    while n <= lim:
        if not num % n or not num % (n + 2): return 0
        n += 6
    return num

sum_of_primes = 17
count_primes = 4
i = 11
while i < number_limit:
    sum_of_primes += isPrime_v3(i)
    sum_of_primes += isPrime_v3(i+2)
    i += 6

print(str(count_primes) + " primes, its sum = " + str(sum_of_primes))

print ("time elapsed: {:.2f}s".format(time.time() - start_time))
"""result for 5 000 000 = 838596693108"""