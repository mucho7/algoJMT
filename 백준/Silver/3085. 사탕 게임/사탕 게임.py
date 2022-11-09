def count_candy():
    row_cnt, col_cnt, row_max, col_max = 1, 1, 0, 0

    for y_idx in range(N):
        for x_idx in range(N):
            if table[y_idx][x_idx] == table[y_idx][x_idx + 1]:
                row_cnt += 1
            else:
                row_cnt = 1
            row_max = max(row_cnt, row_max)

            if table[x_idx][y_idx] == table[x_idx + 1][y_idx]:
                col_cnt += 1
            else:
                col_cnt = 1
            col_max = max(col_cnt, col_max)

        row_cnt = col_cnt = 1

    return max(row_max, col_max)


N = int(input())
table = [list(input() + '0') for _ in range(N)]
table.append(list('0' * (N+1)))

dxy = [[1, 0], [-1, 0], [0, 1], [0, -1]]

ans = 0
tmp1 = tmp2 = 0

for y_idx in range(N):
    for x_idx in range(N):
        for direction in dxy:
            nx = x_idx + direction[0]
            ny = y_idx + direction[1]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            if table[y_idx][x_idx] != table[ny][nx]:
                table[ny][nx], table[y_idx][x_idx] = table[y_idx][x_idx], table[ny][nx]

                ans = max(ans, count_candy())

                table[y_idx][x_idx], table[ny][nx] = table[ny][nx], table[y_idx][x_idx]

print(ans)