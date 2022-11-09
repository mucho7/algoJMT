N, S = list(map(int, input().split()))

pan_list = list(map(int, input().split()))

ans_list = []

for chance in range(1, 1 << N):
    tmp = []
    for idx in range(N):
        if chance & (1 << idx):
            tmp.append(pan_list[idx])
    if sum(tmp) == S:
        ans_list.append(tmp)

print(len(ans_list))