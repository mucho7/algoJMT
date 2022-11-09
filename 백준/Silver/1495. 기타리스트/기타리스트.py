N, S, M = list(map(int, input().split()))

modify_list = list(map(int, input().split()))

volume = [0 for _ in range(M+1)]

volume[S] = 1

for modify in modify_list:

    tmp_volume = [0 for _ in range(M+1)]

    for idx in range(M+1):
        if volume[idx]:

            if idx - modify >= 0:
                tmp_volume[idx - modify] = 1

            if idx + modify <= M:
                tmp_volume[idx + modify] = 1

    volume = tmp_volume.copy()

for idx in range(M, -1, -1):
    if volume[idx]:
        print(idx)
        break
else:
    print(-1)

