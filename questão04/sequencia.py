# 4) Descubra a lógica e complete o próximo elemento:
# a) 1, 3, 5, 7, ___
# b) 2, 4, 8, 16, 32, 64, ____
# c) 0, 1, 4, 9, 16, 25, 36, ____
# d) 4, 16, 36, 64, ____
# e) 1, 1, 2, 3, 5, 8, ____
# f) 2,10, 12, 16, 17, 18, 19, ____


# a) 
def proximo_numero_impar(sequencia):
    return sequencia[-1] + 2

sequencia_a = [1, 3, 5, 7]
proximo_a = proximo_numero_impar(sequencia_a)
print(f"O próximo número na sequência é {proximo_a}.")

# b)

def proxima_potencia_de_2(sequencia):
    return sequencia[-1] * 2

sequencia_b = [2, 4, 8, 16, 32, 64]
proximo_b = proxima_potencia_de_2(sequencia_b)
print(f"O próximo número na sequência é {proximo_b}.")

# c)

def proximo_quadrado_perfeito(sequencia):
    proximo_indice = len(sequencia) + 1
    return (proximo_indice - 1) ** 2

sequencia_c = [0, 1, 4, 9, 16, 25, 36]
proximo_c = proximo_quadrado_perfeito(sequencia_c)
print(f"O próximo número na sequência é {proximo_c}.")

# d) 

def proximo_quadrado_multiplo_de_2(sequencia):
    proximo_indice = len(sequencia) * 2
    return proximo_indice ** 2

sequencia_d = [4, 16, 36, 64]
proximo_d = proximo_quadrado_multiplo_de_2(sequencia_d)
print(f"O próximo número na sequência é {proximo_d}.")

# e) 
def proximo_numero_fibonacci(sequencia):
    return sequencia[-1] + sequencia[-2]

sequencia_e = [1, 1, 2, 3, 5, 8]
proximo_e = proximo_numero_fibonacci(sequencia_e)
print(f"O próximo número na sequência é {proximo_e}.")


# f)

def proximo_numero_na_sequencia(sequencia):
    return sequencia[-1] + 1

sequencia_f = [2, 10, 12, 16, 17, 18, 19]
proximo_f = proximo_numero_na_sequencia(sequencia_f)
print(f"O próximo número na sequência é {proximo_f}.")