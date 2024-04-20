const sidebar = document.querySelector(".Rsidebar");
const sidebarClose = document.querySelector("#sidebar-close");
const menu = document.querySelector(".menu-content");
const menuItems = document.querySelectorAll(".submenu-item");
const subMenuTitles = document.querySelectorAll(".submenu .menu-title");
const counter = document.querySelector('.count')
sidebarClose.addEventListener("click", () => {
  sidebar.classList.toggle("close")
  counter.style.display = 'none';
});

menuItems.forEach((item, index) => {
  item.addEventListener("click", () => {
    console.log("Click ")
    menu.classList.add("submenu-active");
    item.classList.add("show-submenu");
    menuItems.forEach((item2, index2) => {
      if (index !== index2) {
        item2.classList.remove("show-submenu");
      }
    });
  });
});

subMenuTitles.forEach((title) => {
  title.addEventListener("click", () => {
    menu.classList.remove("submenu-active");
  });
});

console.log(menuItems, subMenuTitles);
