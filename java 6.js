// Клас для зберігання даних про абонента
class Abonent {
  constructor() {
    this.name = "";
    this.number = "";
  }

  // Метод для встановлення імені та номера
  set(name, number) {
    this.name = name;
    this.number = number;
  }

  // Метод для виводу даних
  get() {
    console.log(`Ім'я: ${this.name}, Номер: ${this.number}`);
  }
}

// Створюємо трьох абонентів
const abonent1 = new Abonent();
abonent1.set("Олександр", "+380501234567");

const abonent2 = new Abonent();
abonent2.set("Марія", "+380671112233");

const abonent3 = new Abonent();
abonent3.set("Іван", "+380931234567");

// Зберігаємо абонентів у масив
const abonents = [abonent1, abonent2, abonent3];

// Виводимо всіх абонентів
abonents.forEach((abonent, index) => {
  console.log(`Абонент №${index + 1}:`);
  abonent.get();
});