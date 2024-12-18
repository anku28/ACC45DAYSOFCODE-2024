def chef_and_his_apps(test_cases):
    results = []
    for S, X, Y, Z in test_cases:
        free_space = S - (X + Y)
        
        if free_space >= Z:
            # No app needs to be deleted
            results.append(0)
        else:
            space_needed = Z - free_space
            if X >= space_needed or Y >= space_needed:
                # Deleting one app is sufficient
                results.append(1)
            else:
                # Both apps need to be deleted
                results.append(2)
    return results

# Input handling
T = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(T)]

# Processing and Output
results = chef_and_his_apps(test_cases)
print("\n".join(map(str, results)))
