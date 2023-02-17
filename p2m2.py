# 1 - While pedindo para a pessoa inclua uma vaga e um resumo
# 2 - é pra checar na minibio se há as palavras chaves necessarias para ser um candidato válido
# 3 - encerrar o codigo com 0
# 4 - usar dicionario para colocar a quantidade de curriculos e quantas pessoas tem as palavras chaves
# 5 - vaga 1: Python, Programação, Desenvolvimento
# 6 - vaga 2: Análise de dados, Dados, SQL


contV1 = 0
contI1 = 0
contV2 = 0
contI2 = 0

qntd_cndts1 = {'vaga': '1', 'válidos':0, 'inválidos':0}
qntd_cndts2 = {'vaga': '2', 'válidos':0, 'inválidos':0}
qntd_curriculum1 = {'curriculos vaga 1':0}
qntd_curriculum2 = {'curriculos vaga 2':0}

dicionario1 = {}
dicionario2 = {}


while(True):

    menu = input('Deseja adicionar alguém ao sistema ou fazer uma pesquisa no banco de dados? (1 para adicionar, 2 para pesquisar, 3 para consultar o banco de dados e 0 para sair)\n').upper()
    print('\n')
    
    if menu == '1':
        while(vagas != '0'):
            vagas = input('Adicionar para qual vaga? [1/2] (0 para voltar)\n')

            if vagas == '1':
                candidato1 = input('Nome do candidato:\n').upper()
                print ('')
                resumo1 = input('Digite o resumo:\n').lower()
                dicionario1 = {candidato1: resumo1}

            elif vagas == '2':
                candidato2 = input('Nome do candidato:\n').upper()
                print ('')
                resumo2 = input('Digite o resumo:\n').lower()
                dicionario2 = {candidato2: resumo2}

            elif vagas == '0':
                break

            else:
                print('Escolha inválida!')

        print ('')


    elif menu == '2':

        while(esc != '0'):
            esc = input('Pesquisar candidatos na Vaga 1 ou Vaga 2: [1/2] (0 para voltar)\n')
            print ('')

            if esc == '1':
                if 'python' in dicionario1[candidato1] and 'programação' in dicionario1[candidato1] and 'desenvolvimento' in dicionario1[candidato1]:
                    print('O candidato é válido')
                    qntd_cndts1['válidos'] = + 1
                    qntd_curriculum1['curriculos vaga 1'] = + 1
                else:
                    print('O candidato não é válido')
                    qntd_cndts1['inválidos'] = + 1
                    qntd_curriculum1['curriculos vaga 1'] = + 1

            elif esc == '2':
                if 'análise de dados' in dicionario2[candidato2] and 'dados' in dicionario2[candidato2] and 'sql' in dicionario2[candidato2]:
                    print('O candidato é válido')
                    qntd_cndts2['válidos'] = +1
                    qntd_curriculum2['curriculos vaga 2'] = + 1
                else:
                    qntd_cndts2['inválidos'] = +1
                    print('O candidato não é válido')
                    qntd_curriculum2['curriculos vaga 2'] = + 1
            
            elif esc == '0':
                break

            else:
                print('Escolha inválida!')

    elif menu == '3':
        while(voltar != 'S'):
            print ('Candidatos:')
            print (f'Candidatos vaga 1: {dicionario1}')
            print (f'Candidatos vaga 2: {dicionario2}')
            print ('')

            print ('Quantidade de candidatos válidos e inválidos: ')
            print (f'Quantidade de candidatos vaga 1: {qntd_cndts1}')
            print (f'Quantidade de candidatos vaga 2: {qntd_cndts2}')
            print ('')

            print ('Quantidade de curruculos em cada vaga: ')
            print (f'Quantidade de curriculos vaga 1: {qntd_curriculum1}')
            print (f'Quantidade de curriculos vaga 2: {qntd_curriculum2}')
            print ('')
            voltar = input('Deseja voltar ao menu anterior?[S/N]\n').upper()
            print('')
            if voltar == 'S':
                break

    elif menu == '0':
        break

    else:
        print('Escolha inválida!')
