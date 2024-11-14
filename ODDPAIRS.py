T = int(input())
results = []

for _ in range(T):
    N = int(input())
    
    odds = (N + 1) // 2
    evens = N // 2     
    
    pairs = odds * evens * 2
    
    results.append(pairs)

print("\n".join(map(str, results)))