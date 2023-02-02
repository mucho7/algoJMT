import sys
input = sys.stdin.readline

N, S = list(map(int, input().split()))
nums = list(map(int, input().split())) + [0]

temp_sum = nums[0]
ans = N + 1
outer_cursor = 0
inner_cursor = 0


while outer_cursor < N and outer_cursor >= inner_cursor:
    if temp_sum < S:
        outer_cursor +=  1
        temp_sum += nums[outer_cursor]

    else:
        ans = min(ans, outer_cursor - inner_cursor + 1)
        temp_sum -= nums[inner_cursor]
        inner_cursor += 1


if ans == N + 1:
    print(0)
else:
    print(ans)