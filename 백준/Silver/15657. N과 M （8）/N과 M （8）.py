def DFS(starting):

    if len(ans_list) == M:
        print(' '.join(map(str, ans_list)))
        return

    for idx in range(starting, len(num_list)):
        ans_list.append(num_list[idx])

        DFS(idx)

        ans_list.pop()


N, M = map(int, input().split())

num_list = sorted(list(map(int, input().split())))

ans_list = []

DFS(0)