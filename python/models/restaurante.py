class Restaurante: 
  restaurantes = []

  def __init__(self, nome: str, categoria: str):
    self._nome = nome.title()
    self._categoria = categoria
    self._ativo = False

    Restaurante.restaurantes.append(self)
  
  def __str__(self):
    return f"{self._nome} | {self._categoria}"

  def ativar(self):
    self._ativo = True

  @property
  def ativo(self):
    return "☑️" if self._ativo else "❌"

  # cls stands for class. No use at all.
  @classmethod
  def listar(cls):
    print(f"{'Nome'.ljust(25)} | {'Categoria'.ljust(15)} | {'Ativo'.ljust(15)}")
    for res in cls.restaurantes:
      print(f"{res._nome.ljust(25)} - {res._categoria.ljust(15)} | {res.ativo.ljust(15)}")

# res_praca._ativo = True # funciona
# res_praca.nome = "Restaurante da Praça"

Restaurante.listar();