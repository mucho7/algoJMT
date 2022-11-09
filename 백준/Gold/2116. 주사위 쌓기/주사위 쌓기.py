def whats_on_top(side_idx):
    if side_idx == 0:
        return 5
    elif side_idx == 1:
        return 3
    elif side_idx == 2:
        return 4
    elif side_idx == 3:
        return 1
    elif side_idx == 4:
        return 2
    elif side_idx == 5:
        return 0


def best_side(bottom_idx, dice_idx):
    tmp_dice_list = dice_list[dice_idx].copy()
    tmp_top = whats_on_top(bottom_idx)
    if tmp_top > bottom_idx:
        tmp_dice_list.pop(tmp_top)
        tmp_dice_list.pop(bottom_idx)
    else:
        tmp_dice_list.pop(bottom_idx)
        tmp_dice_list.pop(tmp_top)
    return max(tmp_dice_list)


N = int(input())

dice_list = [list(map(int, input().split())) for _ in range(N)]

ans = 0

for first_top_idx in range(6):

    cnt = 1
    tmp_ans = 0

    top = dice_list[0][first_top_idx]
    tmp_ans += best_side(first_top_idx, 0)

    while cnt != N:

        for idx in range(6):

            if dice_list[cnt][idx] == top:
                bottom = idx
                top = dice_list[cnt][whats_on_top(bottom)]
                break

        tmp_ans += best_side(bottom, cnt)
        cnt += 1

    ans = max(ans, tmp_ans)

print(ans)
