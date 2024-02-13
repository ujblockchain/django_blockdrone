const FIRST_NAME = document.getElementById('first-name');
const LAST_NAME = document.getElementById('last-name');
const EMAIL = document.getElementById('email');
const ACCOUNT_IMAGE = document.getElementById('account-image');
let userInfo = JSON.parse(sessionStorage.getItem('user-info'));

FIRST_NAME.value = `${userInfo.firstName[0].toUpperCase()}${userInfo.firstName.substr(1)}`;
LAST_NAME.value = `${userInfo.surname[0].toUpperCase()}${userInfo.surname.substr(1)}`;
EMAIL.value = userInfo.email;
ACCOUNT_IMAGE.src = userInfo.imageUrl;

const WELCOME = document.getElementById('welcome');

if (sessionStorage.getItem('signedIn') === 'true') {
  WELCOME.innerText = `Welcome, ${userInfo.firstName[0].toUpperCase()}${userInfo.firstName.substr(1)}`
}