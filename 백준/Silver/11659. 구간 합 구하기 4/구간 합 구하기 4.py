import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))

N_list = list(map(int, input().split()))
sum_N = [0] * (N + 1)

for idx in range(1, N+1):
    sum_N[idx] = sum_N[idx - 1] + N_list[idx - 1]


for _ in range(M):
    left, right = list(map(int, input().split()))

    print(sum_N[right] - sum_N[left-1])