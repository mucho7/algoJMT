num = int(input())
input_list = [int(input()) for _ in range(num)]
stack_list = [0]
ans_list = []

stk_cursor = 0

for value in input_list:
    if value > stk_cursor:
        for num in range(stk_cursor + 1, value + 1):
            stk_cursor += 1
            ans_list.append('+')
            stack_list.append(num)
        ans_list.append('-')
        stack_list.pop(-1)
    elif value < stk_cursor:
        if value == stack_list.pop(-1):
            ans_list.append('-')
        else:
            print('NO')
            break
else:
    for ans in ans_list:
        print(ans)


