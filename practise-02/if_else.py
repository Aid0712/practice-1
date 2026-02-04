# 1) Положительное/не положительное
x = -2
if x > 0:
    print("positive")
else:
    print("negative")

# 2) Пароль совпал или нет
password = "1234"
if password == "1234":
    print("access granted")
else:
    print("access denied")

# 3) Чётное/нечётное
n = 11
if n % 2 == 0:
    print("even")
else:
    print("odd")

# 4) Есть ли слово
word = "cat"
sentence = "I have a dog"
if word in sentence:
    print("found")
else:
    print("not found")

# 5) Больше/меньше
a, b = 10, 20
if a > b:
    print("a > b")
else:
    print("a < b")
