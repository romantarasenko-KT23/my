let name = "Іван";
let city = name;
console.log(city); // Виведе: Іван


let userName = "Olga"; // Змінна "name" уже існує, перейменуємо на "userName"
console.log(`привіт ${1}`);       // привіт 1
console.log(`привіт ${"name"}`);  // привіт name
console.log(`привіт ${userName}`); // привіт Olga


let a = "5";
let b = "13cvb";
let c = "12.9sxdcfgv";

console.log(Number(a));    // 5
console.log(parseInt(b));  // 13
console.log(parseFloat(c));// 12.9



let sum = 0.1 + 0.2;
sum = parseFloat(sum.toFixed(1)); // Оновлюємо значення змінної
console.log(sum); // 0.3


console.log(Math.max(20, 10, 50, 40)); // 50


let random = Math.random() * (4 - 2) + 2;
console.log(random);


const message = "Welcome to Bahamas!";
console.log(message.length); // 19


console.log(message.toUpperCase()); // "WELCOME TO BAHAMAS!"


let person = {};
person.name = "Іван";
person.age = 25;
person.city = "Київ";

console.log(person);

delete person.city;

person["like flowers"] = true;

console.log(person);

for (let key in person) {
    console.log(`${key}: ${person[key]}`);
  }







  
  