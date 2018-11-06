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
txtCords = (200,100)
imgPersonagem = pygame.image.load(txtImgLoad)
imgPersonagem = pygame.transform.scale(imgPersonagem, txtCords)
rectPersonagem = imgPersonagem.get_rect()

imgPersonagem2 = pygame.image.load(txtImgLoad)
imgPersonagem2 = pygame.transform.scale(imgPersonagem2, txtCords)
rectPersonagem2 = imgPersonagem2.get_rect()
# print("qtd Players: " + str(servidor.getQuantPlayers()))
id2 = servidor.conectaPlayer("Mau3",txtImgLoad,txtCords,0.0,0.0)
id = servidor.conectaPlayer("Mau",txtImgLoad,txtImgLoad,0.0,0.0)

print("qtd Players: " + str(servidor.getQuantPlayers()))


playerL = servidor.getPlayer(id)
player = Player(playerL[0],playerL[1],playerL[5],playerL[6],playerL[7],playerL[8])
player.setNome("Beta")
playerL = servidor.getPlayer(id2)
player2 = Player(playerL[0],playerL[1],playerL[5],playerL[6],playerL[7],playerL[8])
player2.setNome("Alfa")

servidor.atualizaPlayer(id,player.getTudo())
servidor.atualizaPlayer(id2,player2.getTudo())

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
    #player.setCoords(rectPersonagem.x,rectPersonagem.y)
    #servidor.atualizaPlayer(id,player)

    if tecla[pygame.K_l]:
        rectPersonagem2.move_ip(player2.getVelocidade(), 0)
    if tecla[pygame.K_j]:
        rectPersonagem2.move_ip(-player2.getVelocidade(), 0)
    if tecla[pygame.K_i]:
        rectPersonagem2.move_ip(0, -player2.getVelocidade())
    if tecla[pygame.K_k]:
        rectPersonagem2.move_ip(0, player2.getVelocidade())

    #player.setCoords(rectPersonagem2.x,rectPersonagem2.y)
    #servidor.atualizaPlayer(id2,player2)

    
    #Desenho do background
    tela.fill(preto)
    '''   
    for i in range(servidor.getQuantPlayers()):

        jogadorAux = servidor.getPlayer(i+1)
        imgPAux=jogadorAux.getImgPlayer()
        rectPAux=jogadorAux.getRectPlayer()
        tela.blit(imgPAux, rectPAux)

    if player.getStatus() == True:
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
    tela.blit(imgPersonagem2, rectPersonagem2)
    
    pygame.display.update()
    clock.tick(30)

pygame.quit ()
