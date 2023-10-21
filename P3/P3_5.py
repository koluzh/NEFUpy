def is_palindrome(x: int):
    s = str(x)
    for i in range(len(s)//2):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True


res = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        if is_palindrome(j * i) and res < i * j:
            res = i * j

print(res)
