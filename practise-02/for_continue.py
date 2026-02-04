# 1) Пропустить 2
for i in range(5):
    if i == 2:
        continue
    print(i)

# 2) Печатать только чётные
for i in range(10):
    if i % 2 != 0:
        continue
    print(i)

# 3) Пропустить пустые
items = ["a", "", "b", "", "c"]
for s in items:
    if s == "":
        continue
    print(s)

# 4) Пропустить отрицательные
nums = [3, -1, 5, -2, 8]
for x in nums:
    if x < 0:
        continue
    print(x)

# 5) Пропустить слова короче 3
words = ["hi", "python", "ok", "code"]
for w in words:
    if len(w) < 3:
        continue
    print(w)
