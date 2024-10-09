def min_flips_to_unify_direction(test_cases):
    results = []
    for N, X in test_cases:
        # Calculate number of face-down cards
        face_down = N - X
        # Calculate minimum flips needed
        min_flips = min(X, face_down)
        results.append(min_flips)
    return results

# Input reading
T = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(T)]

# Get results and print
results = min_flips_to_unify_direction(test_cases)
for res in results:
    print(res)
