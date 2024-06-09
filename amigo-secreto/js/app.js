const inputNome = document.getElementById('nome-amigo');
const listaAmigos = document.getElementById('lista-amigos');
const listaSorteio = document.getElementById('lista-sorteio');

let nomesJaAdicinados = {};

function adicionar() {
  const nome = inputNome.value.trim();

  if (nome === '') {
    alert('Não é possível incluir nomes vazios!')
    return;
  }

  if (nomesJaAdicinados[nome.toLowerCase()]) {
    alert('Não adicione 2 nomes iguais!');
    return;
  }
  nomesJaAdicinados[nome.toLowerCase()] = true;

  if (!listaAmigos.textContent) {
    listaAmigos.textContent = `${nome}`
  } else {
    listaAmigos.textContent += `, ${nome}`
  }
  inputNome.value = '';
}

function sortear() {
  listaSorteio.innerHTML = '';
  const amigos = listaAmigos.textContent.split(', ');
  if (amigos.length <= 2) {
    alert('A lista de amigos é pequena de mais para um amigo secreto!');
    return;
  }
  embaralhar(amigos);

  for (let i = 0; i < amigos.length - 1; i++) {
    const amigo = amigos[i];
    const p = document.createElement('p');
    p.textContent = `${amigo} -> ${amigos[i + 1]}`
    listaSorteio.appendChild(p)
  }
  const p = document.createElement('p');
  p.textContent = `${amigos[amigos.length - 1]} -> ${amigos[0]}`
  listaSorteio.appendChild(p)
}

function embaralhar(array) {
  for (let i = array.length; i; i--) {
    const randomIndex = Math.floor(Math.random() * i);
    const temp = array[i - 1]
    array[i - 1] = array[randomIndex];
    array[randomIndex] = temp;
  }
}

function reiniciar() {
  listaAmigos.textContent = '';
  listaSorteio.innerHTML = '';
  nomesJaAdicinados = {};
}


// function sortear() {
//   const sorteados = {};
//   const jaSorteados = {};

//   const amigos = listaAmigos.textContent.split(', ')

//   for (let i = 0; i < amigos.length; i++) {
//     let randomIndex;
//     let randomAmigo;
//     do {
//       randomIndex = Math.floor(Math.random() * amigos.length);
//       randomAmigo = amigos[randomIndex]
//     } while (
//       jaSorteados[randomAmigo] ||
//       amigos[i] == randomAmigo
//     )
    
//     jaSorteados[randomAmigo] = true;
//     sorteados[amigos[i]] = amigos[randomIndex];
//   }

//   console.log(sorteados);
// }