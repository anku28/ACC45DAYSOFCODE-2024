# Read number of test cases
T = int(input())

results = []
for _ in range(T):
    # Read the value of N for each test case
    N = int(input())
    
    # Check if N is a multiple of 4
    if N % 4 == 0:
        results.append("Good")
    else:
        results.append("Not Good")

# Output results for each test case
for result in results:
    print(result)
