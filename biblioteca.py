# Questão 5
from modelos.livro import Livro

# Questão 6
livro_biblioteca = Livro('Predador Americano', 'Maurin Calamn', 2019)
print (f'Antes de emprestar (biblioteca); Livro disponível? {livro_biblioteca}')
livro_biblioteca.emprestar()
print (f'Antes de emprestar (biblioteca); Livro disponível? {livro_biblioteca}')