import sys
import heapq
input = sys.stdin.readline


def dijkstra(starting):
    pq = []
    heapq.heappush(pq, (0, starting))
    visited[starting] = 0

    while pq:
        distance, node = heapq.heappop(pq)

        if visited[node] < distance:
            continue

        for nw, nx in linked[node]:
            distance_node = distance + nw

            if visited[nx] > distance_node:
                heapq.heappush(pq, (distance_node, nx))
                visited[nx] = distance_node


N = int(input())
M = int(input())

inf = 10 ** 13

linked = [[] for _ in range(N + 1)]
visited = [inf for _ in range(N+1)]

for _ in range(M):
    start, end, cost = list(map(int, input().split()))

    linked[start].append((cost, end))

start, end = list(map(int, input().split()))

dijkstra(start)

print(visited[end])
