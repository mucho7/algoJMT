N, M = list(map(int, input().split()))
A_list = [list(map(int, input().split())) for _ in range(N)]
B_list = [list(map(int, input().split())) for _ in range(N)]

for y_idx in range(N):
    for idx in range(M):
        print(A_list[y_idx][idx] + B_list[y_idx][idx], end=" ")
    print()
    