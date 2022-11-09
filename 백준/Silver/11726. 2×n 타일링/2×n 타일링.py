n = int(input())
tile_list = [0] * (n + 1)

for idx in range(n+1):
    if idx < 2:
        tile_list[idx] = 1
    else:
        tile_list[idx] = tile_list[idx - 1] + tile_list[idx - 2]


print(tile_list[n] % 10007)
