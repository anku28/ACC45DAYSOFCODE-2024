import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Input number of test cases
T = int(input().strip())

# For each test case, check primality and print result
for _ in range(T):
    N = int(input().strip())
    if is_prime(N):
        print("yes")
    else:
        print("no")
