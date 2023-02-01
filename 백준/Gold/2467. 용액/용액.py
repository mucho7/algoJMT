import sys
input = sys.stdin.readline

N  = int(input())
num_list = list(map(int, input().split()))

left = 0
right = N - 1

answerL = 0
answerR = N - 1
ans = abs(num_list[left]) + abs(num_list[right])

while left < right:
    temp_sum = num_list[left] + num_list[right]

    if abs(temp_sum) < ans:
        answerL = left
        answerR = right
        ans = abs(temp_sum)

    if temp_sum > 0:
        right -= 1
    elif temp_sum < 0:
        left += 1
    else:
        break

print(num_list[answerL], num_list[answerR])