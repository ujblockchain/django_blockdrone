// let userInfo = JSON.parse(sessionStorage.getItem('user-info'));
// const WELCOME = document.getElementById('welcome');

// if (sessionStorage.getItem('signedIn') === 'true') {
//   WELCOME.innerText = `Welcome, ${userInfo.firstName[0].toUpperCase()}${userInfo.firstName.substr(1)}`
// }

// const BLOCKED = document.getElementsByClassName('blocked__item');
// const PAGINATE_BACK = document.getElementById('paginate-back');
// const PAGINATE_NEXT = document.getElementById('paginate-next');
// const PAGINATE_NUMBER = document.getElementById('paginate-number');
// const itemsPerPage = 5;
// const NUMBER_OF_PAGES = BLOCKED.length % itemsPerPage === 0 ? BLOCKED.length / itemsPerPage : Math.ceil(BLOCKED.length / itemsPerPage);
// let currentPage = 1;

// PAGINATE_NUMBER.innerText = currentPage;

// for (var i = 0; i < BLOCKED.length; i++) {
//   if (i >= (currentPage - 1) * itemsPerPage && i < currentPage * itemsPerPage) {
//     BLOCKED[i].style.display = 'block';
//   }
// }

// PAGINATE_BACK.addEventListener('click', () => {
//   if (currentPage > 1) {
//     currentPage -= 1;
//   }

//   PAGINATE_NUMBER.innerText = currentPage;

//   for (var i = 0; i < BLOCKED.length; i++) {
//     if (i >= (currentPage - 1) * itemsPerPage && i < currentPage * itemsPerPage) {
//       BLOCKED[i].style.display = 'block';
//     } else {
//       BLOCKED[i].style.display = 'none';
//     }
//   }
// });

// PAGINATE_NEXT.addEventListener('click', () => {
//   if (currentPage < NUMBER_OF_PAGES) {
//     currentPage += 1;
//   }

//   PAGINATE_NUMBER.innerText = currentPage;

//   for (var i = 0; i < BLOCKED.length; i++) {
//     if (i >= (currentPage - 1) * itemsPerPage && i < currentPage * itemsPerPage) {
//       BLOCKED[i].style.display = 'block';
//     } else {
//       BLOCKED[i].style.display = 'none';
//     }
//   }
// });