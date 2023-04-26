"https://ulearn.me/course/python/Tribonachchi_7d25e08b-0b2c-4822-bcc0-feedd62838ff"


def treb(n):
    if n <= 1:
        return 1
    return treb(n - 1) + treb(n - 2) * 3


n = int(input())
ans = treb(n)
print(ans)

