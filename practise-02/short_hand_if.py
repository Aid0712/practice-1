# 1) Найти большую
a, b = 5, 9
print(a if a > b else b)

# 2) Чётность/нечетность
n = 14
print("even" if n % 2 == 0 else "odd")

# 3) Пустая строка или нет
s = ""
print("not empty" if s else "empty")

# 4) Проверка возраста
age = 17
print("adult" if age >= 18 else "minor")

# 5) Вхождение подстроки
text = "hello world"
print("has world" if "world" in text else "no world")
