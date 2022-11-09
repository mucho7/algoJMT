# 사고 싶은 카드의 갯수
N = int(input())


# idx + 1 = 팩에 들어 있는 카드갯수
# value = 팩의 가격

Pi = list(map(int, input().split()))

Pi.insert(0, 0)

shopping_list = [0 for _ in range(N+1)]

shopping_list[1] = Pi[1]
for idx in range(2, N+1):
    for cur in range(1, idx):
        shopping_list[idx] = max(shopping_list[idx], shopping_list[idx - cur] + Pi[cur], Pi[idx])

print(shopping_list[N])