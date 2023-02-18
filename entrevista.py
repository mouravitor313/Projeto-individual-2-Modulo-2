# Criado por: Vítor
# Inicialmente não alterado (18/02/2023)

import csv # import da biblioteca que irá editar um arquivo csv
class Entrevista: # criação da classe Entrevista
    


    entrevistado = 'user' # variavel designada para colocar o nome do entrevistado para usar com o get e set


    def __init__(self, idade, gen, r1, r2, r3, r4, data, hora): # construtor para iniciar as variaveis
        self.idade = idade # variavel designada para a idade
        self.gen = gen # variavel designada para o genero
        self.r1 = r1 # variavel designada para a primeira resposta
        self.r2 = r2 # variavel designada para a segunda resposta
        self.r3 = r3 # variavel designada para a terceira resposta
        self.r4 = r4 # variavel designada para a quarta resposta
        self.data = data # variavel designada para a data
        self.hora = hora # variavel designada para a hora

    def Entrevistado (self):
        while (self.idade != '00'):
            self.idade = input ('Insira a idade do entrevistado: ')
            self.gen = input ('Insira o gênero do entrevistado: ')
            self.r1 = input ('Insira a primeira resposta do entrevistado: ')
            self.r2 = input ('Insira a segunda resposta do entrevistado: ')
            self.r3 = input ('Insira a terceira resposta do entrevistado: ')
            self.r4 = input ('Insira a quarta resposta do entrevistado: ')
            self.data = input ('Insira a data da entrevista: ')
            self.hora = input ('Insira a hora da entrevista: ')

    def get_usuario(self):
        return self.entrevistado

    def set_usuario(self, new_user):
        self.nome = new_user   

    def exportar_dados(self):
        with open ('saida_entrevista.csv', 'w', newline = '') as saida:
            cabecalho = ['entrevistado', 'idade', 'genêro', 'r1', 'r2', 'r3', 'r4', 'data', 'hora']
            writer = csv.DictWriter(saida, fieldnames = cabecalho)

            for linha in writer:
                writer.writeheader()
                writer.writerow({'entrevistado':self.entrevistado, 'idade':self.idade, 'genêro':self.gen, 'r1':self.r1, 'r2':self.r2, 'r3':self.r3, 'r4':self.r4, 'data':self.data, 'hora':self.hora})
        
