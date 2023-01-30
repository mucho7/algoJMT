# A65 a97

word = input()

for char in word:
    if 65<= ord(char) <= 90:
        print(chr(ord(char) + 32), end='')
    else:
        print(chr(ord(char) - 32), end='')