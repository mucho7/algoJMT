N, M = map(int, input().split())

site_dict = dict()
for _ in range(N):
    site, password = input().split()
    site_dict[site] = password

for _ in range(M):
    finding_site = input()
    print(site_dict.get(finding_site))