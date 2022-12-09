from collections import deque


def pour(x, y):
    if not visited[x][y]:
        visited[x][y] = True
        possible.append((x, y))


def BFS():
    while possible:
        x, y = possible.popleft()
        z = C - x - y

        if x == 0:
            answer.append(z)

        # x -> y
        water = min(x, B - y)
        pour(x - water, y + water)
        # x -> z
        water = min(x, C - z)
        pour(x - water, y)

        # y -> x
        water = min(y, A - x)
        pour(x + water, y - water)
        # y -> z
        water = min(y, C - z)
        pour(x, y - water)

        # z -> x
        water = min(z, A - x)
        pour(x + water, y)
        # z -> y
        water = min(z, B - y)
        pour(x, y + water)


A, B, C = map(int, input().split())

possible = deque()
possible.append((0, 0))

visited = [[0 for _ in range(B + 1)] for _ in range(A + 1)]
visited[0][0] = True

answer = []

BFS()

# 출력
answer.sort()
for ans in answer:
    print(ans, end=' ')