# Number of test cases
T = int(input())

# Loop through each test case
for _ in range(T):
    # Read the starting time X
    X = int(input())
    
    # Check if he can finish the assignments by 10 pm
    if X + 3 <= 10:
        print("Yes")
    else:
        print("No")