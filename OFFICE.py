# cook your dish here
# Input number of test cases
T = int(input())

# Loop through each test case
for _ in range(T):
    # Input the values of X and Y
    X, Y = map(int, input().split())
    
    # Calculate the total working hours in one week
    total_hours = 4 * X + Y
    
    # Output the result
    print(total_hours)
