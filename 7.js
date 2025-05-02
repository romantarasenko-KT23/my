function Calculator() {
  this.read = function() {
    this.a = +prompt("Введіть перше число:", 0);
    this.b = +prompt("Введіть друге число:", 0);
  };

  this.sum = function() {
    return this.a + this.b;
  };

  this.mul = function() {
    return this.a * this.b;
  };
}

// Приклад використання:
let calc = new Calculator();
calc.read();
alert("Сума: " + calc.sum());
alert("Добуток: " + calc.mul());