T = int(input())
results = []

for _ in range(T):
    X, Y = map(int, input().split())
    
    water_needed_per_person = 2 * Y
    
    if water_needed_per_person > 0:
        max_people = X // water_needed_per_person
    else:
        max_people = 0
    
    results.append(max_people)

print("\n".join(map(str, results)))