# Number of test cases
T = int(input())

for _ in range(T):
    # Read the referee decisions as a list of integers
    R = list(map(int, input().split()))
    
    # Check if all referees agree that the ball is inside (all 0's)
    if all(r == 0 for r in R):
        print("IN")
    else:
        print("OUT")
