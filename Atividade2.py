# Atividade 2
# Nome: Rubens Matias
# Matricula: 0013970

# Exercício 1 - Crie uma função que imprima a sequência de números pares entre 1 e 20 (a função não recebe parâmetro)
# e depois faça uma chamada à função para listar os números
def printSequenceNumbers():
    for i in range(1, 21):
        if i % 2 == 0:
            print(i)


print("###############")
print("# Exercício 1:")
printSequenceNumbers()

# Exercício 2 - Crie uam função que receba uma string como argumento e retorne a mesma string em letras maiúsculas.
# Faça uma chamada à função, passando como parâmetro uma string


def upperString(string):
    print(string.upper())


print("\n###############")
print("# Exercício 2:")
upperString('palavra enorme')

# Exercício 3 - Crie uma função que receba como parâmetro uma lista de 4 elementos, adicione 2 elementos a lista e imprima a lista


def receiveElementsAndReturn(lista):
    lista.append(5)
    lista.append(6)
    print(lista)


myList = [1, 2, 3, 4]
print("\n###############")
print("# Exercício 3:")
receiveElementsAndReturn(myList)

# Exercício 4 - Crie uma função que receba um argumento formal e uma possível lista de elementos. Faça duas chamadas à função, com apenas 1 elemento e na segunda chamada com 4 elementos


def receivingArgAndList(arg1, *list):
    print("O elemento passado foi: ", arg1)
    for item in list:
        print("O elemento passado foi: ", item)
    return


print("\n###############")
print("# Exercício 4:")
print("\n# Primeira chamada:")
receivingArgAndList("elemento inserido por Rubens")
print("\n# Segunda chamada:")
receivingArgAndList('element1', 'element2', 'element3', 'element4',)

# Exercício 5 - Crie uma função anônima e atribua seu retorno a uma variável chamada soma. A expressão vai receber 2 números como parâmetro e retornar a soma deles


def soma(x, y): return x + y


print("\n###############")
print("# Exercício 5:")
print("A soma de 5 e 6 utilizando a função anônima é:", soma(5, 6))

# Exercício 6 - Execute o código abaixo e certifique-se que compreende a diferença entre variável global e local
total = 0


def soma(arg1, arg2):
    total = arg1 + arg2
    print("Dentro da função o total é: ", total)
    return total


print("\n###############")
print("# Exercício 6:")
soma(10, 20)
print("Fora da função o total é: ", total)

# Exercício 7 - Abaixo você encontra uma lista com temperaturas em graus Celsius
# Crie uma função anônima que converta cada temperatura para Fahrenheit
# Dica: para conseguir realizar este exercício, você deve criar sua função lambda, dentro de uma função
# (que será estudada no próximo capítulo). Isso permite aplicar sua função a cada elemento da lista
# Como descobrir a fórmula matemática que converte de Celsius para Fahrenheit? Pesquise!!!


def convertToFahrenheit(celsius): return (celsius * 9/5) + 32


Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = map(convertToFahrenheit, Celsius)

print("\n###############")
print("# Exercício 7:")
print(list(Fahrenheit))

# Exercício 8 - Crie uma list comprehension que imprima o quadrado dos números de 1 a 10
print("\n###############")
print("# Exercício 8:")
listComprehension = [x**2 for x in range(1, 11)]
print(listComprehension)

# Exercício 9 - Crie uma list comprehension que imprima as palavras com a letra a no nome
palavras = ["maça", "coiote", "banana", "terreno", "Python"]
listComprehensionExerciceNine = [x for x in palavras if "a" in x]
print("\n###############")
print("# Exercício 9:")
print(listComprehensionExerciceNine)

# Exercício 10 - Crie uma list comprehension que imprima os números menores que 5 em um intervalo de 1 a 10
listComprehensionExerciceTen = [x for x in range(1, 11) if x < 5]
print("\n###############")
print("# Exercício 10:")
print(listComprehensionExerciceTen)
