import math

# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read N and X
    N, X = map(int, input().split())
    
    # Read the health points of the enemies
    health_points = list(map(int, input().split()))
    
    # Calculate time required in single-target mode
    time_single_target = sum(math.ceil(h / X) for h in health_points)
    
    # Calculate time required in multi-target mode
    time_multi_target = max(health_points)
    
    # Output the minimum time required
    print(min(time_single_target, time_multi_target))
