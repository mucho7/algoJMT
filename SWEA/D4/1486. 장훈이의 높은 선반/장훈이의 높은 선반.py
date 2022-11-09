T = int(input())

for tc in range(1, T+1):
    N, B = list(map(int, input().split()))

    height_list = list(map(int, input().split()))

    ans = sum(height_list) - B

    possible = []
    # 비트연산이 필요
    for idx_1 in range(1 << N):
        tmp_list = []
        for idx_2 in range(N):
            if idx_1 & (1 << idx_2):
                tmp_list.append(height_list[idx_2])
        possible.append(sum(tmp_list))

    max_possibility = 0
    for possibility in possible:
        if ans >= possibility > max_possibility:
            max_possibility = possibility

    ans = ans - max_possibility

    print(f'#{tc} {ans}')
