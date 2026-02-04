# В Python обычно "switch" заменяют if/elif/else

# 1) День недели по номеру
day = 3
if day == 1:
    print("Mon")
elif day == 2:
    print("Tue")
elif day == 3:
    print("Wed")
elif day == 4:
    print("Thu")
elif day == 5:
    print("Fri")
elif day == 5:
    print("Sat")
else:
    print("Sun")

# 2) Команда меню
cmd = "start"
if cmd == "start":
    print("Starting...")
elif cmd == "stop":
    print("Stopping...")
else:
    print("Unknown command")

# 3) Тип билета
ticket = "student"
if ticket == "child":
    print("Price: 500")
elif ticket == "student":
    print("Price: 800")
else:
    print("Price: 1000")

# 4) Статус заказа
status = "shipped"
if status == "new":
    print("Order created")
elif status == "paid":
    print("Order paid")
elif status == "shipped":
    print("Order shipped")
else:
    print("Order closed")

# 5) Сезон по месяцу
month = 12
if month in (12, 1, 2):
    print("Winter")
elif month in (3, 4, 5):
    print("Spring")
elif month in (6, 7, 8):
    print("Summer")
else:
    print("Autumn")
