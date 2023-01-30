T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = list(map(int, input().split()))

    distance = (abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2) ** (1/ 2)

    radius = r1 + r2 

    # 원이 원을 품은 케이스를 정리할 수 없음
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    elif distance > radius:
        print(0)
        
    elif distance == radius:
        print(1)
    elif distance < radius:
        if r1 > distance + r2 or r2 > distance + r1:
            print(0)
        elif r1 == distance + r2 or r2 == distance + r1:
            print(1)
        else:
            print(2)