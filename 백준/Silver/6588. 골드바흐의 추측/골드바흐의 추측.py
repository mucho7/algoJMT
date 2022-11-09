def isPrime(num):
    if num==1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                return False
        return True


input_num = 3

while input_num != 0:
    input_num = int(input())
    for num in range(input_num-1, 0, -2):
        if isPrime(num):
            temp2 = input_num - num
            if isPrime(temp2):
                print(f'{input_num} = {temp2} + {num}')
                break