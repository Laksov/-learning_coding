#https://ulearn.me/course/python/O_chisle_e81cb7d6-ba5b-4af1-aa16-eb63ec5dac7c
n = int(input())
count = 0
sharing = False

while not sharing:
    if n % 9 == 0:
        sharing = True
        break
    n += 1
    count += 1

print(count)


