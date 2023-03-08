# https://ulearn.me/course/python/Schetchik_39dc9600-caa1-410b-a51d-b6099d3e8049
l, r = map(int, input().split())
n = int(input())
# ai = [int(el) for el in input().split()]
d = dict()
for i in range(l, r + 1):
    d[i] = 0
for el in input().split():
    num = int(el)
    if num <= r and num >= l:
        if num in d.keys():
            d[num] += 1
for i in range(l, r + 1):
    print(f"{i}: {d[i]}")
