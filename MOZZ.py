# Function to calculate maximum number of plates
def max_plates(T, test_cases):
    results = []
    for t in range(T):
        X, Y, R = test_cases[t]

        # Calculate the total sticks Chef ate
        extra_sticks = R // 30  # Calculate extra sticks from the money received
        total_sticks = X + extra_sticks  # Total sticks eaten

        # Calculate the maximum number of plates Chef ordered
        plates = (total_sticks + Y - 1) // Y  # Ceiling of total_sticks / Y
        results.append(plates)

    return results

# Input reading
T = int(input())
test_cases = []

for _ in range(T):
    test_cases.append(tuple(map(int, input().split())))

# Calculate results
results = max_plates(T, test_cases)

# Output results
for result in results:
    print(result)
