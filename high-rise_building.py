# https://ulearn.me/course/python/Mnogoetazhka_9ddd9d0b-7e8a-4028-bbcc-57e0869619f5
n, m = map(int, input().split())

count = 0
for i in range(n):
    s = input()
    for j in range(1, m):
        if s[j - 1] == s[j] and s[j] == '1':
            count += 1
            break

print(count)
