import sys
import heapq

input = sys.stdin.readline

V, E = map(int, input().split())
edge_list = [[] for _ in range(V + 1)]
visited = [0 for _ in range(V + 1)]
heap = [[0, 1]]

ans = 0
cnt = 0

for _ in range(E):
    start, end, dist = map(int, input().split())
    edge_list[start].append([dist, end])
    edge_list[end].append([dist, start])


while True:
    if cnt == V:
        break

    dist, start  = heapq.heappop(heap)

    if not visited[start]:
        visited[start] = 1
        ans += dist
        cnt += 1
        
        for edge in edge_list[start]:
            heapq.heappush(heap, edge)

print(ans)