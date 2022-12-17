import sys
sys.setrecursionlimit(10**6)


def normal(x_idx: int, y_idx: int, color: chr, depth: int):

    for direc in dxy:
        nx, ny = x_idx + direc[0], y_idx + direc[1]
        if 0 <= nx < N and 0 <= ny < N:
            if not visited[ny][nx] and image[ny][nx] == color:
                visited[ny][nx] = depth
                normal(nx, ny, color, depth)


def rg_eye(x_idx: int, y_idx: int, color: chr, depth: int):
    if color == 'R' or color == 'G':
        for direc in dxy:
            nx, ny = x_idx + direc[0], y_idx + direc[1]
            if 0 <= nx < N and 0 <= ny < N:
                if not rg_visited[ny][nx]:
                    if image[ny][nx] == 'R' or image[ny][nx] == 'G':
                        rg_visited[ny][nx] = depth
                        rg_eye(nx, ny, color, depth)

    else:
        for direc in dxy:
            nx, ny = x_idx + direc[0], y_idx + direc[1]
            if 0 <= nx < N and 0 <= ny < N:
                if not rg_visited[ny][nx] and image[ny][nx] == 'B':
                    rg_visited[ny][nx] = depth
                    rg_eye(nx, ny, color, depth)



N = int(input())

image = []
for _ in range(N):
    image.append(input())

dxy = [[1, 0], [-1, 0], [0, 1], [0, -1]]
visited = [[0 for _ in range(N)] for _ in range(N)]
rg_visited = [[0 for _ in range(N)] for _ in range(N)]

dep = 1
rg_dep = 1

for y in range(N):
    for x in range(N):
        if not visited[y][x]:
            visited[y][x] = dep
            normal(x, y, image[y][x], dep)
            dep += 1
        if not rg_visited[y][x]:
            rg_visited[y][x] = rg_dep
            rg_eye(x, y, image[y][x], rg_dep)
            rg_dep += 1

print(dep - 1)
print(rg_dep - 1)