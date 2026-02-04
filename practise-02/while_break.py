# 1) break сразу
while True:
    print("once")
    break

# 2) Остановиться на 5
i = 0
while i < 10:
    if i == 5:
        break
    print(i)
    i += 1

# 3) Поиск элемента
nums = [3, 7, 2, 9, 5]
i = 0
while i < len(nums):
    if nums[i] == 9:
        print("found 9 at", i)
        break
    i += 1

# 4) Остановиться при делимости на 7
n = 1
while True:
    if n % 7 == 0:
        print("first multiple of 7 =", n)
        break
    n += 1

# 5) Остановиться, когда сумма превысит 20
i = 1
total = 0
while True:
    total += i
    if total > 20:
        print("total =", total)
        break
    i += 1
