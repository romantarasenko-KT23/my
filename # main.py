# main.py
# ===== Завдання 1: Калькулятор =====

def add(a, b):
    """Повертає суму двох чисел"""
    return a + b

def subtract(a, b):
    """Повертає різницю двох чисел"""
    return a - b

def multiply(a, b):
    """Повертає добуток двох чисел"""
    return a * b

def divide(a, b):
    """Повертає результат ділення, з перевіркою на ділення на нуль"""
    if b == 0:
        return "Помилка: ділення на нуль неможливе!"
    return a / b


# ===== Завдання 2: Функції для роботи зі списками =====

def calculate_average(numbers):
    """Повертає середнє арифметичне чисел у списку"""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def find_max(numbers):
    """Повертає найбільше число у списку"""
    if not numbers:
        return None
    return max(numbers)


# ===== Основна програма =====

def main():
    print("=== Частина 1: Калькулятор ===")
    a = float(input("Введіть перше число: "))
    b = float(input("Введіть друге число: "))
    operation = input("Введіть операцію (+, -, *, /): ")

    if operation == "+":
        result = add(a, b)
    elif operation == "-":
        result = subtract(a, b)
    elif operation == "*":
        result = multiply(a, b)
    elif operation == "/":
        result = divide(a, b)
    else:
        result = "Невідома операція!"

    print("Результат:", result)

    print("\n=== Частина 2: Робота зі списками ===")
    numbers = [12, 45, 67, 23, 89, 34, 56]
    average = calculate_average(numbers)
    maximum = find_max(numbers)

    print("Список чисел:", numbers)
    print("Середнє арифметичне:", average)
    print("Найбільше число:", maximum)


# Запуск програми
if __name__ == "__main__":
    main()
