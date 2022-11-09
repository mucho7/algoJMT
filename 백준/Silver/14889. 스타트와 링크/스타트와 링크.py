def status_sum(player):
    result = 0
    for A_1 in player:
        for A_2 in player:
            result += status_list[A_1][A_2]
    return result


N = int(input())

status_list = [list(map(int, input().split())) for _ in range(N)]
possible = list()

for chance in range(1, 1 << N):
    tmp = []
    for idx in range(N):
        if chance & (1 << idx):
            tmp.append(idx)
    if len(tmp) == N // 2 and len(tmp) != 0:
        for val in range(N):
            if val not in tmp:
                tmp.append(val)
        possible.append(tmp)

ans_list = []

for combination in range(len(possible) // 2):
    team_A = possible[combination][0:N//2]
    team_B = possible[combination][N//2:N]

    ans_list.append(abs(status_sum(team_A) - status_sum(team_B)))

print(min(ans_list))