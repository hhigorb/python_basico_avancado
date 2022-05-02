"""
Escopo de variáveis

Dois casos de escopo:

1 - Variáveis globais:
    - Variáveis globais são reconhecidas, ou seja, seu escopo compreende o programa inteiro.

2 - Variáveis locais:
    - Variáveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo
    está limitado ao bloco onde foi declarada.

Python é uma linguagem de tipagem dinâmica, isso significa que ao declararmos uma variável, nós não colocamos
o tipo de dado dela. Este tipo é inferido ao atribuirmos o valor à mesma.

"""

numero = 42  # Exemplo de variável global
print(numero)
print(type(numero))

if numero > 10:
    novo = numero + 10  # A variável 'novo' está declarada localmente dentro do bloco if. Portanto, é local.
    print(novo)

print(novo)
