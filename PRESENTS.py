# Function to calculate the minimum coins required
def minimum_coins(n):
    groups = n // 5          # Number of complete groups of 5 gifts
    remaining = n % 5        # Remaining gifts after complete groups
    return 4 * groups + remaining

# Read the number of test cases
T = int(input())
results = []

# Process each test case
for _ in range(T):
    N = int(input())
    results.append(minimum_coins(N))

# Output all results
for result in results:
    print(result)
