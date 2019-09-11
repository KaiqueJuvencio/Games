import random
import os

#==================== NOMES ===================

# Kalvin Vasconscelos: 31894666
# Kaique Costa: 31844812

#===============================================






matriz = []
size = 10
flag = True
tentativa = 20
cls = "\n"*50
vencimento = 0
vetor_ver = []

#================================  Variáveis CRUZADOR =======================================
cruzador_x = random.randint(0, 9)
cruzador_y = random.randint(0, 9)
dadobinario = random.randint(1, 2)
cruzador_horizontal = random.randint(0, 1)
cruzador_vertical = random.randint(0, 1)

if cruzador_horizontal == 1 and cruzador_vertical == 1:
    cruzador_vertical = 0
if cruzador_horizontal == 0 and cruzador_vertical == 0:
    cruzador_horizontal = 0
    cruzador_vertical = 1
#=============================================================================================



#================================  Variáveis SUBMARINO =======================================
submarino_x = random.randint(0, 9)
submarino_y = random.randint(0, 9)
submarino_horizontal = random.randint(0, 1)
submarino_vertical = random.randint(0, 1)

if submarino_horizontal == 1 and submarino_vertical == 1:
    submarino_vertical = 0
if submarino_horizontal == 0 and submarino_vertical == 0:
    submarino_horizontal = 0
    submarino_vertical = 1
#==============================================================================================


#================================  Variáveis ENCOURAÇADO =======================================
encouracado_x = random.randint(0, 9)
encouracado_y = random.randint(0, 9)
encouracado_horizontal = random.randint(0, 1)
encouracado_vertical = random.randint(0, 1)

if encouracado_horizontal == 1 and encouracado_vertical == 1:
    encouracado_vertical = 0
if encouracado_horizontal == 0 and encouracado_vertical == 0:
    encouracado_horizontal = 0
    encouracado_vertical = 1
#==============================================================================================


#================================  Variáveis PORTA-AVIÃO =======================================
porta_x = random.randint(0, 9)
porta_y = random.randint(0, 9)
porta_horizontal = random.randint(0, 1)
porta_vertical = random.randint(0, 1)

if porta_horizontal == 1 and porta_vertical == 1:
    porta_vertical = 0
if porta_horizontal == 0 and porta_vertical == 0:
    porta_horizontal = 0
    porta_vertical = 1
#==============================================================================================






def tabuleiro():
    num = 0
    for i in range(size):
        linha = []
        for j in range(size):
            linha.append(".")
        matriz.append(linha)
    print("                                                           _    _    _    _    _    _    _    _    _    _")
    print("                                                           0    1    2    3    4    5    6    7    8    9")
    print("                                                           -    -    -    -    -    -    -    -    -    -")
    for k in range(size):
        print("                                                   |",num,"|", end ='   ')
        num+=1
        for l in range(size):
            print(matriz[k][l], end='    ')
        print("\n")


#=============================== Validação para não sair do tabuleiro =====================
while cruzador_x + 3 > 9 or cruzador_y + 3 > 9:
    cruzador_x = random.randint(0, 9)
    cruzador_y = random.randint(0, 9)

while submarino_x + 2 > 9 or submarino_y + 2 > 9:
    submarino_x = random.randint(0, 9)
    submarino_y = random.randint(0, 9)

while encouracado_x + 4 > 9 or encouracado_y + 4 > 9:
    encouracado_x = random.randint(0, 9)
    encouracado_y = random.randint(0, 9)

while porta_x + 5 > 9 or porta_y + 5 > 9:
    porta_x = random.randint(0, 9)
    porta_y = random.randint(0, 9)
#===========================================================================================




while flag == True:

    erro = True
    print("                                              ______       _        _ _             _   _                  _                       _   ")
    print("                                              | ___ \     | |      | | |           | \ | |                | |                  _~ )_)_~")
    print("                                              | |_/ / __ _| |_ __ _| | |__   __ _  |  \| | __ ___   ____ _| |                 )_))_))_)  ")
    print("                                              | ___ \/ _` | __/ _` | | '_ \ / _` | | . ` |/ _` \ \ / / _` | |                 _!__!__!_      ")
    print("                                              | |_/ / (_| | || (_| | | | | | (_| | | |\  | (_| |\ V / (_| | |                 \______t/      ")
    print("                                              \____/ \__,_|\__\__,_|_|_| |_|\__,_| \_| \_/\__,_| \_/ \__,_|_|               ~~~~~~~~~~~~~       ")
    print(" ")
    print("Tentativas: ", tentativa)
    print("Acertos: ",vencimento)
    tabuleiro()
    if vencimento == 14:
        print("============ PARABÉNS, VOCÊ VENCEU =============")
        break
    if tentativa == 0:
        print("============ TENTATIVAS ESGOTADAS =============")
        break
    print("C = Acertou um Cruzador.")
    print("S = Acertou um Submarino.")
    print("E = Acertou um Encouraçado.")
    print("P = Acertou um Porta-Avião.")
    print("x = Acertou nada.\n\n")
    x = int(input("Digite o X: "))
    y = int(input("Digite o Y: "))
    tentativa-=1




# ================================  Criação CRUZADOR =======================================

    soma_cruz_x = 0
    soma_cruz_y = 0


    if cruzador_horizontal == 1:
        for cruzx in range(3):
            if x == cruzador_x + soma_cruz_x and y == cruzador_y:
                matriz[x][y] = "C"
                vencimento += 1
                erro = False
            soma_cruz_x += 1

    if cruzador_vertical == 1:
        for cruzy in range(3):
            if x == cruzador_x and y == cruzador_y + soma_cruz_y:
                matriz[x][y] = "C"
                vencimento += 1
                erro = False
            soma_cruz_y +=1

#============================================================================================



# ================================  Criação SUBMARINO =======================================

    soma_sub_x = 0
    soma_sub_y = 0



    if submarino_horizontal == 1:
        for subx in range(2):
            if x == submarino_x + soma_sub_x and y == submarino_y:
                matriz[x][y] = "S"
                vencimento += 1
                erro = False
            soma_sub_x += 1

    if submarino_vertical == 1:
        for suby in range(2):
            if x == submarino_x and y == submarino_y + soma_sub_y:
                matriz[x][y] = "S"
                vencimento += 1
                erro = False
            soma_sub_y += 1

#============================================================================================



# ================================  Criação ENCOURAÇADO =======================================

    soma_enc_x = 0
    soma_enc_y = 0



    if encouracado_horizontal == 1:
        for encx in range(4):
            if x == encouracado_x + soma_enc_x and y == encouracado_y:
                matriz[x][y] = "E"
                vencimento += 1
                erro = False
            soma_enc_x += 1

    if encouracado_vertical == 1:
        for ency in range(4):
            if x == encouracado_x and y == encouracado_y + soma_enc_y:
                matriz[x][y] = "E"
                vencimento += 1
                erro = False
            soma_enc_y += 1

#============================================================================================


# ================================  Criação PORTA-AVIÃO =======================================

    soma_porta_x = 0
    soma_porta_y = 0



    if porta_horizontal == 1:
        for portax in range(5):
            if x == porta_x + soma_porta_x and y == porta_y:
                matriz[x][y] = "P"
                vencimento += 1
                erro = False
            soma_porta_x += 1

    if porta_vertical == 1:
        for portay in range(5):
            if x == porta_x and y == porta_y + soma_porta_y:
                matriz[x][y] = "P"
                vencimento += 1
                erro = False
            soma_porta_y += 1

#============================================================================================
    if erro == True:
        matriz[x][y] = "x"

    print(cls)








