const games = document.getElementsByClassName('dashboard__items__item');

function alterarStatus(id) {
  const game = games[id - 1];
  const button = game.querySelector('.dashboard__item__button');
  // console.log('button: ', button)
  const image = game.querySelector('.dashboard__item__img');
  // console.log('image: ', image)

  if (button.classList.contains('dashboard__item__button--return')) {
    button.classList.remove('dashboard__item__button--return');
    button.textContent = "Alugar"
    image.classList.remove('dashboard__item__img--rented');
  } else {
    button.classList.add('dashboard__item__button--return');
    button.textContent = "Devolver"
    image.classList.add('dashboard__item__img--rented');
  }
}