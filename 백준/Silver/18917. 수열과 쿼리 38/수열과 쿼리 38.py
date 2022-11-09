import sys
input = sys.stdin.readline


N = int(input())

N_dict = dict()
dict_sum = dict_xor = 0

for _ in range(N):
    order = list(map(int, input().split()))

    if order[0] == 1:
        if N_dict.get(order[1]) is not None:
            N_dict[order[1]] += 1
        else:
            N_dict[order[1]] = 1
        dict_sum += order[1]
        dict_xor ^= order[1]

    elif order[0] == 2:
        N_dict[order[1]] -= 1
        dict_sum -= order[1]
        dict_xor ^= order[1]

    elif order[0] == 3:
        print(dict_sum)

    elif order[0] == 4:
        print(dict_xor)