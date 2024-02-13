const PILOTS = document.getElementsByClassName('pilots-list__item');
const PAGINATE_BACK = document.getElementById('paginate-back');
const PAGINATE_NEXT = document.getElementById('paginate-next');
const PAGINATE_NUMBER = document.getElementById('paginate-number');
const itemsPerPage = 3;
const NUMBER_OF_PAGES = PILOTS.length % itemsPerPage === 0 ? PILOTS.length / itemsPerPage : Math.ceil(PILOTS.length / itemsPerPage);
let currentPage = 1;

PAGINATE_NUMBER.innerText = currentPage;

for (var i = 0; i < PILOTS.length; i++) {
  if (i >= (currentPage - 1) * itemsPerPage && i < currentPage * itemsPerPage) {
    PILOTS[i].style.display = 'block';
  }
}

PAGINATE_BACK.addEventListener('click', () => {
  if (currentPage > 1) {
    currentPage -= 1;
  }

  PAGINATE_NUMBER.innerText = currentPage;

  for (var i = 0; i < PILOTS.length; i++) {
    if (i >= (currentPage - 1) * itemsPerPage && i < currentPage * itemsPerPage) {
      PILOTS[i].style.display = 'block';
    } else {
      PILOTS[i].style.display = 'none';
    }
  }
});

PAGINATE_NEXT.addEventListener('click', () => {
  if (currentPage < NUMBER_OF_PAGES) {
    currentPage += 1;
  }

  PAGINATE_NUMBER.innerText = currentPage;

  for (var i = 0; i < PILOTS.length; i++) {
    if (i >= (currentPage - 1) * itemsPerPage && i < currentPage * itemsPerPage) {
      PILOTS[i].style.display = 'block';
    } else {
      PILOTS[i].style.display = 'none';
    }
  }
});