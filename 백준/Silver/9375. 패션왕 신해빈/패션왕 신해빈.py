T = int(input())

for _ in range(T):
    N = int(input())

    fashion = dict()

    for _ in range(N):
        name, cloth = input().split()
        if fashion.get(cloth) is None:
            fashion[cloth] = 1
        else:
            fashion[cloth] += 1

    ans = 1
    for cloth_type in fashion.values():
        ans = ans * (cloth_type + 1)

    print(ans - 1)
