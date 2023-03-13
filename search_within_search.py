#https://ulearn.me/course/python/Poisk_vnutri_poiska_7baffd31-fe05-43ce-993b-739f163083fc
def is_more(s):

    vowels = 0
    uppers = 0

    for el in s:
        if el.lower() in 'aeiuyo':
            vowels += 1
        if not el.islower():
            uppers += 1

    return uppers > vowels


k = 0

for word in input().split():
    if is_more(word):
        k += 1

print(k)





