thing_list = list(map(int, input().split()))

perfect = [1, 1, 2, 2, 2, 8]

for idx in range(6):
    print(perfect[idx] - thing_list[idx], end=" ")