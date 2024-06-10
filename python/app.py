import os

restaurantes = [
  {
    "nome": "Praça",
    "categoria": "Japonesa",
    "ativo": False
  },
  {
    "nome": "Pizza Suprema",
    "categoria": "italiana",
    "ativo": True
  }
]

def menu():
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
  print("Cadastro de novos restaurantes")
  nome_res = input("Nome do restaurante: ")
  categoria_res = input("Categoria do restaurante: ")

  res = {
    "nome": nome_res, 
    "categoria": categoria_res, 
    "ativo": False
  }
  restaurantes.append(res)
  #
  retornar()


def exibir():
  print("Restaurantes já cadastrados:")
  for res in restaurantes:
    ativo = "ativo" if res['ativo'] else "desativado"
    print(f"> {res['nome'].ljust(20)} | {res['categoria'].ljust(20)} | {ativo}")
  print('\n')
  #
  retornar()


def ativar():
  print("Alternar estado do restaurante")
  nome = input("Digite o nome do restaurante que deseja alternar o estado: ")
  encontrado = False
  for res in restaurantes:
    if res['nome'] == nome:
      encontrado = True
      res['ativo'] = not res['ativo']
      # bem estranho na verdade, mas funciona bem.
      acao = 'ativado' if res['ativo'] else 'desativado'
      mensagem = f"O restaurante {res['nome']} foi {acao} com sucesso."
      print(mensagem)
  
  if not encontrado:
    print("Restaurante não encontrado.")
  #
  retornar()


def sair():
  executando = False
  os.system('cls')
  print("Encerrando programa...")


def opcao_invalida():
  print("Opção Inválida!")
  retornar()


# def main():
#   menu()


if __name__ == "__main__":
  menu()