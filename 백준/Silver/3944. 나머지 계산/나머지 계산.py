import sys
input = sys.stdin.readline

num = int(input())
for _ in range(num):
    b, mine = input().split()
    b = int(b)
    ans = 0

    ans = sum(map(int, list(mine))) % (b-1)

    print(ans)