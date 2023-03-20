# https://ulearn.me/course/python/Zaryadka_59cd2153-8d62-45de-9d09-6be4e71dc0c5
n = int(input())
l = list(map(int, input().split()))
for i in range(n - 1):
    k = 0
    el = l[n-1]
    for j in range(i + 1, n):
        if l[j] >= l[i]:
            el = l[j]
            break
        k += 1
    if l[i] <= el:
        k += 1
    print(k)
print(0)
