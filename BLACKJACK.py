# Number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read the values of A and B
    A, B = map(int, input().split())
    
    # Calculate the required value of C
    C = 21 - (A + B)
    
    # Check if C is within the valid range [1, 10]
    if 1 <= C <= 10:
        print(C)
    else:
        print(-1)