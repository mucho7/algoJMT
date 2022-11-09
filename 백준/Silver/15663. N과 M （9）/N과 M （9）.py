import sys
input = sys.stdin.readline


def DFS():

    visited_at_here = []

    if len(tmp_list) == M:
        print(*tmp_list)
        return

    for idx in range(len(num_list)):
        if visited[idx] == 0 and num_list[idx] not in visited_at_here:
            tmp_list.append(num_list[idx])
            visited_at_here.append(num_list[idx])
            visited[idx] = 1

            DFS()

            tmp_list.pop()
            visited[idx] = 0


N, M = list(map(int, input().split()))

num_list = sorted(list(map(int, input().split())))
visited = [0 for _ in range(N)]

tmp_list = []

DFS()