time, drink = list(map(int, input().split()))

if drink:
    print(280)
else:
    if 12 <= time <= 16:
        print(320)
    else:
        print(280)