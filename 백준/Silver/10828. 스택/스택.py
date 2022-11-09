import sys
input = sys.stdin.readline
stacked_list = []
num = int(input())

for _ in range(num):
    txt = input().split()
    if txt[0] == 'pop':
        if len(stacked_list) == 0:
            print(-1)
        else:
            print(stacked_list.pop(-1))

    elif txt[0] == 'size':
        print(len(stacked_list))

    elif txt[0] == 'empty':
        if len(stacked_list) == 0:
            print(1)
        else:
            print(0)

    elif txt[0] == 'top':
        if len(stacked_list) == 0:
            print(-1)
        else:
            print(stacked_list[-1])

    else:
        stacked_list.append(txt[1])