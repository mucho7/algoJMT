def DFS(starting):

    if len(ans_list) == M:
        print(' '.join(map(str, ans_list)))
        return

    for idx in range(len(num_list)):
        if visited[idx] == 0:
            ans_list.append(num_list[idx])
            visited[idx] = 1

            DFS(num_list[idx])

            ans_list.pop()
            visited[idx] = 0


N, M = map(int, input().split())

num_list = sorted(list(map(int, input().split())))
visited = [0 for _ in range(N)]

ans_list = []

DFS(0)