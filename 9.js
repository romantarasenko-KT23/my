<button onclick="document.getElementById('element').style.display = 'none'">Сховати елемент</button>
<div id="element">Цей елемент зникне</div>




<button onclick="this.style.display = 'none'">Натисни, щоб кнопка зникла</button>




<ul id="tree">
  <li>
    <span onclick="toggle(this)">📁 Батько
      <ul>
        <li>📄 Дитина 1</li>
        <li>📄 Дитина 2</li>
      </ul>
    </span>
  </li>
</ul>

<script>
function toggle(element) {
  const childList = element.querySelector("ul");
  if (childList) {
    childList.style.display = (childList.style.display === "none") ? "block" : "none";
  }
}
</script>

<style>
ul ul {
  margin-left: 20px;
}
</style>