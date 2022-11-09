def pick4(n, picked, to_pick):
    if to_pick == 0:
        possible_list.append(list(picked))
        return

    for idx in range(N):
        if tmp_list[idx]:
            picked.append(n[idx])
            tmp_list[idx] = 0
            pick4(n, picked, to_pick - 1)
            picked.pop()
            tmp_list[idx] = 1


def sub(some_list):
    result = 0
    for idx in range(1, N):
        result += abs(some_list[idx] - some_list[idx - 1])

    return result


N = int(input())

nums = list(map(int, input().split()))

possible_list = []
tmp_list = [1] * 9

pick4(nums, [], N)

ans_list = []

for idx_pack in possible_list:
    ans_list.append(sub(idx_pack))

print(max(ans_list))