from collections import deque

T = int(input())

for _ in range(T):
    p = input()
    n = int(input())
    temp = input()
    deq = deque([])
    err_flag = False
    is_reverse = False

    if not temp == "[]":
        deq = deque(map(int, temp.strip("[, ]").split(",")))

    for char in p:
        if char == "R":
            is_reverse = not is_reverse
        elif char == "D":
            if n > 0:
                n -= 1
                if is_reverse:
                    deq.pop()
                else:
                    deq.popleft()
            else:
                err_flag = True
                break

    if err_flag:
        print("error")
    else:
        print("[", end="")
        if is_reverse:
            for num in range(n - 1, -1, -1):
                print(deq[num], end="")
                if not num == 0:
                    print(",", end="")
        else:
            for num in range(n):
                print(deq[num], end="")
                if not num == n - 1:
                    print(",", end="")
        print("]")