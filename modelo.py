#Herança, Polimorfismo e mais
#tarefa _ playlist de programas de TV
#modelo é o nome do doc criado para representar conceitos classes que representam um domínio do sistema

class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title() #protegendo (tornando privado)
        self.ano = ano
        self.duracao = duracao #não protegido
        self.__likes = 0 #Proteger criar problemas para acessar

    @property #usado para criar uma propriedade que retorna um valor privado
    def likes(self):
        return self.__likes
    def dar_like(self): #método para dar likes é um método. Pq ele é incremental
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter #define que um private receba novo valor
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()#padroniza tratamento

class Serie:
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0 #inicializa likes

    @property
    def likes(self):
        return self.__likes

    def dar_like(self): #método para dar likes é um método. Pq ele é incremental
        self.likes += 1

    def dar_like(self):  # método para dar likes é um método. Pq ele é incremental
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_like()

atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_like()
atlanta.dar_like()

print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas} - Likes: {atlanta.likes}')
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duraçao: {vingadores.duracao} - Likes: {vingadores.likes}')
