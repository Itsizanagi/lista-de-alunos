import random

aluno1 = input(('Primeiro aluno: '))
aluno2 = input(('Segundo aluno: '))
aluno3 = input(('Terceiro aluno: '))
aluno4 = input(('Quarto aluno: '))

lista_alunos = [aluno1, aluno2, aluno3, aluno4]

aluno_escolhido = random.choice(lista_alunos)


print('Dentre os alunos: \n {} \n {} \n {} \n {} \n o escolhio foi: \n {}' .format(aluno1, aluno2, aluno3, aluno4, aluno_escolhido))

