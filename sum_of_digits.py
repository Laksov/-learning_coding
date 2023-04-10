'https://ulearn.me/course/python/Summa_tsifr_96ef6f87-25ca-4ac0-8acc-77b81c7f789a?autoplay=true'


def digits_sum(li):
    count = 0
    for el in li:
        for ch in str(el):
            count += int(ch)
    return count


li = [int(x) for x in input().split() if int(x) % 2 != 0]
print(digits_sum(li))
