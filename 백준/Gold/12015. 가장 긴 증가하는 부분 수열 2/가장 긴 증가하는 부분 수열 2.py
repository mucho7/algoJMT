import sys
input = sys.stdin.readline


def find(target):
    low, high = 1, len(stack) - 1
    while low < high:
        middle = (low+high) // 2
        if stack[middle] < target:
            low = middle + 1
        elif stack[middle] > target:
            high = middle
        else:
            low = high = middle
    return high

N = int(input())
A_list = list(map(int, input().split()))
stack = [0]

for num in A_list:
    if stack[-1] < num:
        stack.append(num)
    else:
        stack[find(num)] = num

print(len(stack) - 1)