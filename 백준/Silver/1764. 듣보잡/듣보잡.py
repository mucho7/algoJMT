N, M = map(int, input().split())

no_listen = dict()
no_hear = dict()

for idx in range(N):
    somebody = input()
    no_listen[somebody] = idx

for idx in range(M):
    somebody = input()
    no_hear[somebody] = idx

ans_list = []
for nono in no_listen.keys():
    if no_hear.get(nono) != None:
        ans_list.append(nono)

print(len(ans_list))
for who in sorted(ans_list):
    print(who)