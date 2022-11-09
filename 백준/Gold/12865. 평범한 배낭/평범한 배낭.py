N, K = list(map(int, input().split()))

things = [[0, 0]]
for _ in range(N):
    things.append(list(map(int, input().split())))

some_list = [[0 for _ in range(K+1)]for _ in range(N+1)]

for thing in range(1, N+1):
    for mass in range(K+1):
        weight = things[thing][0]
        value = things[thing][1]
        if things[thing][0] <= mass:
            some_list[thing][mass] = max(some_list[thing - 1][mass], some_list[thing - 1][mass - things[thing][0]] + things[thing][1])
        else:
            some_list[thing][mass] = some_list[thing - 1][mass]

print(some_list[N][K])
