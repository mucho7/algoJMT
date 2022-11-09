N, M = map(int, input().split())

depth = N - M + 1
cur_for_depth = 0

for leaf in range(1, N):
    if cur_for_depth < depth:
        print(f'{cur_for_depth} {leaf}')
        cur_for_depth += 1
    else:
        print(f'{cur_for_depth - 1} {leaf}')

