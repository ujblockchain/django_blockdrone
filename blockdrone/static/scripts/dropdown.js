const DROPDOWN_BUTTON = document.getElementById('dropdown-button');
const DROPDOWN_CONTENT = document.getElementById('dropdown-content');
const DROPDOWN_BACKGROUND = document.getElementById('dropdown-background');
const DROPDOWN_BUTTON_MENU = document.getElementById('dropdown-button-menu');
const DROPDOWN_CONTENT_MENU = document.getElementById('dropdown-content-menu');
const DROPDOWN_BACKGROUND_MENU = document.getElementById('dropdown-background-menu');
const BODY = document.getElementById('page-top');

DROPDOWN_BUTTON.addEventListener('click', () => {
  let showDropdown = false;

  showDropdown = !showDropdown;

  DROPDOWN_CONTENT.style.display = showDropdown ? 'block' : 'none';
  DROPDOWN_BACKGROUND.style.display = showDropdown ? 'block' : 'none';
});

DROPDOWN_BACKGROUND.addEventListener('click', () => {
  DROPDOWN_CONTENT.style.display = 'none';
  DROPDOWN_BACKGROUND.style.display = 'none';
})

DROPDOWN_BUTTON_MENU.addEventListener('click', () => {
  let showDropdown = false;

  showDropdown = !showDropdown;

  DROPDOWN_CONTENT_MENU.style.display = showDropdown ? 'block' : 'none';
  DROPDOWN_BACKGROUND_MENU.style.display = showDropdown ? 'block' : 'none';
});

DROPDOWN_BACKGROUND_MENU.addEventListener('click', () => {
  DROPDOWN_CONTENT_MENU.style.display = 'none';
  DROPDOWN_BACKGROUND_MENU.style.display = 'none';
})

const DROPDOWN_USER_NAME = document.getElementById('dropdown-user-name');
const DROPDOWN_USER_NAME_MENU = document.getElementById('dropdown-user-name-menu');

DROPDOWN_USER_NAME.innerText = `${userInfo.firstName[0].toUpperCase()}${userInfo.firstName.substr(1)} ${userInfo.surname[0].toUpperCase()}.`;
DROPDOWN_USER_NAME_MENU.innerText = `${userInfo.firstName[0].toUpperCase()}${userInfo.firstName.substr(1)} ${userInfo.surname[0].toUpperCase()}.`;