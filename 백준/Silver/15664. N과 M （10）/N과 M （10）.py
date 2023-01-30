from itertools import combinations 

N, M = list(map(int, input().split()))
num_set = sorted(list(map(int, input().split())))

answers = set(combinations(num_set, M))

for ans in sorted(answers):
    print(*ans)