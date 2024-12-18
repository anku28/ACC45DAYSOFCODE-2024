# Function to calculate the amount Chef needs to pay
def calculate_payment(A, B, C):
    # Find the lowest price among A, B, and C
    min_price = min(A, B, C)
    # Calculate total cost by excluding the lowest price
    total_cost = A + B + C - min_price
    return total_cost

# Read the number of test cases
T = int(input())
results = []

# Process each test case
for _ in range(T):
    # Read prices A, B, and C
    A, B, C = map(int, input().split())
    # Append the result for the current test case
    results.append(calculate_payment(A, B, C))

# Print all results for each test case
for result in results:
    print(result)
