def DFS(some_sum, cnt):

    if cnt == N - 2:
        ans_list.append(some_sum)
        return

    for idx in range(1, N-1):
        if visited[idx] == 0:

            visited[idx] = 1

            n = m = 0
            while visited[idx - n]:
                n += 1
            front = ball_list[idx - n]

            while visited[idx + m]:
                m += 1
            back = ball_list[idx + m]

            some_sum += front * back
            cnt += 1

            DFS(some_sum, cnt)

            some_sum -= front * back
            visited[idx] = 0
            cnt -= 1


N = int(input())

ball_list = list(map(int, input().split()))
ans_list = []
energy_sum = 0

visited = [0 for _ in range(N)]

DFS(energy_sum, 0)

print(max(ans_list))
