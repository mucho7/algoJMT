def plz_die(power):
    if power == 1:
        return A % C

    else:
        tmp = plz_die(power // 2) % C

        if power % 2 == 0:
            return (tmp ** 2) % C
        else:
            return (((tmp ** 2) % C) * A) % C

        
A, B, C = (map(int, input().split()))

ans = plz_die(B)

print(ans)