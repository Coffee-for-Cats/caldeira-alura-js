const inputQuantidade = document.getElementById('quantidade')
const inputDe = document.getElementById('de')
const inputAte = document.getElementById('ate')
const numsPlaceholder = document.getElementById('nums-placeholder')
const botaoReiniciar = document.getElementById('btn-reiniciar')
const botaoSortear = document.getElementById('btn-sortear')

function sortear() {
  const quantidade = parseInt(inputQuantidade.value);
  const min = parseInt(inputDe.value);
  const max = parseInt(inputAte.value);

  const intervalo = max - min;

  //console.log('intervalo: ', intervalo);

  if (quantidade > intervalo) {
    alert('O intervalo é pequeno demais para gerar essa quantidade de números que não se repitam.')
    return;
  }

  // '+a' is a shorthand: String --> Number
  const nums = sortearNums(intervalo, quantidade).map(a => +a + min);
  numsPlaceholder.innerText = nums.join(' ');

  alterarStatusBotao()
}

function sortearNums(intervalo, qtd) {
  const jaSorteados = {};

  for (let i = 0; i < qtd; i++) {
    let num;
    do {
      // gera um número entre 0..intervalo,
      // +1   para incluir o próprio número,
      num = Math.floor(Math.random() * intervalo) + 1;
    } while (jaSorteados[num]);
    jaSorteados[num] = true;
  }

  return Object.keys(jaSorteados);
}

let reiniciarDesabilitado = true;
function alterarStatusBotao() {
  if (reiniciarDesabilitado) {
    botaoReiniciar.classList.remove('container__botao-desabilitado')
    botaoReiniciar.classList.add('container__botao')
  } else {
    botaoReiniciar.classList.add('container__botao-desabilitado')
    botaoReiniciar.classList.remove('container__botao')
  }
  
  reiniciarDesabilitado = !reiniciarDesabilitado;
}

function reiniciar() {
  inputQuantidade.value = '';
  inputAte.value = '';
  inputDe.value = '';
  numsPlaceholder.innerText = 'nenhum até agora';
  alterarStatusBotao();
}

