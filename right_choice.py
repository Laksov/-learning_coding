# https://ulearn.me/course/python/Pravil_nyy_vybor_7739d6fa-0b87-4044-8d65-12c20564a950
a = int(input())
b = int(input())
k = 0
while a >= b:
    a *= 2
    b *= 3
    k += 1
print(k)
