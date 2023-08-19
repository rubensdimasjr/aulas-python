# Exercício 1 - Crie uma estrutura que pergunte ao usuário qual o dia da semana. Se o dia for igual a Domingo ou
# igual a sábado, imprima na tela "Hoje é dia de descanso", caso contrário imprima na tela "Você precisa trabalhar!"
diaDaSemana = input("\nExercício 1 - Que dia da semana é hoje?: ")
if (diaDaSemana == "domingo" or diaDaSemana == "sábado" or diaDaSemana == "sabado"):
    print("Hoje é dia de descanso")
else:
    print("Você precisa trabalhar!")

# Exercício 2 - Crie uma lista de 5 frutas e verifique se a fruta 'Morango' faz parte da lista
frutas = ['Maçã', 'Banana', 'Laranja', 'Pera', 'Uva']
if 'Morango' in frutas:
    print('\nExercício 2 - Sim, Morango faz parte da lista de frutas.')
else:
    print('\nExercício 2 - Não, Morango não faz parte da lista de frutas.')

# Exercício 3 - Crie uma tupla de 4 elementos, multiplique cada elemento da tupla por 2 e guarde os resultados em uma
# lista
tuple = (2, 4, 6, 8)
emptyList = []
for i in tuple:
    element = i * 2
    emptyList.append(element)
print("\nExercício 3 -", emptyList)

# Exercício 4 - Crie uma sequência de números pares entre 100 e 150 e imprima na tela
listForNumbersExerciseFour = []
for num in range(100, 151):
    if num % 2 == 0:
        listForNumbersExerciseFour.append(num)
print("\nExercício 4 -", listForNumbersExerciseFour)

# Exercício 5 - Crie uma variável chamada temperatura e atribua o valor 40. Enquanto temperatura for maior que 35,
# imprima as temperaturas na tela
print("\nExercício 5:")
temperatura = 40
while (temperatura > 35):
    temperatura = temperatura - 1
    print(temperatura)

# Exercício 6 - Crie uma variável chamada contador = 0. Enquanto counter for menor que 100, imprima os valores na tela,
# mas quando for encontrado o valor 23, interrompa a execução do programa
print("\nExercício 6:")
contador = 0
while (contador < 100):
    if (contador == 23):
        print("Encontrado o valor 23. O programa será interrompido.")
        break
    print(contador)
    contador = contador + 1

# Exercício 7 - Crie uma lista vazia e uma variável com valor 4. Enquanto o valor da variável for menor ou igual a 20,
# adicione à lista, apenas os valores pares e imprima a lista
listForExerciseSeven = []
value = 4
while (value <= 20):
    if value % 2 == 0:
        listForExerciseSeven.append(value)
    value = value + 1

print("\nExercício 7 -", listForExerciseSeven)

# Exercício 8 - Transforme o resultado desta função range em uma lista: range(5, 45, 2)
listaForExerciseEight = []
for i in range(5, 45, 2):
    listaForExerciseEight.append(i)
print("\nExercício 8 -", listaForExerciseEight)

# Exercício 9 - Faça a correção dos erros no código abaixo e execute o programa. Dica: são 3 erros.
temperatura = float(input('\nExercício 9 - Qual a temperatura? '))
if temperatura > 30:
    print('Vista roupas leves.')
else:
    print('Busque seus casacos.')

# Exercício 10 - Faça um programa que conte quantas vezes a letra "r" aparece na frase abaixo. Use um placeholder na
# sua instrução de impressão

# “A gratidão é a virtude das almas nobres. O quão feliz é uma pessoa depende da profundidade de sua gratidão.”
frase = "A gratidão é a virtude das almas nobres. O quão feliz é uma pessoa depende da profundidade de sua gratidão."
contador = 0
for letra in frase:
    if letra == 'r':
        contador = contador + 1

print(f"\nExercício 10 - Há {contador} r's nessa frase.")
