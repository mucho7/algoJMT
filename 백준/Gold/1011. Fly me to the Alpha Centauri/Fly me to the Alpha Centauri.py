N = int(input())

for _ in range(N):

    x, y = list(map(int, input().split()))
    distance = y - x
    ans = 0
    cur = 0
    velocity = 1

    while cur < distance:
        ans += 1
        velocity += 1
        cur += velocity // 2
        
    if distance == 1:
        print(1)
    else:
        print(ans)