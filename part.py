#https://ulearn.me/course/python/Partii_9cfa0ec4-3d94-4e09-aabd-226b88e233e3
n = int(input())
k = int(input())
a = int(input())
count = 0

while n < a:
    n = n + (n % k) + 1
    count += 1

print(count)
