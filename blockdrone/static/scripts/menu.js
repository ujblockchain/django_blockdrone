const MENU_TOGGLE = document.getElementById('menu-toggle');
const MENU = document.getElementById('menu');
const MENU_LINKS = document.getElementsByClassName('nav__link');
const HTML = document.getElementById('html');
let showMenu = false;

MENU_TOGGLE.addEventListener('click', () => {
  showMenu = !showMenu;

  MENU.style.transform = showMenu ? 'translateX(0)' : 'translateX(-100vw)';
});

for (let i = 0; i < MENU_LINKS.length; i++) {
  MENU_LINKS[0].addEventListener('click', () => {
    MENU.style.transform = 'translateX(-100vw)';
    showMenu = false;
  })
}