import heapq

T = int(input())

for _ in range(T):
    k = int(input())
    # 최소힙
    que_1 = []
    # 최대힙
    que_2 = []
    visited = [0 for _ in range(k)]

    for idx in range(k):
        command, num = input().split()
        num = int(num)

        if command == 'I':
            heapq.heappush(que_1, (num, idx))
            heapq.heappush(que_2, (-num, idx))
            visited[idx] = 1

        # 1이면 최대값, -1이면 최소값
        elif command == 'D':
            if num == -1:
                # 상대편 힙에서 삭제처리한 친구라면 우리도 삭제
                while que_1 and not visited[que_1[0][1]]:
                    heapq.heappop(que_1)
                # 지시된 동작
                if que_1:
                    visited[que_1[0][1]] = 0
                    heapq.heappop(que_1)

            elif num == 1:
                # 상대편 힙에서 삭제처리한 친구라면 우리도 삭제
                while que_2 and not visited[que_2[0][1]]:
                    heapq.heappop(que_2)
                # 지시된 동작
                if que_2:
                    visited[que_2[0][1]] = 0
                    heapq.heappop(que_2)

    # 마지막으로 한번 더 상대편 힙에서 삭제처리한 친구라면 우리도 삭제
    while que_1 and not visited[que_1[0][1]]:
        heapq.heappop(que_1)

    while que_2 and not visited[que_2[0][1]]:
        heapq.heappop(que_2)

    if que_1 and que_2:
        min_val = que_1[0][0]
        max_val = -(que_2[0][0])
        print(max_val, min_val)
    else:
        print('EMPTY')
