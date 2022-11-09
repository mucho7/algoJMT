import sys
import heapq

input = sys.stdin.readline

N = int(input())

min_heap = []
length = 0

for _ in range(N):
    x = -int(input())

    if x != 0:
        heapq.heappush(min_heap, x)
        length += 1
    else:
        if length != 0:
            print(-heapq.heappop(min_heap))
            length -= 1
        else:
            print(0)

