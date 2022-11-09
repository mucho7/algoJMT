T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    num = 1
    while True:
        tmp = num * num * num

        if tmp == N:
            print(f'#{tc} {num}')
            break
        elif tmp > N:
            print(f'#{tc} -1')
            break

        num += 1
