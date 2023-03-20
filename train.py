# https://ulearn.me/course/python/Posledovatel_nost__c4c08ac4-87a5-42f7-80d3-6cc131e69b41
count = 0
while count > -1:
    a = int(input())
    if a > 0:
        count = a + count
    else:
        break
print(count)
