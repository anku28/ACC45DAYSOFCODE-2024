# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    N, X = map(int, input().split())  # Read N and X
    if X % N == 0:  # Check if X is divisible by N
        print("YES")
    else:
        print("NO")