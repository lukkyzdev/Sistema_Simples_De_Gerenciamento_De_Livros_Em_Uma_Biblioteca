class Livro:
    def __init__(self, titulo, autor, genero, quantidade):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.quantidade = quantidade

livros = []

def cadrastrar_livro():
  titulo = input("Digite o titulo do livro: ")
  autor = input("Digite o autor do livro: ")
  genero = input("Digite o genero do livro: ")
  quantidade = int(input("Digite a quantidade do livro: "))

  novo_livro = Livro(titulo, autor, genero, quantidade)
  livros.append(novo_livro)
  print("Livro cadastrado com sucesso!")

def listar_livros():
  if not livros:
    print("Nenhum livro cadastrado.")
  else:
    print("Lista de Livros:")
    for livro in livros:
      print(f"Título: {livro.titulo}")

def buscar_livro(titulo):
  for livro in livros:
    if livro.titulo.lower() == titulo.lower():
      return livro
  return None

import matplotlib.pyplot as plt

def gerar_grafico():
    if not livros:
        print("Nenhum livro cadastrado para gerar o gráfico.")
        return

    generos = {}
    for l in livros:
        generos[l.genero] = generos.get(l.genero, 0) + l.quantidade

    plt.bar(generos.keys(), generos.values())
    plt.title("Quantidade de livros por gênero")
    plt.xlabel("Gênero")
    plt.ylabel("Quantidade")
    plt.show()

# TESTANDO O SISTEMA
if __name__ == "__main__":
    livros.append(Livro("O Senhor dos Anéis", "J.R.R. Tolkien", "Fantasia", 5))
    livros.append(Livro("Dom Casmurro", "Machado de Assis", "Romance", 7))
    livros.append(Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", "Infantil", 12))

    listar_livros()

    print("\n--- Teste de busca ---")
    livro_encontrado = buscar_livro("Dom Casmurro")
    if livro_encontrado:
        print(f"Livro encontrado: {livro_encontrado.titulo} | {livro_encontrado.autor}")
    else:
        print("Livro não encontrado.")

    livro_inexistente = buscar_livro("Livro que não existe")
    if livro_inexistente:
        print(f"Livro encontrado: {livro_inexistente.titulo}")
    else:
        print("Livro não encontrado.")

    print("\n--- Gerando gráfico ---")
    gerar_grafico()

#Observações: Foi bem dificil, como é meu segundo código eu pedi vários auxílios, mas estou melhorando.
