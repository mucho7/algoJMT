import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [0]
for _ in range(n):
    coins.append(int(input()))

possible = [0 for _ in range(k + 1)]
possible[0] = 1

for coin in coins:
    for money in range(1, k + 1):
        if money - coin >= 0:
            possible[money] += possible[money - coin]

print(possible[k])