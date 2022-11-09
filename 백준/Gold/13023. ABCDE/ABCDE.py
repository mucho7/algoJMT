import sys
input = sys.stdin.readline


def DFS(starting, cnt):
    visited[starting] = 1

    if cnt == 4:
        return True

    for dfs_idx in friends[starting]:
        if visited[dfs_idx] == 0:
            if DFS(dfs_idx, cnt + 1):
                return True
            visited[dfs_idx] = 0
    visited[starting] = 0
    return


N, M = list(map(int, input().split()))

friends = [[] for _ in range(N)]
visited = [0 for _ in range(N)]

for _ in range(M):
    X, Y = list(map(int, input().split()))
    friends[X].append(Y)
    friends[Y].append(X)

friend_length = 0

ans = False

for idx in range(N):
    if DFS(idx, friend_length):
        ans = True
        break

if ans:
    print(1)
else:
    print(0)