from _collections import deque

T = int(input())

for _ in range(T):
    string = input()
    left = deque()
    right = deque()

    for char in string:
        if char.isalpha() or char.isnumeric():
            left.append(char)

        elif char == '<':
            if len(left):
                right.appendleft(left.pop())
        elif char == '>':
            if len(right):
                left.append(right.popleft())
        elif char == '-':
            if len(left):
                left.pop()

    for char in left:
        print(char, end='')
    for char in right:
        print(char, end='')
    print()
