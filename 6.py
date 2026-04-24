N = int(input())
b = 0
a = ""
while b <= N:
    a += str(b)
    a += ","
    b += 2
a = a[:-1]
print(a)