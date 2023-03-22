# https://ulearn.me/course/python/Dialogovaya_sistema_f18cde75-bca4-4c5b-b734-46eb00b5a8de

a = 0
k = list(map(int, input().split()))
count = 0

for i in range(len(k)):
    while a < 32 or k[i] != 0:
        a = a + k[i]
        count += 1

print(count)
