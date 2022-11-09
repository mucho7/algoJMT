import sys
sys.setrecursionlimit(10 ** 5)


def VFD(x_idx, y_idx, check):
    for direction in dxy:
        ny = y_idx + direction[0]
        nx = x_idx + direction[1]
        if farm[ny][nx] and [nx, ny] not in visited:
            visited.append([nx, ny])
            VFD(nx, ny, check)
            check = True
    return check


T = int(input())

for _ in range(T):
    # M : 배추밭의 가로
    # N : 배추밭의 세로
    # K : 배추의 수
    M, N, K = map(int, input().split())

    farm = [[0 for _ in range(M+2)] for _ in range(N+2)]
    visited = []
    near = []

    for _ in range(K):
        X, Y = map(int, input().split())
        farm[Y + 1][X + 1] = 1
        near.append([X, Y])

    dxy = [[1, 0], [-1, 0], [0, 1], [0, -1], [0, 0]]

    ans = 0
    is_visit = False

    for y_idx in range(1, N + 1):
        for x_idx in range(1, M + 1):
            if farm[y_idx][x_idx]:
                if VFD(x_idx, y_idx, is_visit):
                    ans += 1
    print(ans)