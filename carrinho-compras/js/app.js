const optionInput = document.getElementById('produto');
const qtdInput = document.getElementById('quantidade');
const carrinhoSection = document.getElementById('lista-produtos');
const valorTotal = document.getElementById('valor-total');

function adicionar() {
  const [name, price] = optionInput.value.split(' - ')
  const qtd = qtdInput.value;

  if (qtd < 1) {
    alert('A quantidade não pode ser menor do que 1!');
    return;
  }
  
  const totalAtual = parseInt(valorTotal.innerText.split('$')[1]);
  const novoValor = parseInt(price.split('$')[1])
  const totalPrice = novoValor * qtd;

  carrinhoSection.appendChild(
    new Product(name, qtd, `R$ ${totalPrice}`)
  )

  console.log()
  valorTotal.innerText = `R$ ${totalAtual + novoValor * qtd}`;
}

class Product {
  constructor(name, qtd, value) {
    const item = document.createElement('section');
    item.classList.add('carrinho__produtos__produto');

    const qtdSpan = document.createElement('span');
    qtdSpan.classList.add('texto-azul')
    qtdSpan.innerText = `${qtd}x `;
    
    const nameSpan = document.createTextNode(name);
    
    const valueSpan = document.createElement('span');
    valueSpan.classList.add('texto-azul');
    valueSpan.innerText = ` ${value}`;
    
    item.appendChild(qtdSpan)
    item.appendChild(nameSpan)
    item.appendChild(valueSpan)

    console.log(item)

    return item;
  }
}

function limpar() {
  carrinhoSection.innerHTML = '';
  valorTotal.innerText = 'R$ 0'
}