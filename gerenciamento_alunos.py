alunos =[]


#Variavel utilizada na função adicionar_aluno a fim de assegurar que nomes iguais não sejam inseridos na listagem
nomes_unicos = set()

#Utilizado função lambda a fim de calcular a média da soma das 5 notas dos alunos
media = lambda soma: soma / 5


#Função para adicionar alunos. Solicitando nome e 5 notas do aluno e armazenando em um dicionário.
def adicionar_aluno():
       
        nome_aluno = input('Digite o nome do aluno: ').capitalize()
        if nome_aluno.isalpha():
            if nome_aluno in nomes_unicos:
                print('Este nome já foi adicionado.')
                return
        else:
            print('Nome deve conter somente letras')   
            
        try:        
            nota_aluno = [float(input(f'Digite a nota {i+1} do aluno:')) for i in range(5)]
            alunos.append({'Nome do Aluno':nome_aluno, 'Notas Aluno':nota_aluno})
            nomes_unicos.add(nome_aluno)
        except ValueError:
            print('As notas não devem conter letras')

      

#Exibe nome dos alunos e medias.
def exibir_alunos():
    
    for indice, aluno in enumerate(alunos):

        soma = sum(aluno['Notas Aluno'])
        media_aluno = media(soma)

        print(f'{indice}) Nome Aluno: {aluno['Nome do Aluno']} | Média Aluno:{media_aluno}')
        
#Pesquisa através do nome do aluno, exibindo nome e média.
def pesquisar_aluno():
    try:
    
        pesquisa_aluno = input('Digite o nome do aluno')
        aluno_encontrado = False
        for aluno in alunos:
            if aluno['Nome do Aluno'] == pesquisa_aluno:
                aluno_encontrado = True
                soma = sum(aluno['Notas Aluno'])
                media_aluno = media(soma)
                print(f'Nome Aluno: {aluno['Nome do Aluno']} | Média Aluno:{media_aluno}')
        if not aluno_encontrado:
            raise ValueError('Aluno Inexistente')
    except ValueError as e:
        print(e)
            

#Possível alterar a nota solicitando o nome do aluno. A nota é selecionada através do seu indice
def atualizar_notas():
    try:
        soma = 0
        pesquisa_aluno = input('Digite o nome do aluno')
        aluno_encontrado = False
        for aluno in alunos:
            if aluno['Nome do Aluno'] == pesquisa_aluno:
                aluno_encontrado = True
                print(aluno['Notas Aluno'])
                for indice, nota_teste in enumerate(aluno['Notas Aluno']):
                    print(f'{indice})Nota:{nota_teste}')

                indice_nota = int(input('Digite o indice da nota que deseja alterar')) 
                print(aluno['Notas Aluno'])
                for indice, nota in enumerate(aluno['Notas Aluno']):
                    if indice_nota == indice:
                            aluno['Notas Aluno'][indice] = float(input('Digite a nova nota'))
               

        if not aluno_encontrado:
            raise ValueError('Aluno Inexistente')
    except ValueError as e:
        print(e)
   
#Remove aluno solicitando seu nome.
def remover_aluno():
    exibir_alunos()
    nome_aluno = input('Digite o nome do aluno que deseja remover: ')
    for aluno in alunos:
        print(aluno)
        if nome_aluno == aluno['Nome do Aluno']:
            alunos.remove(aluno)


#Exibe aluno e media dos alunos que tiraram 7 ou mais   
def exibir_aprovados():

 
    for aluno in alunos:
        soma = sum(aluno['Nota Aluno'])
        media_aluno = media(soma)
        if media_aluno >= 7:
            print(f'Nome Aluno: {aluno['Nome do Aluno']} | Média Aluno:{media_aluno}')
    

#Menu de opções
while True:
        print('[0]Inserir Aluno\n[1]Listar Alunos\n[2]Pesquisar Aluno\
\n[3]Atualizar Notas\n[4]Remover Aluno\n[5]Exibir Aprovados\n[6]Sair')
        opc = int(input('Digite a opção desejada: \n'))
   
        match opc:
                case 0:
                    adicionar_aluno()
            
                case 1:
                    exibir_alunos()

                case 2:
                    pesquisar_aluno()
                
                case 3:
                    atualizar_notas()

                case 4:
                    remover_aluno()

                case 5: 
                    exibir_aprovados()

                case 6:
                    break        
