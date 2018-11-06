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
tela = pygame.display.set_mode((800, 600))
preto = (0, 0, 0) #RGB: preto == 0R, 0G, 0B

#Personagem
txtImgLoad = "imagens/Rocket.png"
txtRect = (200,100)
imgPersonagem = pygame.image.load(txtImgLoad)
imgPersonagem = pygame.transform.scale(imgPersonagem, txtRect)
rectPersonagem = imgPersonagem.get_rect()

id = servidor.conectaPlayer("Mau",txtImgLoad,txtImgLoad,0.0,0.0)

print("qtd Players: " + str(servidor.getQuantPlayers()))


playerL = servidor.getPlayer(id)
player = Player(playerL[0],playerL[1],playerL[5],playerL[6],playerL[7],playerL[8])
player.setNome("Beta")

servidor.atualizaPlayer(id,player.getTudo())

print(player.getNome())


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

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
    # Atualizando as coordenadas
    player.setCoords(rectPersonagem.x,rectPersonagem.y)
    playerL = player.getTudo()
    servidor.atualizaPlayer(id,playerL)

    print(" Coord "+str(rectPersonagem.x)+ " "+str(rectPersonagem.y))

    
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
            
    '''if player.getStatus() == True:
        for i in range(servidor.getQuantPlayers()):
            if i != id:
                #jogadorAux = servidor.getPlayer(i+1)
                #rectPAux=jogadorAux.getRectPlayer()
                #if rectPersonagem.colliderect(rectPAux):
                if rectPersonagem.colliderect(rectPersonagem2):
                    player.setStatus(False)
                    player2.setStatus(True)
                    player2.setVida(player2.getVida()-1)
                    
                    servidor.atualizaPlayer(id,player)
                    servidor.atualizaPlayer(id2,player2)'''

    tela.blit(imgPersonagem, rectPersonagem)

    
    pygame.display.update()
    clock.tick(30)

pygame.quit ()
