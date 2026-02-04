# 1) Остановиться на 3
for i in range(10):
    if i == 3:
        break
    print(i)

# 2) Найти первое чётное
nums = [1, 7, 9, 4, 10]
for x in nums:
    if x % 2 == 0:
        print("first even =", x)
        break

# 3) Поиск символа
text = "hello"
for ch in text:
    if ch == "l":
        print("found l")
        break

# 4) Прервать при слове stop
words = ["go", "go", "stop", "go"]
for w in words:
    if w == "stop":
        break
    print(w)

# 5) Прервать при сумме > 10
nums = [2, 4, 7, 1]
total = 0
for x in nums:
    total += x
    if total > 10:
        print("stopped at total =", total)
        break
