#Dada uma lista contendo as notas de alunos em uma disciplina, escreva uma expressão para:

notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]

#a) Encontrar quantos alunos tiraram nota 7
print(notas.count(7))

#b) Alterar a última nota para 4
notas[-1] = 4
print(notas)

#c) Encontrar a maior nota
maior = max(notas)
print(maior)

#d) Ordenar a lista de notas
notas.sort()
print(notas)

#e) A média das notas
media = sum(notas)/len(notas)
print(media)