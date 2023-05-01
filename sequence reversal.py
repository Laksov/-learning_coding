'https://ulearn.me/course/python/Razvorot_posledovatel_nosti_9ee9b14d-d649-433e-a27a-11d548b008a1'


def rec_reverse():
    n = int(input())

    if n == -1:
        return
    rec_reverse()
    print(n)


rec_reverse()
