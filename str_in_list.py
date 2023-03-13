#https://ulearn.me/course/python/21c37d82-4f23-44dd-b159-0f5f0bd70e21
def get_price(s):
    k = 0
    for el in s:
        if el == '#':
            k += 1000
        else:
            k += 100
    return k

n = int(input())
c = 0

for i in range(n):
    s = input()
    c += get_price(s)

print(c)