N = int(input())
statues = list(map(int, input().split()))

cnt_list = []
left = 0
right = 0
ans = 0

for idx in range(N):
    if statues[idx] == 1:
        left += 1
        right -= 1
    else:
        right += 1
        left -= 1
    
    if left > ans or right > ans:
        ans = max(left, right)

    if left < 0:
        left = 0
    
    if right < 0:
        right = 0

print(ans)