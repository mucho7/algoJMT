while True:
    a, b, c = list(map(int, input().split()))

    if a == 0 and b == 0 and c == 0:
        break
        
    long = max(a, b, c)
    
    result = a ** 2 + b ** 2 + c ** 2 - long ** 2

    if result == long ** 2:
        print('right')
    else:
        print('wrong')