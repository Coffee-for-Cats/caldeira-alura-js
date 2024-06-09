const qtdLivreSuperior = document.getElementById('qtd-superior');
const qtdLivrePista = document.getElementById('qtd-pista');
const qtdLivreInferior = document.getElementById('qtd-inferior');

const inputQtd = document.getElementById('qtd');
const inputIngresso = document.getElementById('tipo-ingresso');

function comprar() {
  if (inputQtd.value < 1) {
    alert('O número de ingressos comprados não pode ser menor do que 1!')
    return
  }

  let target;

  switch (inputIngresso.value) {
    case 'inferior':
      target = qtdLivreInferior;
      break;
    case 'superior':
      target = qtdLivreSuperior;
      break;
    case 'pista':
      target = qtdLivrePista;
      break;
    default:
      alert("Tipo de ingresso inválido.")
  }

  if (+target.innerText < inputQtd.value) {
    alert('Não há lugares disponíveis o bastante!')
    return
  }

  target.innerText -= inputQtd.value;
}