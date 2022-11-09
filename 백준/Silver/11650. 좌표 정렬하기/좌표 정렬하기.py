N = int(input())

coordinates = dict()

for _ in range(N):
    tmp = list(map(int, input().split()))

    if coordinates.get(tmp[0]) is None:
        coordinates[tmp[0]] = list()
        coordinates[tmp[0]].append(tmp[1])
    else:
        coordinates[tmp[0]].append(tmp[1])

for key in sorted(coordinates.keys()):
    for value in sorted(coordinates[key]):
        print(f'{key} {value}')

