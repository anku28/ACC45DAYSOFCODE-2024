# Number of test cases
T = int(input())

results = []
for _ in range(T):
    # Read N and K
    N, K = map(int, input().split())
    
    # Read the list of minion characteristics
    characteristics = list(map(int, input().split()))
    
    # Count Wolverine-like minions
    count = 0
    for characteristic in characteristics:
        # Add K and check if divisible by 7
        if (characteristic + K) % 7 == 0:
            count += 1
    
    # Store result for the test case
    results.append(count)

# Output all results for each test case
for result in results:
    print(result)
