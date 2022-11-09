def dfs(start):
    if len(ans_list) == M:
        print(*ans_list)
        return
    remember_me = 0
    for i in range(start, len(nums)):
        if remember_me != nums[i]:
            ans_list.append(nums[i])
            remember_me = nums[i]
            dfs(i)
            ans_list.pop()


N, M = list(map(int, input().split()))

nums = sorted(list(set(map(int, input().split()))))

ans_list = []

dfs(0)