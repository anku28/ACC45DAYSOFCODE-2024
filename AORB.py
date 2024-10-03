T=int(input())
for _ in range(T):
    X, Y = map(int, input().split()) 
    points_AB = (500 - 2 * X) + (1000 - 4 * (X + Y))

    points_BA = (1000 - 4 * Y) + (500 - 2 * (X + Y))

    print(max(points_AB, points_BA)) 
