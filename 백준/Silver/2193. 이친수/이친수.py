N = int(input())

pinary = [1] * (N + 1)

for idx in range(N+1):
    if idx < 3:
        pinary[idx] = 1
    else:
        pinary[idx] = pinary[idx - 1] + pinary[idx - 2]

print(pinary[N])