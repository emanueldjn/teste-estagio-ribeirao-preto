# 1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
## escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.


def pertence_fibonacci(numero):
    if numero < 0:
        return False
    a, b = 0, 1
    while a < numero:
        a, b = b, a + b
        return a == numero 
    
# print(pertence_fibonacci(13))  True
# print(pertence_fibonacci(14))   False

# TESTANDO O CÓDIGO:

numero = int(input("Digite um número: "))
if pertence_fibonacci(numero):
    print(f"O número {numero} pertence a sequência de fibonacci.")
else: 
    print(f"O número {numero} não pertence a sequência de fibonacci.")  
    
