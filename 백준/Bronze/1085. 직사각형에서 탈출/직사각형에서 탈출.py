x, y, w, h = list(map(int, input().split()))

x_diff = 0
y_diff = 0

if x > w - x:
    x_diff = w - x
else:
    x_diff = x
    
if y > h -y:
    y_diff = h - y
else:
    y_diff = y
    
if x_diff > y_diff:
    print(y_diff)
else:
    print(x_diff)