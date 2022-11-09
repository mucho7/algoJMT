def DFS(starting):
    if len(ans_list) == M:
        print(' '.join(map(str, ans_list)))
        return

    for i in range(starting, N + 1):
        ans_list.append(i)
        DFS(i)
        ans_list.pop()


N, M = map(int, input().split())

ans_list = []

DFS(1)