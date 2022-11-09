from math import factorial

N = int(input())

if N == 3:
    print(0)
else:
    ans = factorial(N) // (factorial(4) * factorial(N-4))
    print(ans)


