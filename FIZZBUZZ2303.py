# Read number of test cases
T = int(input())

results = []
for _ in range(T):
    # Read the value of N
    N = int(input())
    
    # Calculate possible choices of captain and vice-captain
    choices = N * (N - 1)
    
    # Store result for the test case
    results.append(choices)

# Output all results for each test case
for result in results:
    print(result)
