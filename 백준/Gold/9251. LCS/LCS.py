first = input()
second = input()

ans = [[0 for _ in range(len(second) + 1)] for _ in range(len(first) + 1)]

for first_idx in range(1, len(first) + 1):
    for second_idx in range(1, len(second) + 1):
        ans[first_idx][second_idx] = max(ans[first_idx][second_idx - 1], ans[first_idx - 1][second_idx])

        if first[first_idx - 1] == second[second_idx - 1]:
            ans[first_idx][second_idx] = ans[first_idx - 1][second_idx - 1] + 1

print(ans[-1][-1])
