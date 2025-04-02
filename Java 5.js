// 1. Об'єкт студента та метод для виведення інформації
function Student(name, specialty, averageGrade, missedClasses) {
    this.name = name;
    this.specialty = specialty;
    this.averageGrade = averageGrade;
    this.missedClasses = missedClasses;
}

Student.prototype.getInfo = function() {
    console.log(`Ім'я: ${this.name}, Спеціальність: ${this.specialty}, Середній бал: ${this.averageGrade}, Пропущені заняття: ${this.missedClasses}`);
};

const student1 = new Student("Олег", "Інформатика", 4.5, 2);
const student2 = new Student("Марія", "Математика", 4.8, 0);
const student3 = new Student("Андрій", "Фізика", 4.2, 3);

student1.getInfo.call(student2);
student1.getInfo.apply(student3);
const boundGetInfo = student1.getInfo.bind(student1);
boundGetInfo();

// 2. Дві кнопки з визначенням HTML та CSS
document.body.innerHTML += '<button id="htmlBtn">Що таке HTML?</button>';
document.body.innerHTML += '<button id="cssBtn">Що таке CSS?</button>';
document.body.innerHTML += '<p id="output"></p>';

document.getElementById("htmlBtn").addEventListener("click", function() {
    document.getElementById("output").textContent = "HTML - це мова розмітки гіпертексту, яка використовується для створення веб-сторінок.";
});

document.getElementById("cssBtn").addEventListener("click", function() {
    document.getElementById("output").textContent = "CSS - це мова стилів, яка використовується для оформлення веб-сторінок.";
});

