# class Livro:
#     def __init__(self, titulo, autor, paginas):
#         self.titulo = titulo
#         self.autor = autor
#         self.paginas = paginas
        
#     def __str__(self):
#         return f'{self.titulo} por {self.autor} - {self.paginas} páginas'
    
#     @property
#     def titulo_autor(self):
#         return f'{self.titulo} por {self.autor}'
    
#     def aumentar_paginas(self, quantidade):
#         self.paginas += quantidade

# livro1=Livro('Dives','Natos',50)
# print(livro1)
# print('')

# livro1.aumentar_paginas(90)
# print(livro1)

# # Questão 1
# class Pessoa:
#     def __init__(self, nome, idade, profissao):
#         self.nome = nome
#         self.idade = idade
#         self.profissao = profissao
        
#     def __str__(self):
#         return f'{self.nome}, {self.idade} anos, {self.profissao}'
    
#     def aniversario (self):
#         self.idade += 1
        
#     @property
#     def saudacao(self):
#         if self.profissao:
#             print (f'Olá sou {self.nome}! Sou {self.profissao}.')
#         else:
#             print (f'Olá sou {self.nome}')
        
# pessoa1=Pessoa('Armando',30,'Dentista')
# print(pessoa1)
# print('')

# pessoa1.aniversario()
# print(pessoa1)
# print('')

# pessoa1.saudacao
# print(pessoa1)
# print('')

# Questão 2 
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self._ativo = False #atributo protegido
        
# Questão 3
    def __str__(self):
        return f'Conta de {self.titular} - Saldo R${self.saldo}'
    
# conta1=ContaBancaria('Philip', 2.500)
# conta2=ContaBancaria('Joe', 3.700)
    
# print('')
# print(conta1)
# print(conta2)
# print('')


# Questão 4
    @classmethod
    def ativar_conta(cls):
        cls._ativo = True
        # return cls._ativo
        
conta3=ContaBancaria('Penelope', 3.58)
print (f'Antes de ativar: Conta Ativa? {conta3._ativo}')
ContaBancaria.ativar_conta(conta3)
print (f'Depois de ativar: Conta Ativa? {conta3._ativo}')

# Questão 5 e 6
# class ContaBancariaPythonica:
#     def __init__(self, titular, saldo):
#         self._titular = titular
#         self._saldo = saldo
#         self._ativo = False

#     @property
#     def titular(self):
#         return self._titular

#     @property
#     def titular(self):
#         return self._titular

#     @property
#     def titular(self):
#         return self._titular

# conta4=ContaBancariaPythonica('Josefino',1500.03)
# print(f'Titular da conta 4 é: {conta4.titular}' 
        
# Questão 7
class ClienteBanco:
    def __init__(self,nome,idade,profissao,endereco,telefone):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
        self.endereco = endereco
        self.telefone = telefone

cliente1 = ClienteBanco('Josh', 22, 'Médico', 'Rua Marechal Deodoro, 198', '11 91452-2788')
cliente2 = ClienteBanco('Noah', 19, 'Arquiteto', 'Rua XV de Novembro, 509', '11 95581-6485')
cliente3 = ClienteBanco('Anny', 24, 'Estilista', 'Rua Visconde de Nacar, 4019', '11 95893-0026')

#Questão 8 
@classmethod
def criar_conta(cls,titular,saldo_inicial):
    conta=ClienteBanco(titular,saldo_inicial)
    return conta

conta_cliente1=ClienteBanco.criar_conta('Ton', 455-66)
print (f'{conta_cliente1.titular}.  Com saldo de R${conta_cliente1.saldo_inicial}')
    