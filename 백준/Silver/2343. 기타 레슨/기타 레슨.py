import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lecture = list(map(int, input().split()))

vm = max(lecture)
start = vm
end = sum(lecture)

res = 10**9
while start <= end:
    mid = (start+end)//2
    cnt = 1
    tmp = 0
    for i in range(N):
        if tmp + lecture[i] <= mid:
            tmp += lecture[i]
        else:
            cnt += 1
            tmp = lecture[i]
        if cnt > M:
            break
    if cnt > M:
        start = mid+1
    else:
        end = mid-1
        if mid >= vm:
            res = min(res, mid)
print(res)