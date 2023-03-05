#https://ulearn.me/course/python/Dinamicheskiy_maksimum_e1e9545e-d0d3-42d5-b486-07c1937522d8
el = 0
maxx = -1
while el != -1:
    el = int(input())
    if el > maxx:
        maxx = el
    if el != -1:
        print(maxx)

