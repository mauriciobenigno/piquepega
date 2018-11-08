import sys
import Pyro4
import pygame
import server
from server import Servidor
from player import Player

#sys.excepthook = Pyro4.util.excepthook

servidor = Pyro4.Proxy("PYRONAME:example.warehouse")
# print("servidor: " + str(objServidor))

# Informações iniciais
nome = input("Nome: ")
pygame.init()
clock = pygame.time.Clock()
ALTURA = 800
LARGURA = 600
AREA = ALTURA*LARGURA

tela = pygame.display.set_mode((ALTURA, LARGURA))
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

#Personagem
txtImgLoad = "imagens/feliz.png"
txtRect = (50,50)
imgPersonagem = pygame.image.load(txtImgLoad)
imgPersonagem = pygame.transform.scale(imgPersonagem, txtRect)
rectPersonagem = imgPersonagem.get_rect()

id = servidor.conectaPlayer("Mau",txtImgLoad,txtImgLoad,0.0,0.0)

print("qtd Players: " + str(servidor.getQuantPlayers()))


playerL = servidor.getPlayer(id)
player = Player(playerL[0],playerL[1],playerL[5],playerL[6],playerL[7],playerL[8])
player.setNome("Beta")
player.setStatus(True)

servidor.atualizaPlayer(id,player.getTudo())

print(player.getNome())


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #Atualização de Sprite

    #Movimentação do personagem
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_d]:
        rectPersonagem.move_ip(player.getVelocidade(), 0)
    if tecla[pygame.K_a]:
        rectPersonagem.move_ip(-player.getVelocidade(), 0)
    if tecla[pygame.K_w]:
        rectPersonagem.move_ip(0, -player.getVelocidade())
    if tecla[pygame.K_s]:
        rectPersonagem.move_ip(0, player.getVelocidade())

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
        
    servidor.atualizaPlayer(id,player.getTudo())    
    # Atualizando as coordenadas
    player.setCoords(rectPersonagem.x,rectPersonagem.y)
    playerL = player.getTudo()
    servidor.atualizaPlayer(id,playerL)
    
    #Desenho do background
    tela.fill(preto)
       
    for i in range(servidor.getQuantPlayers()):
        if i != id:
            oPlayers = servidor.getPlayer(i)
            imgJog = pygame.image.load(oPlayers[5])
            imgJog = pygame.transform.scale(imgJog,txtRect)
            rectJogs = imgJog.get_rect()
            rectJogs.x=oPlayers[7]
            rectJogs.y=oPlayers[8]
            tela.blit(imgJog, rectJogs)
            if player.getStatus() == True:
                if rectPersonagem.colliderect(rectJogs):
                    nickname = fonte.render(str("COLISAO"), True, (255,0,0))
                    sfxColisao.play(loops=0, maxtime=0)
                    tela.blit(nickname, rectPersonagem)

    if player.getStatus() == True:
        txtImgLoad="imagens/mau.png"
        imgPersonagem = pygame.image.load(txtImgLoad)
        imgPersonagem = pygame.transform.scale(imgPersonagem, txtRect)
        rectPersonagem = imgPersonagem.get_rect()
        rectPersonagem.x=player.getCoordX()
        rectPersonagem.y=player.getCoordY()
        player.setImg(txtImgLoad)
        servidor.atualizaPlayer(id,playerL)
    if player.getStatus() == True and player.getVelocidade()>5:
        txtImgLoad="imagens/mauTunado.png"
        imgPersonagem = pygame.image.load(txtImgLoad)
        imgPersonagem = pygame.transform.scale(imgPersonagem, txtRect)
        rectPersonagem = imgPersonagem.get_rect()
        rectPersonagem.x=player.getCoordX()
        rectPersonagem.y=player.getCoordY()
        player.setImg(txtImgLoad)
        servidor.atualizaPlayer(id,playerL)
    if player.getStatus() == False:
        txtImgLoad="imagens/feliz.png"
        imgPersonagem = pygame.image.load(txtImgLoad)
        imgPersonagem = pygame.transform.scale(imgPersonagem, txtRect)
        rectPersonagem = imgPersonagem.get_rect()
        rectPersonagem.x=player.getCoordX()
        rectPersonagem.y=player.getCoordY()
        player.setImg(txtImgLoad)
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
        #tela.blit(imgPersonagem, rectPersonagem)

    tela.blit(imgPersonagem, rectPersonagem)

    # Mostrar vidas
    score = fonte2.render ("Vidas: " + str(player.getVidas()), True, (255, 255, 255))
    tela.blit(score, (10,5))

    # Mostrar nome
    nickname = fonte.render(str(nome), True, (0,255,0))
    tela.blit(nickname, rectPersonagem)
    
    pygame.display.update()
    clock.tick(60)

pygame.quit ()
