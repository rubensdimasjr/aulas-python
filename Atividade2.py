# Atividade 2
# Nome: Rubens Matias
# Matricula: 0013970

# Exercício 1 - Crie uma função que imprima a sequência de números pares entre 1 e 20 (a função não recebe parâmetro) 
# e depois faça uma chamada à função para listar os números
def printSequenceNumbers():
    for i in range(1,21):
        if i % 2 == 0:
            print(i)

print("###############")
print("# Exercício 1:")
printSequenceNumbers()

# Exercício 2 - Crie uam função que receba uma string como argumento e retorne a mesma string em letras maiúsculas.
# Faça uma chamada à função, passando como parâmetro uma string
def upperString(string):
    print(string.upper())

print("###############")
print("# Exercício 2:\n")
upperString('palavra enorme')

# Exercício 3 - Crie uma função que receba como parâmetro uma lista de 4 elementos, adicione 2 elementos a lista e 
# imprima a lista
# print("###############")
