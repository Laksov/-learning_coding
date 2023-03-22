# https://acm.timus.ru/problem.aspx?space=1&num=1510

n = int(input())
d = dict()

for i in range(n):
    m = int(input())
    if m in d.keys():
        d[m] += 1
    else:
        d[m] = 1

m = -1
k = -1

for key, value in d.items():
    if value > m:
        m = value
        k = key

print(k)
