num = int(input())
for _ in range(num):
    txt = input()
    left_cnt = 0
    right_cnt = 0
    for idx in range(len(txt)):
        if txt[idx] == '(':
            right_cnt += 1
        else:
            left_cnt += 1
        if right_cnt - left_cnt == -1:
            break

    if right_cnt == left_cnt:
        print('YES')
    else:
        print('NO')