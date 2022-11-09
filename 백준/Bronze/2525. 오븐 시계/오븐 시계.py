time = list(map(int, input().split()))
minute = int(input())

time[1] = time[1] + minute

while time[1] >= 60:
    time[0] += 1
    time[1] -= 60

if time[0] >= 24:
    time[0] -= 24

print(f'{time[0]} {time[1]}')