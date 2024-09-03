# Interruptor 1: Controla a lâmpada que está apagada e quente.
# Interruptor 2: Controla a lâmpada que está acesa.
# Interruptor 3: Controla a lâmpada que está apagada e fria.

import time

# Simulação dos estados das lâmpadas
def inicializar_lampadas():
    return [0, 0, 0]  # 0: apagada e fria, 1: acesa, 2: apagada e quente

def ligar_interrupor(lampadas, interrupor):
    if interrupor == 1:
        lampadas[0] = 2  # Lâmpada 1 fica quente
    elif interrupor == 2:
        lampadas[1] = 1  # Lâmpada 2 fica acesa

def desligar_interrupor(lampadas, interrupor):
    if interrupor == 1:
        lampadas[0] = 0  # Lâmpada 1 fica fria

def verificar_lampadas(lampadas):
    resultados = []
    for i, estado in enumerate(lampadas):
        if estado == 1:
            resultados.append(f"Lâmpada {i + 1} está acesa.")
        elif estado == 2:
            resultados.append(f"Lâmpada {i + 1} está apagada e quente.")
        else:
            resultados.append(f"Lâmpada {i + 1} está apagada e fria.")
    return resultados

# Inicializa as lâmpadas
lampadas = inicializar_lampadas()

# Simulação
print("Ligando o Interruptor 1 por 15 minutos...")
ligar_interrupor(lampadas, 1)

# Simula 15 minutos de espera (em prática, é um tempo mais longo)
time.sleep(1)  # Aqui é um segundo para simulação rápida

print("Desligando o Interruptor 1 e ligando o Interruptor 2...")
desligar_interrupor(lampadas, 1)
ligar_interrupor(lampadas, 2)

# Verificação das lâmpadas após a segunda ida
resultado = verificar_lampadas(lampadas)
for res in resultado:
    print(res)


