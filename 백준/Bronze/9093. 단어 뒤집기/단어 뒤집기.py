num = int(input())

for _ in range(num):
    txt = input().split()
    for idx in txt:
        print(idx[::-1], end=' ')
