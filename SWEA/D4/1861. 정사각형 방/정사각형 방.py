def check(start, some_list):
    global ans

    some_list.append(start)
    if tree[start][1]:
        check(start + 1, some_list)

        if len(some_list) > len(ans):
            ans = some_list


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    N_list = [[0 for _ in range(N+2)] for _ in range(N + 2)]
    tree = [[idx, 0] for idx in range(pow(N, 2) + 1)]
    ans = []

    for idx in range(1, N + 1):
        N_list[idx] = [0]
        N_list[idx].extend(list(map(int, input().split())))
        N_list[idx].append(0)

    dxy = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    for y_idx in range(1, N + 1):
        for x_idx in range(1, N + 1):
            for direction in dxy:
                nx = x_idx + direction[1]
                ny = y_idx + direction[0]
                if N_list[y_idx][x_idx] + 1 == N_list[ny][nx]:
                    tree[N_list[y_idx][x_idx]][1] = N_list[ny][nx]

    for idx in range(1, pow(N, 2)+1):
        check(idx, [])

    print(f'#{tc} {ans[0]} {len(ans)}')
