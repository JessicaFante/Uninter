#Exercício - Um aluno, para passar de ano, precisa ser aprovado em todas as matérias que está cursando. Assuma que a
#média para aprovação é a partir de 7, e que o aluno cursa 3 matérias, somente. Escreva um algoritmo que leia a nota
#final do aluno em cada matéria, e informe na tela, se ele passou ou não.

media = 7
m1 = float(input('Digite a nota da 1° matéria:'))
m2 = float(input('Digite a nota da 2° matéria:'))
m3 = float(input('Digite a nota da 3° matéria:'))
if m1 >= media and m2 >= media and m3 >= media:
    print('O aluno está aprovado de ano!')
else:
    print('O aluno está reprovado de ano!')
