def check(x, y, op):
    if op == '<':
        if x > y:
            return False
    if op == '>':
        if x < y:
            return False
    return True


def go(index, num):
    if index == k + 1:
        ans_list.append(num)
        return

    for idx in range(10):
        if tmp_list[idx]:
            continue

        if index == 0 or check(num[index - 1], str(idx), sign_list[index - 1]):
            tmp_list[idx] = True
            go(index + 1, num + str(idx))
            tmp_list[idx] = False


k = int(input())

sign_list = list(input().split())

tmp_list = [0] * 10
ans_list = []

go(0, '')

ans_list = sorted(ans_list)

print(ans_list[-1])
print(ans_list[0])

