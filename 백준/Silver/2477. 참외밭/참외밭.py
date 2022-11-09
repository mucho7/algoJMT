melon = int(input())
square_list = []
for _ in range(6):
    square_list.append(list(map(int, (input().split()))))

square_width = 0
square_height = 0

for idx in range(6):
    if square_list[idx][0] == 1:
        square_width += square_list[idx][1]
    elif square_list[idx][0] == 3:
        square_height += square_list[idx][1]

small_height = small_width = 0
# 작은 사각형의 정보 찾기
for idx in range(6):
    if square_list[idx][0] == 1 or square_list[idx][0] == 2:
        if square_list[idx][1] == square_width:
            if idx == 0:
                small_height = abs(square_list[5][1] - square_list[idx+1][1])
            elif idx == 5:
                small_height = abs(square_list[idx-1][1] - square_list[0][1])
            else:
                small_height = abs(square_list[idx-1][1] - square_list[idx+1][1])
    elif square_list[idx][0] == 3 or square_list[idx][0] == 4:
        if square_list[idx][1] == square_height:
            if idx == 0:
                small_width = abs(square_list[5][1] - square_list[idx+1][1])
            elif idx == 5:
                small_width = abs(square_list[idx-1][1] - square_list[0][1])
            else:
                small_width = abs(square_list[idx-1][1] - square_list[idx+1][1])



square = square_height * square_width
small_square = small_height * small_width
ans = (square - small_square) * melon

print(ans)