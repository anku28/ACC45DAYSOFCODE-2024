# Function to find the maximum tastiness
def max_tastiness(T, test_cases):
    results = []
    for i in range(T):
        a, b, c, d = test_cases[i]
        # Calculate the maximum tastiness
        max_tasty = max(a + c, a + d, b + c, b + d)
        results.append(max_tasty)
    return results

# Input and Output handling
T = int(input())  # Number of test cases
test_cases = [list(map(int, input().split())) for _ in range(T)]

# Get the results
results = max_tastiness(T, test_cases)

# Print the results
for result in results:
    print(result)
