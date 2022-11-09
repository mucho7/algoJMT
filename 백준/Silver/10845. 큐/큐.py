import sys
input = sys.stdin.readline
que_list = []
num = int(input())

for _ in range(num):
    txt = input().split()
    if txt[0] == 'pop':
        if len(que_list) == 0:
            print(-1)
        else:
            print(que_list.pop(0))

    elif txt[0] == 'push':
        que_list.append(txt[1])

    elif txt[0] == 'size':
        print(len(que_list))

    elif txt[0] == 'empty':
        if len(que_list) == 0:
            print(1)
        else:
            print(0)

    elif txt[0] == 'front':
        if len(que_list) == 0:
            print(-1)
        else:
            print(que_list[0])

    elif txt[0] == 'back':
        if len(que_list) == 0:
            print(-1)
        else:
            print(que_list[-1])

    else:
        que_list.append(txt[1])