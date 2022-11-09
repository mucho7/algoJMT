T = int(input())

plusplus = [1] * 11
plusplus[1] = 1
plusplus[2] = 2
plusplus[3] = 4

for idx in range(11):
    if idx < 4:
        pass
    else:
        plusplus[idx] = 2 * plusplus[idx-1] - plusplus[idx - 4]

for _ in range(T):
    n = int(input())

    print(plusplus[n])