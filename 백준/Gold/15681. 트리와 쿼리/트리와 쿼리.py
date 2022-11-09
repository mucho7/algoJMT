import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def DFS(starting):
  visited[starting] = 1

  for node in graph[starting]:
    if not visited[node]:
      DFS(node)
      subtree[starting] += subtree[node]
      visited[node] = 0


N, R, Q = list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
subtree = [1 for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for _ in range(N-1):
  U, V = list(map(int, input().split()))
  graph[U].append(V)
  graph[V].append(U)

DFS(R)

for _ in range(Q):
  target_node = int(input())
  print(subtree[target_node])
  
