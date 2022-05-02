"""
Listas Aninhadas

- Algumas linguagens de programação (C/Java) possuem estruturas de dados chamadas de arrays
    - Unidimensionais (Arrays/Vetores)
    - Multidimensionais (Matrizes)

Em Python nós temos as listas

valores = [1, 2, 3, 3.24, True]

Exemplos:

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matriz 3 x 3
print(listas)
print(type(listas))

# Como fazemos para acessar os dados?

print(listas[0][1])
print(listas[2][1])

# Iterando com loops em uma lista aninhada:
for lista in listas:
    for numero in lista:
        print(numero)

# List Comprehension:

[[print(valor) for valor in lista] for lista in listas]
"""














