T = int(input())  
for _ in range(T):
    N = int(input())
    coefficients = list(map(int, input().split())) 
    for i in range(N - 1, -1, -1):  
        if coefficients[i] != 0:
            degree = i
            break
    print(degree)  