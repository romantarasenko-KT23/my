# -------------------------------
# УМОВНІ КОНСТРУКЦІЇ
# -------------------------------

print("=== УМОВНІ КОНСТРУКЦІЇ ===")

# 1. Перевірка паролю
password = "password123"
user_password = "password123"  # задане значення
if user_password == password:
    print("Ви увійшли в систему")
else:
    print("Неправильний пароль")

# 2. Визначення днів тижня
day_number = 4
if day_number == 1:
    print("Понеділок")
elif day_number == 2:
    print("Вівторок")
elif day_number == 3:
    print("Середа")
elif day_number == 4:
    print("Четвер")
elif day_number == 5:
    print("П’ятниця")
elif day_number == 6:
    print("Субота")
elif day_number == 7:
    print("Неділя")
else:
    print("Помилка: номер дня має бути від 1 до 7")

print()

# -------------------------------
# ЦИКЛИ
# -------------------------------

print("=== ЦИКЛИ ===")

# 1. Таблиця множення
number = 5
print(f"Таблиця множення для {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# 2. Сума чисел
numbers = [3, 5, 7, 9, 11]
total_sum = sum(numbers)
print("Сума чисел:", total_sum)

# 3. Факторіал числа
n = 5
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"Факторіал {n} =", factorial)

# 4. Парні числа від 1 до 50
print("Парні числа від 1 до 50:")
for i in range(1, 51):
    if i % 2 == 0:
        print(i, end=" ")
print("\n")

# 5. Пошук простих чисел
print("Прості числа від 1 до 50:")
for num in range(2, 51):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
print("\n")

# -------------------------------
# СПИСКИ
# -------------------------------

print("=== СПИСКИ ===")

# 1. Робота із списками
numbers_list = [1, 2, 3, 4, 5]
numbers_list.append(10)
numbers_list.append(20)
numbers_list.remove(10)
print("Оновлений список:", numbers_list)

# 2. Знаходження суми
list_sum = [5, 10, 15, 20]
print("Сума елементів:", sum(list_sum))

# 3. Подвійні значення
original = [2, 4, 6, 8]
doubled = [x * 2 for x in original]
print("Подвоєні значення:", doubled)
print()

# -------------------------------
# КОРТЕЖІ
# -------------------------------

print("=== КОРТЕЖІ ===")

# 1. Робота із кортежами
fruits = ("яблуко", "банан", "апельсин")
print("Елементи кортежу:")
for fruit in fruits:
    print(fruit)

# 2. Об'єднання кортежів
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2
print("Об'єднаний кортеж:", combined_tuple)
print()

# -------------------------------
# СЛОВНИКИ
# -------------------------------

print("=== СЛОВНИКИ ===")

# 1. Робота із словниками
athlete = {
    "ім'я": "Майкл Джордан",
    "вік": 60,
    "спорт": "баскетбол",
    "команда": "Chicago Bulls"
}
print("Інформація про спортсмена:")
for key, value in athlete.items():
    print(f"{key}: {value}")

# 2. Оновлення словника
books = {
    "1984": 1949,
    "Гаррі Поттер": 1997
}
books["Майстер і Маргарита"] = 1967
print("Оновлений словник книг:", books)

# 3. Пошук значення
countries = {
    "Україна": "Київ",
    "Польща": "Варшава",
    "Франція": "Париж",
    "Італія": "Рим"
}
country = "Польща"
if country in countries:
    print(f"Столиця країни {country} — {countries[country]}")
else:
    print("Такої країни немає у словнику.")
