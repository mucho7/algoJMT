import sys
input = sys.stdin.readline

word = list(input().strip())
word_stack = []
tc_num = int(input())
cursor = len(word)

for tc in range(tc_num):
    order = input().split()

    if order[0] == 'L' and word:
        word_stack.append((word.pop()))

    elif order[0] == 'D' and word_stack:
        word.append(word_stack.pop())

    elif order[0] == 'B' and word:
        word.pop()

    elif order[0] == 'P':
        word.append(order[1])


word.extend(reversed(word_stack))

for char in word:
    print(char, end='')
