# N 기타, M 곡
N, M = list(map(int, input().split()))
guitar_song = dict()

max_yes = 0
min_guitar = [[] for _ in range(M + 1)]

possible = []

for _ in range(N):
    guitar, song = input().split()
    guitar_song[guitar] = list(song)

for cha in range(1 << N):
    tmp = []
    for idx in range(N):
        if cha & (1 << idx):
            tmp.append(list(guitar_song.keys())[idx])
    possible.append(tmp)

for combo in possible:

    song_check = list('N' * M)
    yes_num = 0

    for guitar_key in combo:
        for idx in range(M):
            if guitar_song.get(guitar_key)[idx] == 'Y' and song_check[idx] == 'N':
                song_check[idx] = 'Y'
                yes_num += 1

    if max_yes <= yes_num:
        max_yes = yes_num
        min_guitar[max_yes].append(len(combo))

for idx in range(M, 0, -1):
    if min_guitar[idx]:
        print(min(min_guitar[idx]))
        break
else:
    print(-1)