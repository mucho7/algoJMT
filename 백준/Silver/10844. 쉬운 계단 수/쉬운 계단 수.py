N = int(input())

stair_list = [dict() for _ in range(N+1)]
stair_list[1] = {idx: 1 for idx in range(1, 10)}
stair_list[1][0] = 0

for idx in range(2, N+1):
    for num_key in range(10):
        if num_key == 0:
            stair_list[idx][num_key] = stair_list[idx - 1][num_key + 1]
        elif num_key == 9:
            stair_list[idx][num_key] = stair_list[idx - 1][num_key - 1]
        else:
            stair_list[idx][num_key] = stair_list[idx-1][num_key+1] + stair_list[idx - 1][num_key - 1]

print(sum(stair_list[N].values()) % 1000000000)

