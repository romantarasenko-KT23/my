# main.py
# ============================================================
# ✅ Завдання 1: Принцип єдиного обов'язку (SRP)
# ============================================================

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class UserService:
    """Клас відповідає лише за керування користувачами."""
    def create_user(self, name, email):
        user = User(name, email)
        print(f"Користувач створений: {user.name} ({user.email})")
        return user

    def update_user(self, user, new_name=None, new_email=None):
        if new_name:
            user.name = new_name
        if new_email:
            user.email = new_email
        print(f"Користувача оновлено: {user.name} ({user.email})")

    def delete_user(self, user):
        print(f"Користувача видалено: {user.name} ({user.email})")
        del user


# --- Приклад використання ---
print("=== SRP ===")
service = UserService()
u = service.create_user("Олександр", "alex@example.com")
service.update_user(u, new_name="Олександр Іваненко")
service.delete_user(u)


# ============================================================
# ✅ Завдання 2: Принцип відкритості/закритості (OCP)
# ============================================================
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class AreaCalculator:
    """Новий клас, який не змінює існуючі фігури"""
    @staticmethod
    def calculate(shape: Shape):
        return shape.area()


print("\n=== OCP ===")
circle = Circle(5)
rect = Rectangle(4, 6)
print(f"Площа кола: {AreaCalculator.calculate(circle):.2f}")
print(f"Площа прямокутника: {AreaCalculator.calculate(rect):.2f}")


# ============================================================
# ✅ Завдання 3: Принцип підстановки Лісков (LSP)
# ============================================================

class Figure(ABC):
    @abstractmethod
    def get_area(self):
        pass


class Square(Figure):
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side * self.side


class CircleLSP(Figure):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2


def print_area(figure: Figure):
    """Ця функція працює з будь-якою фігурою — підкласи повністю замінні"""
    print(f"Площа: {figure.get_area():.2f}")


print("\n=== LSP ===")
print_area(Square(4))
print_area(CircleLSP(3))


# ============================================================
# ✅ Завдання 4: Принцип розділення інтерфейсу (ISP)
# ============================================================

# ❌ Неправильний варіант — великий інтерфейс з усіма методами
# ✅ Правильний — кожен клас реалізує лише потрібний функціонал

class Printable(ABC):
    @abstractmethod
    def print_doc(self, document):
        pass


class Scannable(ABC):
    @abstractmethod
    def scan_doc(self, document):
        pass


class Copyable(ABC):
    @abstractmethod
    def copy_doc(self, document):
        pass


class Printer(Printable):
    def print_doc(self, document):
        print(f"Друкую документ: {document}")


class Scanner(Scannable):
    def scan_doc(self, document):
        print(f"Сканую документ: {document}")


class Copier(Printable, Scannable, Copyable):
    """Мультифункціональний пристрій"""
    def print_doc(self, document):
        print(f"Друкую: {document}")

    def scan_doc(self, document):
        print(f"Сканую: {document}")

    def copy_doc(self, document):
        print(f"Копіюю: {document}")


print("\n=== ISP ===")
printer = Printer()
scanner = Scanner()
copier = Copier()

printer.print_doc("Звіт.pdf")
scanner.scan_doc("Фото.jpg")
copier.copy_doc("Документ.docx")


# ============================================================
# ✅ Завдання 5: Принцип інверсії залежностей (DIP)
# ============================================================

class NotificationService(ABC):
    @abstractmethod
    def send(self, message):
        pass


class EmailNotification(NotificationService):
    def send(self, message):
        print(f"Надіслано email: {message}")


class SMSNotification(NotificationService):
    def send(self, message):
        print(f"Надіслано SMS: {message}")


class UserManager:
    """Клас залежить від абстракції, а не конкретної реалізації"""
    def __init__(self, notifier: NotificationService):
        self.notifier = notifier

    def register_user(self, name):
        print(f"Користувач {name} зареєстрований.")
        self.notifier.send(f"Вітаємо, {name}! Реєстрація успішна.")


print("\n=== DIP ===")
email_notifier = EmailNotification()
sms_notifier = SMSNotification()

manager1 = UserManager(email_notifier)
manager1.register_user("Ірина")

manager2 = UserManager(sms_notifier)
manager2.register_user("Андрій")
