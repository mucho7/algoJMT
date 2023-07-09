def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x_root = find(x)
    y_root = find(y)

    if x_root == y_root:
        return

    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    else:
        parent[y_root] = x_root
        rank[x_root] += 1


N, M = map(int, input().split())

parent = [i for i in range(N + 1)]
rank = [0] * (N + 1)

for _ in range(M):
    operator, a, b = map(int, input().split())

    if operator == 1:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
    elif operator == 0:
        union(a, b)
