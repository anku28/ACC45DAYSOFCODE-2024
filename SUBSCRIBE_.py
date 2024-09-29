# Number of test cases
T = int(input())

# Loop through each test case
for _ in range(T):
    # Read the number of friends and the cost of one subscription
    N, X = map(int, input().split())
    
    # Calculate the number of subscriptions needed
    subscriptions = (N + 5) // 6
    
    # Calculate the total cost
    total_cost = subscriptions * X
    
    # Output the total cost for this test case
    print(total_cost)
