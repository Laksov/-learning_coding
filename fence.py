#https://ulearn.me/course/python/Zaborchik_d86889d8-14f4-47c6-b707-331e5f8c3934
def get_max_neighbor(l, r, fence):
    count = 0
    if r - l <= 1:
        return count
    for i in range(l, r-1):
        cur = fence[i]
        if (fence[i - 1] < cur) and (fence[i + 1] < cur):
            count += 1

    return count


# считываем входные данные
n = int(input())
fence = [int(el) for el in input().split()]

q = int(input())
for i in range(q):
    l, r = map(int, input().split())
    print(get_max_neighbor(l, r, fence))

