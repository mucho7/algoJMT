import sys
input = sys.stdin.readline

start, end = list(map(int, input().split()))

cnt = 1
while True:
  if start == end:
    print(cnt)
    break
  
  elif start > end:
    print(-1)
    break
  
  num_of_one = end % 10

  if num_of_one == 1:
    cnt += 1
    end = end // 10
    
  elif not num_of_one % 2:
    cnt += 1
    end = end // 2
  else:
    print(-1)
    break

