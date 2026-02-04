# 1) 0 1 2 3 4
i = 0
while i < 5:
    print(i)
    i += 1

# 2) Сумма 1 2 3 4 5
i = 1
total = 0
while i <= 5:
    total += i
    i += 1
print("sum =", total)

# 3) Обратный отсчёт
n = 3
while n > 0:
    print(n)
    n -= 1
print("go!")

# 4) Пока строка не станет длинной
s = ""
while len(s) < 3:
    s += "a"
print(s)

# 5) делим на 2 пока число не станет 1 
x = 20
while x > 1:
    x //= 2
    print(x)
