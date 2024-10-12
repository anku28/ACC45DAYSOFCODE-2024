# Input handling
A, B, C, X = map(int, input().split())

# Check if X is one of the prepared topics
if X == A or X == B or X == C:
    print("Yes")
else:
    print("No")
