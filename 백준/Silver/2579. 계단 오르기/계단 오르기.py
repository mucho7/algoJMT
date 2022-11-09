stair_len = int(input())

stair_list = [0 for _ in range(stair_len + 1)]
ans = [0 for _ in range(stair_len + 1)]


for idx in range(1, stair_len + 1):
    stair_list[idx] = int(input())

if stair_len == 1:
    print(stair_list[1])
elif stair_len == 2:
    print(stair_list[1] + stair_list[2])
else:
    ans[1] = stair_list[1]
    ans[2] = stair_list[1] + stair_list[2]
    ans[3] = max(stair_list[1] + stair_list[3], stair_list[2] + stair_list[3])

    for idx in range(4, stair_len + 1):
        ans[idx] = max(ans[idx - 3] + stair_list[idx - 1] + stair_list[idx], ans[idx - 2] + stair_list[idx])


    print(ans[stair_len])