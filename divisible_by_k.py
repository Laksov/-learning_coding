# https://ulearn.me/course/python/Delitsya_na_k__8702bb2e-c40d-444e-9e8a-f8da98be91f6
# работает за квадрат
# k = int(input())
# n = int(input())
# l = list(map(int, input().split()))
# for i in range(n):
#     count = 0
#     for j in range(0,i + 1):
#         if l[j] % k == 0:
#             count += 1
#     print(count)
# работает за линию
k = int(input())
n = int(input())
count = 0
for el in input().split():
    num = int(el)
    if num % k == 0:
        count += 1
    print(count)
