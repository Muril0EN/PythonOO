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

    def __str__(self): #método especial que retorna dado como string
        return f'({self._nome}) - ({self.ano}) - ({self._likes}) likes'

class Filme(Programa): #a classe mãe vai entre parênteses
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)#chamando inicializar da classe mãe. Assim, o objeto recebe instância craida pela classe mãe
        self.duracao = duracao  # não protegido

    def __str__(self):
        return f'({self.nome}) - ({self.duracao}) - ({self._likes})'
class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'({self.nome}) - ({self.temporadas}) - ({self.likes})'

vingadores = Filme('vingadores', 2018, 160)
vingadores.dar_like()

atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_like()
atlanta.dar_like()

#Polimorfismo ->
filmes_e_series = [vingadores, atlanta] #criar lista

for programa in filmes_e_series: #a definição do método 'imprime' na superclasse exclui a necessidade de fazer
    # 'if' pra descobrir "detalhes" de cada classe filho
    print(programa) #se definido __str__ na classe o programa "acha" e imprime a string.
