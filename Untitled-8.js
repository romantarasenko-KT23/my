<!DOCTYPE html>
<html>
<body>

<div data-widget-name="menu">Виберіть жанр</div>

<script>
  // Отримуємо елемент за допомогою CSS-селектора [data-widget-name]
  let elem = document.querySelector('[data-widget-name]');

  // Читаємо значення атрибута
  let value = elem.dataset.widgetName;

  // Виводимо значення в консоль
  console.log(value); // "menu"
</script>

</body>
</html>

