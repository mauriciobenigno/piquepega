import sys
import Pyro4
import pygame
import server
from server import Servidor
from player import Player
from random import randint
'''
->Adicionar<-
1 - Ao passar por cima de um corpo morto, ficar lento até sair dele
2 - Player amarelo deleta o bonus do player vermelho
3 - Player que desconecta, vira morto
4 - Player pegador que desconecta, sorteia novo pegador
5 - Mudar nome pegador para infectado
6 - criar imagem de cerebro para bonus

'''
#sys.excepthook = Pyro4.util.excepthook

servidor = Pyro4.Proxy("PYRONAME:example.warehouse")
# print("servidor: " + str(objServidor))

# Informações iniciais
nome = input("Nome: ")
pygame.init()
clock = pygame.time.Clock()
ALTURA = 540
LARGURA = 790
AREA = ALTURA*LARGURA

tela = pygame.display.set_mode((LARGURA,ALTURA))
pygame.display.set_caption("Pique e Pega: Multiplayer")

# Cores
preto = (0, 0, 0) #RGB: preto == 0R, 0G, 0B
branco = (255, 255, 255)

# Texto Nomes
fonte = pygame.font.SysFont("arial", 10)
fonte2 = pygame.font.SysFont("arial", 30)
nickName = None

# Sons de fundo
pygame.mixer.music.load("sons/sbb416.mp3")
pygame.mixer.music.play(loops = -1)
sfxColisao = pygame.mixer.Sound("sons/beep_02.wav")

# Tela de fundo
imgBackGround =  pygame.image.load("imagens/gramado.jpg")
rectBackGround = imgBackGround.get_rect()

# Paredes
def colisaoParede(X,Y):
    if X<=0:
        return True
    if X+50>=LARGURA:
        return True
    if Y<=0:
        return True
    if Y+50>=ALTURA:
        return True
    return False

# Obstaculos
obstaculos = servidor.getObstaculos()
obstaculosImg = pygame.image.load("imagens/obstaculo.jpg")
obstaculosScale = (60,60)
obstaculosImg = pygame.transform.scale(obstaculosImg, obstaculosScale)
obstaculosRect = list()
for i in range(len(obstaculos)):
    obstaculosRt = obstaculosImg.get_rect();
    obstaculosRt.x = obstaculos[i][0]
    obstaculosRt.y = obstaculos[i][1]
    obstaculosRect.append(obstaculosRt)

def colisaoObstaculos():
    for obstaculoI in obstaculosRect:
       if rectPersonagem.colliderect(obstaculoI):
           return True
    return False

# Passar a vez
foiPego=False
freezePego=0

# Numero da sorte - Bonus
numeroSorte = randint(0,50)
imgBonus = pygame.image.load("imagens/morreu.png")
imgBonus = pygame.transform.scale(imgBonus, (50,50))
rectBonus = imgBonus.get_rect()


# Personagem
txtImgLoad = "imagens/feliz.png"
txtRect = (50,50)
imgPersonagem = pygame.image.load(txtImgLoad)
imgPersonagem = pygame.transform.scale(imgPersonagem, txtRect)
rectPersonagem = imgPersonagem.get_rect()
rectPersonagem.x=1
rectPersonagem.y=1

id = servidor.conectaPlayer("Mau",txtImgLoad,txtImgLoad,0.0,0.0)

print("qtd Players: " + str(servidor.getQuantPlayers()))


playerL = servidor.getPlayer(id)
player = Player(playerL[0],playerL[1],playerL[5],playerL[6],playerL[7],playerL[8])
#player.setStatus(True)

servidor.atualizaPlayer(id,player.getTudo())



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Morre pro resto do servidor
            txtImgLoad="imagens/morreu.png"
            imgPersonagem = pygame.image.load(txtImgLoad)
            imgPersonagem = pygame.transform.scale(imgPersonagem, txtRect)
            rectPersonagem = imgPersonagem.get_rect()
            rectPersonagem.x=player.getCoordX()
            rectPersonagem.y=player.getCoordY()
            player.setImg(txtImgLoad)
            servidor.atualizaPlayer(id,playerL)
            tela.blit(imgBonus, rectBonus)
            # Finaliza o jogo
            pygame.quit()
            exit()
            

            
    # Se atualiza com informações do player no servidor
    playerL = servidor.getPlayer(id)
    #Detectar se foi pego
    if playerL[2] == True:
        player.setStatus(True)
    if playerL[2] == False:
        player.setStatus(False)
        
    if player.getStatus() == True and foiPego == False:
        if freezePego < 120:
            player.setVelocidade(3)
            freezePego=freezePego+1
        if freezePego >= 120:
            freezePego=0
            foiPego=True
            player.setVelocidade(5)
 
    
 
    #Movimentação do personagem
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_d]:
        rectPersonagem.move_ip(player.getVelocidade(), 0)
        if colisaoParede(rectPersonagem.x,rectPersonagem.y) or colisaoObstaculos():
            rectPersonagem.move_ip(-player.getVelocidade(), 0)
    if tecla[pygame.K_a]:
        rectPersonagem.move_ip(-player.getVelocidade(), 0)
        if colisaoParede(rectPersonagem.x,rectPersonagem.y) or colisaoObstaculos():
            rectPersonagem.move_ip(player.getVelocidade(), 0)
    if tecla[pygame.K_w]:
        rectPersonagem.move_ip(0, -player.getVelocidade())
        if colisaoParede(rectPersonagem.x,rectPersonagem.y) or colisaoObstaculos():
            rectPersonagem.move_ip(0, player.getVelocidade())
    if tecla[pygame.K_s]:
        rectPersonagem.move_ip(0, player.getVelocidade())
        if colisaoParede(rectPersonagem.x,rectPersonagem.y) or colisaoObstaculos():
            rectPersonagem.move_ip(0, -player.getVelocidade())
    if tecla[pygame.K_e]:
        print(" Coodenadas x "+str(rectPersonagem.x)+" y "+str(rectPersonagem.y) )
    if tecla[pygame.K_q]:
        foiPego=True
        player.setStatus(True)
        playerL[2]=True
        servidor.setPegador(id)
        servidor.atualizaPlayer(id,playerL)
        print("Agora sou mal")
           
    if tecla[pygame.K_h]:
        player.setStatus(False)
    if tecla[pygame.K_j]:
        player.setStatus(True)
    if tecla[pygame.K_k]:
        player.setVidas(0)
    if tecla[pygame.K_l]:
        player.setVidas(999)
    if tecla[pygame.K_m]:
        player.setVelocidade(7)
    
    # Atualizando as coordenadas
    player.setCoords(rectPersonagem.x,rectPersonagem.y)
    playerL = player.getTudo()
    servidor.atualizaPlayer(id,playerL)
    
    #Desenho do background
    tela.blit(imgBackGround, (0,0))

    for obstaculoIR in obstaculosRect:
        tela.blit(obstaculosImg, obstaculoIR)
        if player.getStatus() == True and servidor.getBonus() == True:
                if rectPersonagem.colliderect(rectBonus):
                    player.setVelocidade(7)
                    servidor.desativarBonus()
                    nickname = fonte.render(str("COLISAO"), True, (255,0,0))
                    sfxColisao.play(loops=0, maxtime=0)
                    tela.blit(nickname, rectPersonagem)
    
       
    for i in range(servidor.getQuantPlayers()):
        if i != id:
            oPlayers = servidor.getPlayer(i)
            imgJog = pygame.image.load(oPlayers[5])
            imgJog = pygame.transform.scale(imgJog,txtRect)
            rectJogs = imgJog.get_rect()
            rectJogs.x=oPlayers[7]
            rectJogs.y=oPlayers[8]
            tela.blit(imgJog, rectJogs)
            if player.getStatus() == True and foiPego == True:
                if rectPersonagem.colliderect(rectJogs):
                    nickname = fonte.render(str("COLISAO"), True, (255,0,0))
                    sfxColisao.play(loops=0, maxtime=0)
                    tela.blit(nickname, rectPersonagem)
                    # Passar a vez para o jogador
                    player.setStatus(False)
                    playerL[2]=False
                    foiPego=False
                    servidor.setPegador(i)
            

                    
                    


    if player.getStatus() == True and player.getVelocidade()>5:
        txtImgLoad="imagens/mauTunado.png"
        imgPersonagem = pygame.image.load(txtImgLoad)
        imgPersonagem = pygame.transform.scale(imgPersonagem, txtRect)
        rectPersonagem = imgPersonagem.get_rect()
        rectPersonagem.x=player.getCoordX()
        rectPersonagem.y=player.getCoordY()
        player.setImg(txtImgLoad)
        servidor.atualizaPlayer(id,playerL)
    elif player.getStatus() == True:
        txtImgLoad="imagens/mau.png"
        imgPersonagem = pygame.image.load(txtImgLoad)
        imgPersonagem = pygame.transform.scale(imgPersonagem, txtRect)
        rectPersonagem = imgPersonagem.get_rect()
        rectPersonagem.x=player.getCoordX()
        rectPersonagem.y=player.getCoordY()
        player.setImg(txtImgLoad)
        servidor.atualizaPlayer(id,playerL)
        if servidor.getBonus() == False:
            numAux = randint(0,50)
            if numeroSorte == numAux:
                servidor.ativarBonus()

    
    if player.getStatus() == False:
        txtImgLoad="imagens/feliz.png"
        imgPersonagem = pygame.image.load(txtImgLoad)
        imgPersonagem = pygame.transform.scale(imgPersonagem, txtRect)
        rectPersonagem = imgPersonagem.get_rect()
        rectPersonagem.x=player.getCoordX()
        rectPersonagem.y=player.getCoordY()
        player.setImg(txtImgLoad)
        player.setVelocidade(5)
        servidor.atualizaPlayer(id,playerL)
    if player.getVidas() == 0:
        txtImgLoad="imagens/morreu.png"
        imgPersonagem = pygame.image.load(txtImgLoad)
        imgPersonagem = pygame.transform.scale(imgPersonagem, txtRect)
        rectPersonagem = imgPersonagem.get_rect()
        rectPersonagem.x=player.getCoordX()
        rectPersonagem.y=player.getCoordY()
        player.setImg(txtImgLoad)
        servidor.atualizaPlayer(id,playerL)

    tela.blit(imgPersonagem, rectPersonagem)

    if servidor.getBonus() == True:
        cordBonus = servidor.getCordBonus()
        rectBonus.x = cordBonus[0]
        rectBonus.y = cordBonus[1]
        tela.blit(imgBonus, rectBonus)

    # Mostrar vidas
    score = fonte2.render ("Vidas: " + str(player.getVidas()), True, (255, 255, 255))
    tela.blit(score, (10,5))

    # Mostrar nome
    nickname = fonte.render(str(nome), True, (0,255,0))
    tela.blit(nickname, rectPersonagem)
    
    pygame.display.update()
    clock.tick(60)

pygame.quit ()
