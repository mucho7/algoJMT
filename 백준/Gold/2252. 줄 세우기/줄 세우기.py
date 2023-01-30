from collections import deque 

N, M = list(map(int, input().split()))
N_list = [[] for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]
temp_que = deque([])
ans = []

for _ in range(M):
    start, target = list(map(int, input().split()))
    N_list[start].append(target)
    visited[target] += 1

for idx in range(1, N+1):
    if not visited[idx]:
        temp_que.append(idx)

while temp_que:
    target = temp_que.popleft()
    ans.append(target)
    for idx in N_list[target]:
        visited[idx] -= 1
        if not visited[idx]:
            temp_que.append(idx)
            
for num in ans:
    print(num, end=" ")