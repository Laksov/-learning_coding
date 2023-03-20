#https://ulearn.me/course/python/d5c95841-a2b1-4c5d-b54e-63d10e5a823f

k = int(input())
a = int(input())
count = 0
year = 1991

while k < a:
    if year % 2 == 0:
        k += 5
    else:
        k += k % 11
    count += 1
    year += 1

print(count)

