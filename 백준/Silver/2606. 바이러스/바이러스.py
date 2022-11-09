def dfs(w):
    visited_list[w] = 1

    for tmp in range(computer + 1):
        if worm_list[w][tmp] == 1 and visited_list[tmp] == 0:
            dfs(tmp)



computer = int(input())
match = int(input())

worm_list = [[0 for _ in range(computer + 1)] for _ in range(computer + 1)]
visited_list = [0 for _ in range(computer + 1)]

for _ in range(match):
    G, S = map(int, input().split())
    worm_list[G][S] = 1
    worm_list[S][G] = 1

dfs(1)

ans = 0
for visit in visited_list:
    if visit == 1:
        ans += 1

# 숙주인 1번 컴퓨터는 세지 않는다
print(ans - 1)
