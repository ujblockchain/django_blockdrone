const SIGN_OUT = document.getElementById('sign-out');
const SIGN_OUT_MENU = document.getElementById('sign-out-menu');

const signout = () => {
  sessionStorage.removeItem('user-creds');
  sessionStorage.removeItem('user-info');
  sessionStorage.setItem('signedIn','false');
  window.location.href = '../../index.html';
}

SIGN_OUT.addEventListener('click', signout);
SIGN_OUT_MENU.addEventListener('click', signout);