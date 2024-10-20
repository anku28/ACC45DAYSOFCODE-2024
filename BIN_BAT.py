import math

# Function to calculate the total time for one test case
def total_time(N, A, B):
    # Calculate the number of rounds (log2(N))
    rounds = int(math.log2(N))
    
    # Calculate total time
    total_time = rounds * A + (rounds - 1) * B
    return total_time

# Input number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read N, A, B
    N, A, B = map(int, input().split())
    
    # Calculate and print the total time for this test case
    print(total_time(N, A, B))
