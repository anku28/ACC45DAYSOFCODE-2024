T = int(input())

for _ in range(T):
    N = int(input())
    
    contests = input().split()
    
    start38_count = contests.count("START38")
    ltime108_count = contests.count("LTIME108")
    
    print(start38_count,ltime108_count)