import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def DFS(starting):

    for val in tree[starting]:
        if ans[val] == 0:
            ans[val] = starting
            DFS(val)


N = int(input())

tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    X, Y = map(int, input().split())

    tree[X].append(Y)
    tree[Y].append(X)

ans = [0] * (N+1)
ans[1] = 1
DFS(1)

for idx in range(2, N+1):
    print(ans[idx])