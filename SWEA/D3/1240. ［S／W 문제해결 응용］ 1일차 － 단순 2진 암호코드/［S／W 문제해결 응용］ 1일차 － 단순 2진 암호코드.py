T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    dummy = [list(map(int, input())) for _ in range(N)]
    first_x = first_y = 0

    password_list = [[0, 0, 0, 1, 1, 0, 1], [0, 0, 1, 1, 0, 0, 1], [0, 0, 1, 0, 0, 1, 1], [0, 1, 1, 1, 1, 0, 1],
                     [0, 1, 0, 0, 0, 1, 1], [0, 1, 1, 0, 0, 0, 1], [0, 1, 0, 1, 1, 1, 1], [0, 1, 1, 1, 0, 1, 1],
                     [0, 1, 1, 0, 1, 1, 1], [0, 0, 0, 1, 0, 1, 1]]

    password_sum = 0
    password_check = 0

    for y_idx in range(N):
        for x_idx in range(M-1, -1, -1):
            if dummy[y_idx][x_idx]:
                first_x, first_y = x_idx - 55, y_idx
                break
        if first_x:
            break

    for word_idx in range(8):
        tmp_list = []

        for idx in range(7):
            tmp_list.append(dummy[first_y][first_x + idx + word_idx * 7])

        for ch in range(10):
            if tmp_list == password_list[ch]:
                password_sum += ch

                if word_idx % 2:
                    password_check += ch
                else:
                    password_check += 3 * ch

    if not password_check % 10:
        print(f'#{tc} {password_sum}')
    else:
        print(f'#{tc} 0')