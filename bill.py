# https://ulearn.me/course/python/Vasya_i_schet_d46c19e1-03c8-4adb-b241-ce6bd023df6d
k = int(input())
a = int(input())
count = 0

while a > k:
    if k < 1000:
        k += 2
    else:
        k += k // 500
    count += 1

print(count)
