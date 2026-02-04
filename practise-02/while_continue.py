# 1) Пропустить 3
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

# 2) Печатать только нечётные
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)

# 3) Пропуск отрицательных
nums = [2, -1, 5, -3, 7]
i = 0
while i < len(nums):
    if nums[i] < 0:
        i += 1
        continue
    print(nums[i])
    i += 1

# 4) Пропустить пустые строки
items = ["hi", "", "python", "", "ok"]
i = 0
while i < len(items):
    if items[i] == "":
        i += 1
        continue
    print(items[i])
    i += 1

# 5) Пропуск числа 0
arr = [1, 0, 2, 0, 3]
i = 0
while i < len(arr):
    if arr[i] == 0:
        i += 1
        continue
    print("value:", arr[i])
    i += 1
