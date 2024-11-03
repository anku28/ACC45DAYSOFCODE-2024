import sys
import math

def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    p = 2
    while p * p <= limit:
        if is_prime[p]:
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(2, limit + 1) if is_prime[p]]

def segmented_sieve(m, n):
    limit = int(math.sqrt(n)) + 1
    primes = sieve_of_eratosthenes(limit)
    
    size = n - m + 1
    is_prime = [True] * size
    
    for prime in primes:
        # Find the minimum number in the [m,n] range that is a multiple of `prime`
        start = max(prime * prime, m + (prime - m % prime) % prime)
        
        for j in range(start, n + 1, prime):
            is_prime[j - m] = False

    # Collecting all primes in the range
    result = []
    for i in range(size):
        if is_prime[i] and (m + i) > 1:  # Also ensure we don't include 1
            result.append(m + i)
    
    return result

def main():
    input = sys.stdin.read
    data = input().splitlines()
    
    t = int(data[0])
    results = []
    
    for i in range(1, t + 1):
        m, n = map(int, data[i].split())
        primes = segmented_sieve(m, n)
        results.append(primes)

    # Output the results
    output = []
    for primes in results:
        output.extend(map(str, primes))
        output.append("")  # Empty line between test cases
    
    # Join the output into a single string and print it, removing the last empty line
    sys.stdout.write("\n".join(output).strip() + "\n")

if __name__ == "__main__":
    main()
