T = int(input())

for _ in range(T):
    word = input()

    front_palindrome = 0
    back_palindrome = 0
    front = 0
    back = len(word) - 1

    for _ in range(len(word)//2):
        if word[front] != word[back]:
            if front_palindrome:
                front_palindrome = 2
                break
            front_palindrome = 1
            if word[front + 1] == word[back]:
                front += 1
            else:
                front_palindrome = 2
                break
        front += 1
        back -= 1

    front = 0
    back = len(word) - 1
    for _ in range(len(word) // 2):
        if word[front] != word[back]:
            if back_palindrome:
                back_palindrome = 2
                break
            back_palindrome = 1
            if word[front] == word[back - 1]:
                back -= 1
            else:
                back_palindrome = 2
                break
        front += 1
        back -= 1

    print(min(back_palindrome, front_palindrome))