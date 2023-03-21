# https://ulearn.me/course/python/Khoroshaya_stroka_0d33b814-6cb5-4bd5-bb80-9101b280a135

n = list(map(int, input().split()))

for i in range(len(n)):
    while n[i] != 'A':
        if n[i] != 'A':
            n = n[1:]

print(n)
