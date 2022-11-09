N = int(input())
making_list = [0] * (N + 1)

for idx in range(2, N + 1):
    making_list[idx] = making_list[idx - 1] + 1
    if idx % 3 == 0:
        div_3 = making_list[idx // 3] + 1
        making_list[idx] = min(div_3,making_list[idx])
    if idx % 2 == 0:
        div_2 = making_list[idx // 2] + 1
        making_list[idx] = min(div_2, making_list[idx])

print(making_list[N])