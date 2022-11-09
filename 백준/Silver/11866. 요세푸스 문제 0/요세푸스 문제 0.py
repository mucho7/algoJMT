num, jump_num = map(int, input().split())
josua_list = [x for x in range(1, num + 1)]
dem_cursor = 0
dem_list = []

for _ in range(num):
    dem_cursor += jump_num - 1
    if dem_cursor >= len(josua_list):
            dem_cursor = dem_cursor % len(josua_list)
    dem_list.append(josua_list.pop(dem_cursor))
    

print('<', end='')
for dem in dem_list:
    if dem == dem_list[-1]:
        print(dem, end='')
    else:    
        print(dem, end=', ')
print('>', end='')
