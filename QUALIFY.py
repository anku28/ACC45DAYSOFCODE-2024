# Number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read X, A, and B
    X, A, B = map(int, input().split())
    
    # Calculate the total score
    total_score = A + 2 * B
    
    # Check if Chef qualifies
    if total_score >= X:
        print("Qualify")
    else:
        print("NotQualify")
