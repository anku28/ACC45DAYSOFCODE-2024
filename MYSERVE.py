# Number of test cases
T = int(input())

results = []
for _ in range(T):
    # Read P and Q
    P, Q = map(int, input().split())
    
    # Calculate total points and determine the serve pair
    total_points = P + Q
    serve_pair = total_points // 2
    
    # Determine whose serve it is
    if serve_pair % 2 == 0:
        results.append("Alice")
    else:
        results.append("Bob")

# Output each result for the test cases
for result in results:
    print(result)
