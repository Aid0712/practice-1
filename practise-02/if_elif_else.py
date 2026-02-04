# 1) Знак числа
x = 0
if x > 0:
    print("positive")
elif x == 0:
    print("zero")
else:
    print("negative")

# 2) Оценка по баллам
score = 73
if score >= 90:
    print("A")
elif score >= 75:
    print("B")
elif score >= 60:
    print("C")
else:
    print("D")

# 3) Время суток
hour = 21
if 6 <= hour < 12:
    print("morning")
elif 12 <= hour < 18:
    print("day")
else:
    print("evening")

# 4) Размер числа
n = 120
if n < 10:
    print("small")
elif n < 100:
    print("medium")
else:
    print("large")

# 5) Проверка символа
ch = "7"
if ch.isdigit():
    print("digit")
elif ch.isalpha():
    print("letter")
else:
    print("other")
