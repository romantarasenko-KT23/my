function main() {
    // Запитуємо у користувача два числа
    let num1 = parseFloat(prompt("Введіть перше число:"));
    let num2 = parseFloat(prompt("Введіть друге число:"));
    
    // Виконуємо арифметичні операції
    let addition = num1 + num2;
    let subtraction = num1 - num2;
    let multiplication = num1 * num2;
    
    // Перевіряємо, щоб не було ділення на нуль
    let division = num2 !== 0 ? num1 / num2 : "Помилка: ділення на нуль";
    let remainder = num2 !== 0 ? num1 % num2 : "Помилка: ділення на нуль";
    
    // Виводимо результати
    console.log(`Сума: ${addition}`);
    console.log(`Різниця: ${subtraction}`);
    console.log(`Добуток: ${multiplication}`);
    console.log(`Частка: ${division}`);
    console.log(`Остача від ділення: ${remainder}`);
}

main();

function main() {
    // Запитуємо у користувача вік
    let age = parseInt(prompt("Введіть ваш вік:"));
    
    // Перевіряємо, чи є користувач повнолітнім
    if (age >= 18) {
        console.log("Ви повнолітній.");
    } else {
        console.log("Ви неповнолітній.");
    }
}

main();
function main() {
    // Запитуємо у користувача інформацію
    let hasSubscription = prompt("Чи маєте ви абонемент? (true/false)").toLowerCase() === "true";
    let balance = parseFloat(prompt("Скільки у вас на рахунку грошей?"));
    
    // Перевіряємо умови доступу
    if (hasSubscription || balance > 100) {
        console.log("Доступ дозволено");
    } else {
        console.log("Доступ заборонено");
    }
}

main();
function main() {
    // Запитуємо у користувача число
    let number = parseInt(prompt("Введіть число:"));
    
    // Визначаємо, чи є число парним або непарним за допомогою тернарного оператора
    let result = (number % 2 === 0) ? "парне" : "непарне";
    
    // Виводимо результат
    console.log(`Число ${number} є ${result}.`);
}

main();
function main() {
    // Запитуємо у користувача початковий баланс
    let balance = parseFloat(prompt("Введіть ваш поточний баланс:"));
    
    // Додавання 500 грн
    balance += 500;
    
    // Зняття 200 грн
    balance -= 200;
    
    // Нарахування 5% від залишку
    balance += balance * 0.05;
    
    // Виводимо підсумковий баланс
    console.log(`Ваш підсумковий баланс: ${balance.toFixed(2)} грн`);
}

main();
function main() {
    // Запитуємо у користувача число дня тижня
    let dayNumber = parseInt(prompt("Введіть число від 1 до 7, що відповідає дню тижня:"));
    let dayName;
    
    // Визначаємо день тижня за допомогою switch
    switch (dayNumber) {
        case 1:
            dayName = "Понеділок";
            break;
        case 2:
            dayName = "Вівторок";
            break;
        case 3:
            dayName = "Середа";
            break;
        case 4:
            dayName = "Четвер";
            break;
        case 5:
            dayName = "П'ятниця";
            break;
        case 6:
            dayName = "Субота";
            break;
        case 7:
            dayName = "Неділя";
            break;
        default:
            dayName = "Некоректне число, введіть від 1 до 7";
    }
    
    // Виводимо назву дня тижня
    console.log(dayName);
}

main();
function main() {
    // Запитуємо у користувача два числа
    let num1 = parseInt(prompt("Введіть перше число:"));
    let num2 = parseInt(prompt("Введіть друге число:"));
    
    // Виконуємо побітові операції
    let andResult = num1 & num2;
    let orResult = num1 | num2;
    let xorResult = num1 ^ num2;
    let leftShift = num1 << 1;
    let rightShift = num1 >> 1;
    
    // Виводимо результати
    console.log(`Побітове І (AND): ${andResult}`);
    console.log(`Побітове АБО (OR): ${orResult}`);
    console.log(`Побітове XOR: ${xorResult}`);
    console.log(`Зсув вліво (<< 1): ${leftShift}`);
    console.log(`Зсув вправо (>> 1): ${rightShift}`);
}

main();
function main() {
    // Запитуємо у користувача два числа
    let num1 = parseInt(prompt("Введіть перше число:"));
    let num2 = parseInt(prompt("Введіть друге число:"));
    
    // Виконуємо побітові операції
    let andResult = num1 & num2;
    let orResult = num1 | num2;
    let xorResult = num1 ^ num2;
    let leftShift = num1 << 1;
    let rightShift = num1 >> 1;
    
    // Виводимо результати
    console.log(`Побітове І (AND): ${andResult}`);
    console.log(`Побітове АБО (OR): ${orResult}`);
    console.log(`Побітове XOR: ${xorResult}`);
    console.log(`Зсув вліво (<< 1): ${leftShift}`);
    console.log(`Зсув вправо (>> 1): ${rightShift}`);
}

main();
