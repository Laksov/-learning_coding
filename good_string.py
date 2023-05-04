# https://ulearn.me/course/python/Khoroshaya_stroka_0d33b814-6cb5-4bd5-bb80-9101b280a135

s = input()

if not ('A' in s):
    print('')
    exit(0)

k = 0

while s[k] != 'A':
    k += 1

print(s[k:])

