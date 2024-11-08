# Read number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read the length of the array
    N = int(input())
    # Read the array elements
    A = list(map(int, input().split()))
    
    # Calculate the initial sum of the array
    sum_A = sum(A)
    
    # Check if it's possible to make the sum zero
    if sum_A % 2 != 0:
        # If sum is odd, it's not possible to make it zero
        print(-1)
    else:
        # Calculate the minimum number of flips
        print(abs(sum_A) // 2)
