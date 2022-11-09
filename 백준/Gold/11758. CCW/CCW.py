P1 = list(map(int, input().split()))
P2 = list(map(int, input().split()))
P3 = list(map(int, input().split()))

dx_12 = P2[0] - P1[0]
dy_12 = P2[1] - P1[1]

dx_23 = P3[0] - P2[0]
dy_23 = P3[1] - P2[1]

ans = dx_12 * dy_23 - dy_12 * dx_23

if ans > 0:
    print(1)
elif ans < 0:
    print(-1)
else:
    print(0)