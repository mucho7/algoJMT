from itertools import combinations


N, M = list(map(int, input().split()))
char_list = sorted(list(input().split()))
visited = [0 for _ in range(M)]

answer = combinations(char_list, N)
vowel = 'aeiou'

for ans in (answer):
    vo_cnt = 0
    not_vo = 0
    for char in ans:
        if char in vowel:
            vo_cnt += 1
        else:
            not_vo += 1
    if vo_cnt >= 1 and not_vo >= 2:
        for char in ans:
            print(char, end='')
        print()
