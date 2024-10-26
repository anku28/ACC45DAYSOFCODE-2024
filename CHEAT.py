def count_tuesdays(N):
  
    count = 0
    day = 2  
    while day <= N:
        count += 1
        day += 7
    return count


T = int(input())
results = []

for _ in range(T):
    
    N = int(input())
    results.append(count_tuesdays(N))


print("\n".join(map(str, results)))
