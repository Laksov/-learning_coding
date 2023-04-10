def swap(a, b):
    print("local var")
    print(f"a = {a}, b = {b}")
    a, b = b, a
    print(f"a = {a}, b = {b}")
    return [a, b]


a = int(input())
b = int(input())

a, b = swap(a, b)
print("global")
print(f"a = {a}, b = {b}")
li1 = [1, 2, 3, 4, 5, 6]
lli2 = [1, 2, 3]
swap(li1, lli2)
print("global")