import os

from models.restaurante import Restaurante

restaurantes = [
  Restaurante("Praça", "Japonesa"),
  Restaurante("Pizza Suprema", "Italiana")
]

def menu():
  """
  Menu central da aplicação; limpa a tela e mostra as opções que o usuário pode executar,
  além de chamar a função correspondente a tal opção. opcao_invalida() é
  chamada caso um valor inválido seja digitado.
  """
  os.system('cls')
  print("""
  █▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
  ▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █ █ █▀▀ █▀▄ ██▄ ▄█ ▄█\n
  """)
  print("1. Cadastrar restaurante")
  print("2. Exibir restaurantes")
  print("3. Alternar estado do restaurante")
  print("4. Sair")
  
  try:
    op = int(input())
  except:
    opcao_invalida()

  # print(f"Você escolheu {op}.")
  if op == 1: cadastrar()
  elif op == 2: exibir()
  elif op == 3: ativar()
  elif op == 4: sair()
  else: opcao_invalida()


def retornar():
  input("Pressione qualquer tecla para retornar ao menu.")
  menu()


def cadastrar():
  """
  Responsável por cadastrar um novo restaurante
  Inputs:
    - nome do restaurante
    - categoria

  Outputs:
   - adiciona o restaurante na lista restaurantes
  """
  print("Cadastro de novos restaurantes")
  nome_res = input("Nome do restaurante: ")
  categoria_res = input("Categoria do restaurante: ")

  res = Restaurante(nome_res, categoria_res)

  # res = {
  #   "nome": nome_res, 
  #   "categoria": categoria_res, 
  #   "ativo": False
  # }
  restaurantes.append(res)
  #
  retornar()


def exibir():
  """
  Busca receitas por categoria e retorna uma lista de receitas
  Inputs:
   - categoria (str): A categoria da receita desejada

  Outputs:
   - list: Uma lista contendo as receitas da categoria especificada
  """

  print("Restaurantes já cadastrados:")
  Restaurante.listar()
  # for res in restaurantes:
  #   ativo = "ativo" if res['ativo'] else "desativado"
  #   print(f"> {res['nome'].ljust(20)} | {res['categoria'].ljust(20)} | {ativo}")
  print('\n')
  #
  retornar()


def ativar():
  """
  Alterna o status de um restaurante.
  Inputs:
   - nome do restaurante (str)
  Outputs:
   - modifica o status do restaurante com o nome
  """
  print("Alternar estado do restaurante")
  nome = input("Digite o nome do restaurante que deseja alternar o estado: ")
  encontrado = False
  for res in Restaurante.restaurantes:
    if res._nome == nome:
      res.ativar()
      encontrado = True
    # if res['nome'] == nome:
    #   encontrado = True
    #   res['ativo'] = not res['ativo']
    #   # bem estranho na verdade, mas funciona bem.
    #   acao = 'ativado' if res['ativo'] else 'desativado'
    #   mensagem = f"O restaurante {res['nome']} foi {acao} com sucesso."
    #   print(mensagem)
  
  if not encontrado:
    print("Restaurante não encontrado.")
  #
  retornar()


def sair():
  """
  Limpa a tela e sai do programa;
  Nada é executado, a função apenas não chama o menu() novamente
  """
  os.system('cls')
  print("Encerrando programa...")


def opcao_invalida():
  """
  Printa que a opção é inválida e retorna para o menu
  """
  print("Opção Inválida!")
  retornar()


# def main():
#   menu()


if __name__ == "__main__":
  menu()