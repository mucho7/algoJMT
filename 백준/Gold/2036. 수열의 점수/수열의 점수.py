N = int(input())
pos = []
nag = []
one = []
ans = 0

for _ in range(N):
    num = int(input())
    if num > 1:
        pos.append(num)
    elif num <= 0:
        nag.append(num)
    else:
        one.append(num)

pos.sort(reverse=True)
nag.sort()

if len(pos) % 2 == 0:
    for i in range(0, len(pos), 2):
        ans += pos[i] * pos[i+1]
else:
    for i in range(0, len(pos)-1, 2):
        ans += pos[i] * pos[i+1]
    ans += pos[-1]

if len(nag) % 2 == 0:
    for i in range(0, len(nag), 2):
        ans += nag[i] * nag[i+1]
else:
    for i in range(0, len(nag)-1, 2):
        ans += nag[i] * nag[i+1]
    ans += nag[-1]

ans += sum(one)

print(ans)