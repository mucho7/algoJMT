N = int(input())

some_some = [0 for _ in range(N+1)]
some_some[1] = 1

for idx in range(2, N+1):
    if idx % 2 == 0:
        some_some[idx] = 2 * some_some[idx - 1]
    else:
        some_some[idx] = 2 * some_some[idx - 1] + 1

ans = some_some[N] % 10007

if N % 2 == 0:
    print(ans + 1)
else:
    print(ans)

