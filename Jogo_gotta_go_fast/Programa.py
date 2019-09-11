#================================================
#Kaique Juvencio Costa -- 31844812
#Roger Thecera Rojas -- 31849571
#================================================
#inicia o jogo#
import pygame
import random
pygame.init()
import os
import time
#audio_game = pygame.mixer.Sound('gamesong.ogg')
audio_menu = pygame.mixer.Sound('menusong.ogg')
def inicio():
    import pygame
    import os
    pygame.init()
    audio_menu.stop()
    #audio_game.stop()
    audio_menu.play()
    folder = "img"
    image = pygame.image.load(os.path.join(folder,"menuphoto3.png"))
    #===============cores para poder usar==========#
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    ORANGE = (255, 165, 0)
    CINZA = (40,40,40)
    CINZA_CLARO = (100,100,100)

    # ==============fontes para poder usar===========#
    fonte1 = pygame.font.SysFont('Impact', 60)
    fonte2 = pygame.font.SysFont('Arial', 20)
    fonte3 = pygame.font.SysFont('Poor Richard', 30)
    fonte4 = pygame.font.SysFont('BroshK', 30)
    fonte42 = pygame.font.SysFont('BroshK', 80)

    #============== criando a tela===================#
    screen = pygame.display.set_mode((1200, 600))
    screen.fill((BLACK))
    pygame.display.flip()

    # fazendo o texto#
    titulo = fonte42.render('', True, (ORANGE))
    exit = fonte2.render('', True, (ORANGE))
    jogar = fonte4.render('', True, (ORANGE))
    instru = fonte4.render('', True, (ORANGE))
    creditos = fonte4.render('', True, (ORANGE))
    # colocando o texto na tela#

    screen.blit(image,(1,1))




    screen.blit(titulo,[430, 100])
    screen.blit(exit, [10, 570])
    screen.blit(jogar, [500, 250])
    screen.blit(instru, [500, 300])
    screen.blit(creditos, [800, 700])
    pygame.display.update()
    pygame.display.flip()

    #chamando a função Buttons#
    buttons()






#tela de instruções do jogo#
def instru():
    import pygame
    screen = pygame.display.set_mode((1200, 600))
    BLACK = (0, 0, 0)
    ORANGE = (255, 165, 0)
    fonte3 = pygame.font.SysFont('Poor Richard', 30)
    fonte2 = pygame.font.SysFont('Arial', 20)
    screen.fill((246,246,246))
    folder = "img"
    image = pygame.image.load(os.path.join(folder, "instru2.png"))
    screen.blit(image, (0, 0))



    pygame.display.flip()
    fechar_sair()

#tela de créditos#
def creditos():
    import pygame
    W, H = 1000, 750
    HW, HH = W / 2, H / 2
    AREA = W * H

    os.environ['SDL_VIDEO_WINDOW_POS'] = "100,100"

    # setup pygame
    pygame.init()
    CLOCK = pygame.time.Clock()
    DS = pygame.display.set_mode((W, H))
    pygame.display.set_caption("code.Pylet - Scrolling Background Image")
    FPS = 300

    bkgd = pygame.image.load("creditosphoto3.png").convert()

    y = 500
    velocidade_pista = 0.2
    pygame.display.update()
    while True:
        # Faz a pista rodar
        rel_y = y % bkgd.get_rect().height
        DS.blit(bkgd, (0, rel_y - bkgd.get_rect().height))
        if rel_y < H:
            DS.blit(bkgd, (0, rel_y))

        # Velocidade da pista
        y -= velocidade_pista

        # Faz sair de dentro da tela do jogo
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                inicio()




        pygame.display.update()

    pygame.display.flip()
    fechar_sair()


#função que captura os clicks do mouse#
def buttons():
    import pygame
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            # calculando posição do mouse#
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                # clicando nos créditos
                for i in range(470, 710):
                    for j in range(485,580 ):
                        if i == x and j == y:
                            creditos()
                for a in range (470,710):
                    for b in range (385,480):
                        if a==x and b==y:
                            instru()
                for c in range (470,710):
                    for d in range(250,380):
                        if c==x and d==y:
                            jogar()


#função para sair do jogo ou voltar para tela#
def fechar_sair():
    import pygame
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                inicio()
                pygame.display.flip()
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
#o jogo em sí#
#======================Cores=======================
white = (255,255,255)
blue = (108,194,236)
green = (152,231,114)
pink = (253,147,223)
#======================Objetos=====================

def jogo():
    audio_menu.stop()

    #audio_game.play()


    W, H = 1000, 750
    HW, HH = W / 2, H / 2
    AREA = W * H

    os.environ['SDL_VIDEO_WINDOW_POS'] = "100,100"

    # setup pygame
    pygame.init()
    CLOCK = pygame.time.Clock()
    DS = pygame.display.set_mode((W, H))
    pygame.display.set_caption("code.Pylet - Scrolling Background Image")
    FPS = 300

    bkgd = pygame.image.load("backgaming9.png").convert()
    y = 0

    # main loop
    folder = "img"
    #coloca personagem
    x = 600
    y = 500
    x_carro = 475
    y_carro = 650

    x_ret = 475
    y_ret = 500
    #inimigos
    x_inimigo1 =475
    y_inimigo1 =random.randint(-300,0)
    h_inimigo1 = 70
    h_inimigo2 = 70
    h_inimigo3 = 70
    w_inimigo1 = 50
    w_inimigo2 = 50
    w_inimigo3 = 50
    x_inimigo2 = 250
    y_inimigo2 = random.randint(-800,-600)
    x_inimigo3 =700
    y_inimigo3 =random.randint(-600,-300)

    flag =True
    chamado = random.randint(0,5)
    dado = random.randint(1, 3)

    ret = pygame.Rect(x_ret, y_ret, 30, 30)
    ret_inimigo1 = pygame.Rect(x_inimigo1,y_inimigo1,50,70)

    image = pygame.image.load(os.path.join("carrovermelho70x904.png"))
    image2 = pygame.image.load(os.path.join("carsprite_verde2.png"))
    image3 = pygame.image.load(os.path.join("carsprite_ama2.png"))
    image6 = pygame.image.load(os.path.join("carsprite_cinza.png"))
    vida = pygame.image.load(os.path.join("vida3.png"))
    vida2 = pygame.image.load(os.path.join("vida3.png"))
    vida3 = pygame.image.load(os.path.join("vida3.png"))
    x_vida = 5
    y_vida = 75
    x_vida2 = 50
    y_vida2 = 75
    x_vida3 = 95
    y_vida3 = 75

    jogar_dnovo = pygame.image.load(os.path.join("jogar_novamente4.png"))

    audio = pygame.mixer.Sound('batida2.ogg')
    

    cont_vida = 3

    BLACK = (0, 0, 0)
    ORANGE = (255, 165, 0)
    fonte4 = pygame.font.SysFont('BroshK', 30)
    score = 0

    velocidade_pista = 0.7

    lvl1 = True
    lvl2 = False
    lvl3 = False
    lvl4 = False
    lvl5 = False
    lvl6 = False

    inimigo1 = pygame.Rect(x_inimigo1, y_inimigo1, 50, 70)

    pygame.display.update()

    while True:

        score +=1




        #Spawn dos inimigos
        chamado = random.randint(4, 5)
        if y_inimigo1 > 700:
            if chamado == 5:
                dado = random.randint(1, 3)
                y_inimigo1 = random.randint(-200, -100)

        if y_inimigo2 > 700:
            if chamado == 5:
                dado = random.randint(1, 3)
                y_inimigo2 = random.randint(-200, -100)

        if y_inimigo3 > 700:
            if chamado == 5:
                dado = random.randint(1, 3)
                y_inimigo3 = random.randint(-200, -100)








        #Velocidade da pista
        y += velocidade_pista

        # velocidade dos inimigos
        if lvl1 == True:
            if dado ==1:
                y_inimigo1 += 1

            if dado == 2:
                y_inimigo2 +=1

            if dado == 3:
                y_inimigo3 +=1



            if score>5000:
                lvl1 = False
                lvl2 = True
                velocidade_pista = 1


        if lvl2 == True:
            if dado == 1:
                y_inimigo1 += 2

            if dado == 2:
                y_inimigo2 += 2


            if dado == 3:
                y_inimigo3 += 2


            if score>10000:
                lvl2 = False
                lvl3 = True
                velocidade_pista = 1.5

        if lvl3 == True:
            if dado == 1:
                y_inimigo1 += 3

            if dado == 2:
                y_inimigo2 += 3


            if dado == 3:
                y_inimigo3 += 3

            if score > 15000:
                lvl3 = False
                lvl4 = True
                velocidade_pista = 1.7
        if lvl4 == True:
            if dado == 1:
                y_inimigo1 += 4

            if dado == 2:
                y_inimigo2 += 4


            if dado == 3:
                y_inimigo3 += 4

            if score > 20000:
                lvl4 = False
                lvl5 = True
                velocidade_pista = 1.9
        if lvl5 == True:
            if dado == 1:
                y_inimigo1 += 5

            if dado == 2:
                y_inimigo2 += 5


            if dado == 3:
                y_inimigo3 += 5

            if score > 25000:
                lvl5 = False
                lvl6 = True
                velocidade_pista = 2.2
        if lvl6 == True:
            if dado == 1:
                y_inimigo1 += 6

            if dado == 2:
                y_inimigo2 += 6


            if dado == 3:
                y_inimigo3 += 6

        #
        if y_inimigo1>900:
            y_inimigo1 = -10

        if y_inimigo2 >900:
            y_inimigo2 = -10

        if y_inimigo3 > 9000:
            y_inimigo3 = -10













        #Faz sair de dentro da tela do jogo
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                inicio()





                # Verifica se alguma tecla foi pressionada
            if event.type == pygame.KEYDOWN:
                    # Verifica se a seta esquerda foi pressionada
                if event.key == pygame.K_LEFT:
                        x_ret -= 225
                        y_ret -= 0



                        x_carro -= 225
                        y_carro += 0

                        if x_carro < 250:
                            x_carro = 250
                        if x_ret < 250:
                            x_ret = 250

                elif event.key == pygame.K_RIGHT:
                        x_ret += 225
                        y_ret -= 0



                        x_carro += 225
                        y_carro -= 0

                        if x_carro > 700:
                            x_carro = 700
                        if x_ret > 700:
                            x_ret = 700
        #Printa os inimigos
        pygame.draw.rect(DS, green, [x_inimigo1, y_inimigo1, w_inimigo1, h_inimigo1])
        pygame.draw.rect(DS, green, [x_inimigo2, y_inimigo2, w_inimigo2, h_inimigo2])
        pygame.draw.rect(DS, green, [x_inimigo3, y_inimigo3, w_inimigo3, h_inimigo3])

        pygame.draw.rect(DS, green, [x_ret, y_ret, 70, 30])
        rel_y = y % bkgd.get_rect().height
        DS.blit(bkgd, (0, rel_y - bkgd.get_rect().height))
        if rel_y < H:
            DS.blit(bkgd, (0, rel_y))

        #Print vida
        DS.blit(vida, (x_vida,y_vida))
        DS.blit(vida2, (x_vida2, y_vida2))
        DS.blit(vida3, (x_vida3, y_vida3))


        DS.blit(image2,(x_inimigo1,y_inimigo1))
        DS.blit(image3, (x_inimigo2, y_inimigo2))
        DS.blit(image6, (x_inimigo3, y_inimigo3))
        # Faz a pista rodar



        #Printa o carro

        DS.blit(image, (x_carro, y_carro))

        #Printa o Score

        if flag == True:
            print_score1 = fonte4.render(str(score), True, (ORANGE))
            print_score = fonte4.render("Score ", True, (BLACK))
            DS.blit(print_score1, [10, 30])
            DS.blit(print_score,[10,10])


#=================================== COLISOES ==========================================
        if y_inimigo1 > 565 and y_inimigo1 < 700 and x_inimigo1 == x_ret:
            audio.play()
            y_inimigo1 =-10
            cont_vida -= 1
            pygame.display.update()
            time.sleep(1)
            if cont_vida ==2:
                x_vida = 3000
                pygame.display.update()
            if cont_vida == 1:
                x_vida2 = 3000
                pygame.display.update()
            if cont_vida == 0:
                x_vida3 = 3000
                pygame.display.update()

        if y_inimigo2 > 565 and y_inimigo2 < 700 and x_inimigo2 == x_ret:
            audio.play()
            pygame.display.update()
            time.sleep(1)
            x_vida = 3000
            y_inimigo2 = -10
            cont_vida -= 1
            if cont_vida == 2:
                x_vida = 3000
                pygame.display.update()
            if cont_vida == 1:
                x_vida2 = 3000
                pygame.display.update()
            if cont_vida == 0:
                x_vida3 = 3000
                pygame.display.update()


        if y_inimigo3 > 565 and y_inimigo3 < 700 and x_inimigo3 == x_ret:
            audio.play()
            pygame.display.update()
            time.sleep(1)
            x_vida = 3000
            y_inimigo3 = -10
            cont_vida -= 1
            if cont_vida == 2:
                x_vida = 3000
                pygame.display.update()
            if cont_vida == 1:
                x_vida2 = 3000
                pygame.display.update()
            if cont_vida == 0:
                x_vida3 = 3000
                pygame.display.update()

        if cont_vida < 1:
            DS.blit(jogar_dnovo,(100,100))
            print_score = fonte4.render(" Seu Score Foi: ", True, (BLACK))
            DS.blit(print_score, [120, 200])
            DS.blit(print_score1, [285, 200])
            flag = False
            pygame.display.update()
            time.sleep(2)
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_y:
                    jogo()


#======================================================================================




        pygame.display.update()
def jogar():
    import pygame
    jogo()
    pygame.display.flip





