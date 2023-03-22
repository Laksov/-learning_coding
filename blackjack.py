# https://ulearn.me/course/python/Blekdzhek_a5f1a71f-68a1-4fa8-a9a0-a4355fb309c2

count = 0

cards = 0

while count <= 21:
    s = input()
    if s == 'J' or s == 'Q' or s == 'K':
        count += 10
    elif s == 'A':
        count += 11
    else:
        count += int(s)
    cards += 1

print(cards - 1)
