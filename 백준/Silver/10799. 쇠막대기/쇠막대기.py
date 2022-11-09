lazor = input()

ans = 0
lazor_stack = []
for idx in range(len(lazor)):
    if lazor[idx] == '(':
        lazor_stack.append(lazor[idx])
    elif lazor[idx] == ')':
        if lazor[idx - 1] == '(':
            lazor_stack.pop()
            ans += len(lazor_stack)
        else:
            lazor_stack.pop()
            ans += 1
print(ans)