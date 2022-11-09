import sys
import heapq
inf = 10 ** 20
input = sys.stdin.readline

V, E = list(map(int, input().split()))
K = int(input())

node_list = [[] for _ in range(V+1)]
visited = [inf for _ in range(V+1)]

for _ in range(E):
    start, end, distance = list(map(int, input().split()))

    node_list[start].append((distance, end))

pq = []
heapq.heappush(pq, (0, K))
visited[K] = 0

while pq:
    distance_to_node, node = heapq.heappop(pq)

    if visited[node] < distance_to_node:
        continue

    for nw, nx in node_list[node]:
        new_distance = distance_to_node + nw

        if visited[nx] > new_distance:
            visited[nx] = new_distance
            heapq.heappush(pq, (new_distance, nx))

for value in visited[1:]:
    if value == inf:
        print('INF')
    else:
        print(value)