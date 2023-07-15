class Funcionario:
    def registra_horas(self, horas):
        print('Horas registradas.')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')

class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')

class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')

#tarefa: fazer com que funcionários recebam herança de forma personalizada

class Junior(Alura):
    pass

class Pleno(Alura, Caelum): #gerando herança múltiplas, pontos separados por ',', esse comportamente g
    pass #esse comportamento não existe em outras linguagens
#esse herança múltipla pode gerar conflito para execução de meétodos com nomes iguais, pegando o primeiro
jose = Junior()
jose.busca_perguntas_sem_resposta()

luan = Pleno()
luan.busca_perguntas_sem_resposta()
luan.busca_cursos_do_mes()