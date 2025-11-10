# main.py
# ================================================
# ✅ Завдання 1: Створення класу і об'єктів
# ================================================

class Animal:
    def __init__(self, name, species, age):
        """Конструктор класу Animal"""
        self.name = name
        self.species = species
        self.age = age

    def make_sound(self):
        """Виводить звук тварини"""
        print(f"{self.name} ({self.species}) видає звук: *звук тварини*")


# Створюємо два об'єкти класу Animal
animal1 = Animal("Бобік", "Собака", 3)
animal2 = Animal("Мурка", "Кішка", 2)

# Викликаємо методи make_sound()
animal1.make_sound()
animal2.make_sound()


# ================================================
# ✅ Завдання 2: Робота з об'єктами
# ================================================

class Rectangle:
    def __init__(self, width, height):
        """Конструктор класу Rectangle"""
        self.width = width
        self.height = height

    def calculate_area(self):
        """Обчислює площу прямокутника"""
        return self.width * self.height


# Створюємо два об'єкти класу Rectangle
rect1 = Rectangle(5, 10)
rect2 = Rectangle(8, 3)

# Виводимо площу прямокутників
print(f"\nПлоща першого прямокутника: {rect1.calculate_area()}")
print(f"Площа другого прямокутника: {rect2.calculate_area()}")


# ================================================
# ✅ Завдання 3: Наслідування
# ================================================

class Vehicle:
    def __init__(self, make, model, year):
        """Базовий клас Транспортний засіб"""
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        """Виводить базову інформацію"""
        print(f"Це {self.make} {self.model} {self.year} року виробництва.")


# Підклас: Автомобіль
class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type

    def start_engine(self):
        print(f"{self.make} {self.model} — двигун запущено ({self.fuel_type}).")

    def display_info(self):
        print(f"Автомобіль: {self.make} {self.model}, {self.year} р., тип пального: {self.fuel_type}")


# Підклас: Мотоцикл
class Motorcycle(Vehicle):
    def __init__(self, make, model, year, engine_volume):
        super().__init__(make, model, year)
        self.engine_volume = engine_volume

    def rev_engine(self):
        print(f"{self.make} {self.model} — двигун реве ({self.engine_volume} см³)!")

    def display_info(self):
        print(f"Мотоцикл: {self.make} {self.model}, {self.year} р., об’єм двигуна: {self.engine_volume} см³")


# Підклас: Велосипед
class Bicycle(Vehicle):
    def __init__(self, make, model, year, bike_type):
        super().__init__(make, model, year)
        self.bike_type = bike_type

    def ring_bell(self):
        print(f"{self.make} {self.model}: Дзінь-дзінь!")

    def display_info(self):
        print(f"Велосипед: {self.make} {self.model}, {self.year} р., тип: {self.bike_type}")


# Створюємо об’єкти для кожного з підкласів
car = Car("Toyota", "Corolla", 2020, "Бензин")
moto = Motorcycle("Yamaha", "MT-07", 2021, 689)
bike = Bicycle("Trek", "FX 3", 2022, "Гірський")

print("\n=== Інформація про транспорт ===")
car.display_info()
moto.display_info()
bike.display_info()

car.start_engine()
moto.rev_engine()
bike.ring_bell()


# ================================================
# ✅ Завдання 4: Поліморфізм
# ================================================

print("\n=== Демонстрація поліморфізму ===")

vehicles = [car, moto, bike]

for v in vehicles:
    v.display_info()
