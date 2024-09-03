# 2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, 
# além de informar a quantidade de vezes em que ela ocorre;


def contar_letra_a(texto):
    return texto.lower().count('a')


# TESTANDO O CÓDIGO:

texto = input("Digite uma palavra que contenha a letra 'a': ")
quantidade = contar_letra_a(texto)
print(f"a letra 'a' ocorre {quantidade} vezes na palavra")

