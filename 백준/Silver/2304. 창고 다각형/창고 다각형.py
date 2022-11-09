N = int(input())

box_dict = dict()

for _ in range(N):
    K, V = list(map(int, input().split()))
    box_dict[K] = V

max_warehouse = max(box_dict.keys())

max_box = 0
max_idx = -1
result_list = []
# 좌측 탐색
for idx in range(max_warehouse + 1):
    if box_dict.get(idx) is not None and max_box <= box_dict.get(idx):
        max_box = box_dict.get(idx)
        max_idx = idx
        result_list.append(idx)

# 우측 탐색
right_max = 0
right_idx = max_warehouse
while right_idx != max_idx:
    if box_dict.get(right_idx) is not None and right_max < box_dict.get(right_idx):
        right_max = box_dict.get(right_idx)
        result_list.append(right_idx)
    right_idx -= 1

result_list = sorted(result_list)

ans = max_box
for idx in range(len(result_list)):
    if result_list[idx] < max_idx:
        ans += (result_list[idx + 1] - result_list[idx]) * box_dict.get(result_list[idx])
    elif result_list[idx] > max_idx:
        ans += (result_list[idx] - result_list[idx - 1]) * box_dict.get(result_list[idx])

print(ans)