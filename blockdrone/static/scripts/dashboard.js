const WELCOME = document.getElementById('welcome');
let userInfo = JSON.parse(sessionStorage.getItem('user-info'));

if (sessionStorage.getItem('signedIn') === 'true') {
  WELCOME.innerText = `Welcome, ${userInfo.firstName[0].toUpperCase()}${userInfo.firstName.substr(1)}`
}

const USER_NAME = document.getElementById('user-name');
const MEMBER_SINCE = document.getElementById('member-since');

const dateArray = userInfo.createdAt.split(' ');

USER_NAME.innerText = `${userInfo.firstName[0].toUpperCase()}${userInfo.firstName.substr(1)} ${userInfo.surname[0].toUpperCase()}.`;
MEMBER_SINCE.innerText = `${dateArray[2]} ${dateArray[1]} ${dateArray[3]}`;

const JOBS = document.getElementsByClassName('dashboard__item');
const PAGINATE_BACK = document.getElementById('paginate-back');
const PAGINATE_NEXT = document.getElementById('paginate-next');
const PAGINATE_NUMBER = document.getElementById('paginate-number');
const NUMBER_OF_PAGES = JOBS.length % 3 === 0 ? JOBS.length / 3 : Math.ceil(JOBS.length / 3);
const itemsPerPage = 3;
let currentPage = 1;

PAGINATE_NUMBER.innerText = currentPage;

for (var i = 0; i < JOBS.length; i++) {
  if (i >= (currentPage - 1) * itemsPerPage && i < currentPage * itemsPerPage) {
    JOBS[i].style.display = 'block';
  }
}

PAGINATE_BACK.addEventListener('click', () => {
  if (currentPage > 1) {
    currentPage -= 1;
  }

  PAGINATE_NUMBER.innerText = currentPage;

  for (var i = 0; i < JOBS.length; i++) {
    if (i >= (currentPage - 1) * itemsPerPage && i < currentPage * itemsPerPage) {
      JOBS[i].style.display = 'block';
    } else {
      JOBS[i].style.display = 'none';
    }
  }
});

PAGINATE_NEXT.addEventListener('click', () => {
  if (currentPage < NUMBER_OF_PAGES) {
    currentPage += 1;
  }

  PAGINATE_NUMBER.innerText = currentPage;

  for (var i = 0; i < JOBS.length; i++) {
    if (i >= (currentPage - 1) * itemsPerPage && i < currentPage * itemsPerPage) {
      JOBS[i].style.display = 'block';
    } else {
      JOBS[i].style.display = 'none';
    }
  }
});