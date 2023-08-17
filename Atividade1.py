# Atividade 1
# Nome: Rubens Matias
# Matricula: 0013970

# Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números.
numbersExerciseOne = [1,2,3,4,5,6,7,8,9,10]
print("# Exercício 1:",numbersExerciseOne)

# Exercício 2 - Crie uma lista de 5 objetos e imprima na tela
listFiveObjects = [
    'jesus',
    'maria',
    'jose',
    'rodolfo',
    'rubens'
]
print("# Exercício 2:",listFiveObjects)

# Exercício 3 - Crie duas strings e concatene as duas em uma terceira string
firsString = 'Rubens'
secondString = 'Matias'
concatString = firsString + ' ' + secondString
print("# Exercício 3:",concatString)

# Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função count do 
# objeto tupla para verificar quantas vezes o número 4 aparece na tupla
tuplaExerciseFour = (1, 2, 2, 3, 4, 4, 4, 5)
print("# Exercício 4:", tuplaExerciseFour.count(4))

# Exercício 5 - Crie um dicionário vazio e imprima na tela
dictionaryExerciseFive = {}
print("# Exercício 5:",dictionaryExerciseFive)

# Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela
dictionaryExerciseSix = {"Rubens":23,"Gilmar":35,"Henrique":22}
print("# Exercício 6:",dictionaryExerciseSix)

# Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela
dictionaryExerciseSix['Maria'] = 43
print("# Exercício 7:", dictionaryExerciseSix)

# Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. 
# Um dos valores deve ser uma lista de 2 elementos numéricos. 
# Imprima o dicionário na tela.
dictionaryExerciseEight = {
    "Rubens": ['dev',23],
    "Gilmar":35,
    "Henrique":22
}
print("# Exercício 8:",dictionaryExerciseEight)

# Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string, 
# o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e 
# o quarto elemento um valor do tipo float.
# Imprima a lista.
listExerciseNine = [
    'requeredString',
    ("element1", "element2"),
    {"key1":1,"key2":2},
    3.50
]
print("# Exercício 9",listExerciseNine)

# Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.
frase = 'Cientista de Dados é o profissional mais top do século XXI'
print("# Exercício 10:",frase[:18])
