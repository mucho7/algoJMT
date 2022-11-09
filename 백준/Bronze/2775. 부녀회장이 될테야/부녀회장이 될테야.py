T = int(input())

for _ in range(T):
    K = int(input())
    N = int(input())

    ans_list = [[idx for idx in range(N+1)] for _ in range(K+1)]

    for y_idx in range(1, K+1):
        for x_idx in range(1, N+1):
            ans_list[y_idx][x_idx] = sum(ans_list[y_idx-1][:x_idx+1])

    print(ans_list[K][N])