def min_attacks_needed(H, X, Y):
    # Option 1: Use only normal attacks
    normal_attacks_only = (H + X - 1) // X  # This ensures we round up the division
    
    # Option 2: Use the special attack once, then normal attacks
    if Y >= H:
        special_attack_used = 1  # If the special attack alone can reduce health to 0 or less
    else:
        remaining_health = H - Y
        normal_attacks_after_special = (remaining_health + X - 1) // X  # Rounding up
        special_attack_used = 1 + normal_attacks_after_special
    
    # Return the minimum of the two options
    return min(normal_attacks_only, special_attack_used)

# Input handling
T = int(input())  # Number of test cases
for _ in range(T):
    H, X, Y = map(int, input().split())
    print(min_attacks_needed(H, X, Y))
