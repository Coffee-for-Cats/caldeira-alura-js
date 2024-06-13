from models.avaliacao import Avaliacao

class Restaurante: 
  restaurantes = []

  def __init__(self, nome: str, categoria: str):
    self._nome = nome.title()
    self._categoria = categoria
    self._ativo = False
    self._avaliacao = []

    Restaurante.restaurantes.append(self)
  
  def __str__(self):
    return f"{self._nome} | {self._categoria}"

  def ativar(self):
    self._ativo = True

  def receber_avaliacao(self, cliente, nota):
    avaliacao = Avaliacao(cliente, nota)
    self._avaliacao.append(avaliacao)

  @property
  def ativo(self):
    return "☑️" if self._ativo else "❌"

  @property
  def media_avaliacoes(self):
    if not self._avaliacao:
      return 0
    soma_das_notas = sum(avaliacao._notas for avaliacao in self._avaliacao)
    qtd_notas = len(self._avaliacao)
    media = round(soma_das_notas / qtd_notas, 1)
    return media

  # cls stands for class. No use at all.
  @classmethod
  def listar(cls):
    print(f"{'Nome'.ljust(25)} | {'Categoria'.ljust(15)} | {'Ativo'.ljust(15)} | {'Avaliacao'.ljust(15)}")
    for res in cls.restaurantes:
      print(f"{res._nome.ljust(25)} | {res._categoria.ljust(15)} | {res.ativo.ljust(14)} | {str(res.media_avaliacoes).ljust(15)}")

# res_praca._ativo = True # funciona
# res_praca.nome = "Restaurante da Praça"

Restaurante.listar();