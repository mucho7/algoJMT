def han(num):
    ans = 0
    for ham in range(1,num+1):
        if len(str(ham)) < 3:
            ans += 1
        elif len(str(ham)) == 4:
            pass
        else:
            list_ham = list(str(ham))
            if (int(list_ham[0])-int(list_ham[1])) == (int(list_ham[1])-int(list_ham[2])):
                ans += 1
    print(ans)

num = int(input())
han(num)