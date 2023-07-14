#Herança, Polimorfismo e mais
#tarefa _ playlist de programas de TV
#modelo é o nome do doc criado para representar conceitos classes que representam um domínio do sistema
class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()  # classes mãe devem receber apenas '1 _' p/ tornando privado
        self.ano = ano
        self._likes = 0

    @property  # usado para criar uma propriedade que retorna um valor privado
    def likes(self):
        return self._likes

    def dar_like(self):  # método para dar likes é um método. Pq ele é incremental
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter  # define que um private receba novo valor
    def nome(self, novo_nome):
        self._nome = novo_nome.title()  # padroniza tratamento


class Filme(Programa): #a classe mãe vai entre parênteses
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)#chamando inicializar da classe mãe. Assim, o objeto recebe instância craida pela classe mãe
        self.duracao = duracao  # não protegido

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_like()

atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_like()
atlanta.dar_like()

print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas} - Likes: {atlanta.likes}')
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duraçao: {vingadores.duracao} - Likes: {vingadores.likes}')
