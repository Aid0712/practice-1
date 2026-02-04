# 1) range
for i in range(5):
    print(i)

# 2) Перебор списка
nums = [10, 20, 30]
for x in nums:
    print(x)

# 3) Перебор строки
for ch in "abc":
    print(ch)

# 4) Сумма элементов
nums = [1, 2, 3, 4]
total = 0
for x in nums:
    total += x
print("sum =", total)

# 5) Перечисление
names = ["A", "B", "C"]
for idx, name in enumerate(names):
    print(idx, name)
