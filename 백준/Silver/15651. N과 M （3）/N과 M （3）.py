from itertools import product

N, M = list(map(int, input().split()))

ans = product(range(1, N+1), repeat=M)

for per in ans:
    print(*per)