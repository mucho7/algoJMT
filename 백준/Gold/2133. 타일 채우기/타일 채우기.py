N = int(input())

tile_list = [0] * (N + 1)

if N % 2 == 1:
    print(0)
else:
    tile_list[2] = 3
    for idx in range(4, N+1, 2):
        tile_list[idx] += tile_list[2] * tile_list[idx - 2]
        tmp = idx - 4
        while tmp != 0:
            tile_list[idx] += 2 * tile_list[tmp]
            tmp -= 2
        tile_list[idx] += 2

    print(tile_list[N])