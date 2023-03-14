# https://ulearn.me/course/python/Slova_8678e7b3-9622-4fd9-b389-b7d7c0aff79f
def has_leter(s):
    for i in range(len(s)):
        num = ord(s[i])
        if not (65 <= num <= 90 or 97 <= num <= 122):
            return False

    return True


n = 0
is_end = True
while is_end:
    n += 1
    s = input()
    is_end = has_leter(s)
print(n)
