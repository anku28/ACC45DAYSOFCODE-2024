# Read number of test cases
T = int(input())

results = []
for _ in range(T):
    # Read initial score A and B
    A, B = map(int, input().split())
    # Read target score C and D
    C, D = map(int, input().split())
    
    # Check if target score is achievable
    if C >= A and D >= B:
        results.append("POSSIBLE")
    else:
        results.append("IMPOSSIBLE")

# Output all results for each test case
for result in results:
    print(result)
