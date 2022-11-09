# N 도감의 길이
# M 문제의 갯수
N, M = map(int, input().split())

pocketmon_dict = dict()
dogam_dict = dict()

for idx in range(1, N+1):
    pocketmon = input()
    pocketmon_dict[idx] = pocketmon
    dogam_dict[pocketmon] = idx

for _ in range(M):
    question = input()

    try:
        print(pocketmon_dict.get(int(question)))

    except ValueError:
        print(dogam_dict.get(question))