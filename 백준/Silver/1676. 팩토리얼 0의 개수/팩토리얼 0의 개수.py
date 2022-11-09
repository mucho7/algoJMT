# from math import factorial

input_num = int(input())
cnt = 0
for num in range(1, input_num + 1):
    while num != 0:
        if num % 5 == 0:
            num = num // 5
            cnt += 1
        else:
            break


print(cnt)

# print(factorial(input_num))