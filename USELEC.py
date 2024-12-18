# Function to determine if candidate A can win the election
def can_candidate_a_win(n, x, votes_a, votes_b):
    required_wins = (n // 2) + 1
    
    # Count initial wins for candidate A
    initial_wins = sum(1 for i in range(n) if votes_a[i] > votes_b[i])
    
    # If candidate A already has enough wins, return "YES"
    if initial_wins >= required_wins:
        return "YES"
    
    # Calculate deficits where candidate B is winning
    deficits = []
    for i in range(n):
        if votes_a[i] <= votes_b[i]:  # Candidate B is winning in this state
            deficit = votes_b[i] - votes_a[i] + 1
            deficits.append(deficit)
    
    # Sort deficits in ascending order
    deficits.sort()
    
    # Try to flip states in favor of A using the extra votes
    current_wins = initial_wins
    for deficit in deficits:
        if x >= deficit:
            x -= deficit
            current_wins += 1
            if current_wins >= required_wins:
                return "YES"
        else:
            break
    
    return "NO"

# Read input and process each test case
T = int(input())
results = []
for _ in range(T):
    # Read N and X
    N, X = map(int, input().split())
    # Read votes for candidates A and B
    votes_a = list(map(int, input().split()))
    votes_b = list(map(int, input().split()))
    # Append result for the current test case
    results.append(can_candidate_a_win(N, X, votes_a, votes_b))

# Output all results
print("\n".join(results))
