from itertools import combinations

def findDistance(x_idx:int, y_idx:int):
    """우리 집에서 치킨집까지의 거리를 저장한 리스트"""
    result = []
    for chicken_x, chicken_y in chicken_house:
        dis = abs(chicken_x - x_idx) + abs(chicken_y - y_idx)
        result.append(dis)
    distance.append(result)


N, M = list(map(int, input().split()))
chicken_house = []
graph = []
distance = []

for y_idx in range(N):
    row = list((map(int, input().split())))
    graph.append(row)

    for x_idx in range(N):
        if row[x_idx] == 2:
            chicken_house.append([x_idx, y_idx])

for y_idx in range(N):
    for x_idx in range(N):
        if graph[y_idx][x_idx] == 1:
            findDistance(x_idx, y_idx)

combi = combinations(range(len(chicken_house)), M)

ans = 9999
for combo in combi:
    result = 0
    for house in range(len(distance)):
        minimum_lenth = 99
        for idx in range(len(chicken_house)):
            if idx in combo:
                if minimum_lenth > distance[house][idx]:
                    minimum_lenth = distance[house][idx]
        result += minimum_lenth
    if ans > result:
        ans = result
print(ans)