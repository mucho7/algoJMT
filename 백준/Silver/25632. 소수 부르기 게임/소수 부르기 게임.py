def prime(start: int, end: int):
    result = 0

    for num in range(start, end + 1):
        if num == 1:
            continue
        else:
            for i in range(2, int(num**0.5)+1):
                if num % i == 0:
                    break
            else:
                result += 1

    return result


yt_start, yt_end = map(int, input().split())
yj_start, yj_end = map(int, input().split())

yt = prime(yt_start, yt_end)
yj = prime(yj_start, yj_end)

same = 0

if yt_end >= yj_start:
    same = prime(yj_start, yt_end)
elif yj_end >= yt_start:
    same = prime(yt_start, yj_end)

if same % 2 == 1:
    yt += 1

if yt > yj:
    print('yt')
else:
    print('yj')