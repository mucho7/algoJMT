import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))

tree_list = list(map(int, input().split()))
sonamu = max(tree_list)

top = sonamu
bottom = 0


while top >= bottom:

    cur = (top + bottom) // 2

    cut_sum = 0
    for height in tree_list:
        if height - cur > 0:
            cut_sum += height - cur

    if cut_sum >= M:
        bottom = cur + 1

    elif cut_sum < M:
        top = cur - 1

print(top)