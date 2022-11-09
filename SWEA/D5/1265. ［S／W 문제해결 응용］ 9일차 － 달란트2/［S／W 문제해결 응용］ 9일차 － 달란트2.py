T = int(input())

for tc in range(1, T+1):
    N, P = list(map(int, input().split()))

    bunch_list = []

    tmp = N // P
    N -= tmp * P

    for _ in range(P):
        bunch_list.append(tmp)

    cur = 0
    while N != 0:
        bunch_list[cur] += 1
        cur += 1
        N -= 1

    ans = 1
    for value in bunch_list:
        ans = ans * value

    print(f'#{tc} {ans}')
