# Questão 1

class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self._ativo = True

# Questão 2

    def __str__(self):
        return (f'O livro {self.titulo}, tem como Autora a {self.autor} e foi lançado em {self.ano_publicacao}.')

# livro1=Livro('Vermelho Branco Sangue Azul','Casey McQuiston', 2019)
# livro2=Livro('Heartstopper','Alice Oseman', 2016)
# print(livro1)
# print(livro2)

# Questão 3

    def livro_emprestado(self):
        self._ativo = False

    # Adicionando um método para acessar o status do livro
    @property
    def ativo(self):
        return self._ativo
    
# livro1=Livro('Vermelho Branco Sangue Azul','Casey McQuiston', 2019)
# livro2=Livro('Heartstopper','Alice Oseman', 2016)

# livro1.livro_emprestado()
# # livro2.livro_emprestado()

# print('')
# print(livro1)
# print("Status do livro 1:", "Disponível" if livro1.ativo else "Não disponível")
# print('')
# print(livro2)
# print("Status do livro 2:", "Disponível" if livro2.ativo else "Não disponível")
# print('')

# Questão 4
@staticmethod
def verificar_disponibilidade(ano):
   livros_disponiveis=[livro for livro in Livro.livros if livro.ano_publicacao == ano and livro.disponivel]
   for livro in livros_disponiveis:
       print(f'Livros disponíveis em {ano}: {livro}')
    
livro1=Livro('Vermelho Branco Sangue Azul','Casey McQuiston', 2019)
livro2=Livro('Heartstopper','Alice Oseman', 2016)

Livro.livros=[livro1,livro2]
    
    