import sys
import Pyro4
#import Pyro4.util
import pygame
import server
from server import Servidor
from player import Player

#sys.excepthook = Pyro4.util.excepthook

servidor = Pyro4.Proxy("PYRONAME:example.warehouse")
# print("servidor: " + str(objServidor))
print("qtd Players: " + str(servidor.getQuantPlayers()))

# Informações iniciais
nome = input("Nome: ")
pygame.init()
clock = pygame.time.Clock()
tela = pygame.display.set_mode((800, 600))
preto = (0, 0, 0) #RGB: preto == 0R, 0G, 0B

# Servidor
# servidor = Servidor()

#Personagem
imgPersonagem = pygame.image.load("imagens/Rocket.png")
imgPersonagem = pygame.transform.scale(imgPersonagem, (200,100))
rectPersonagem = imgPersonagem.get_rect()

imgPersonagem2 = pygame.image.load("imagens/Rocket.png")
imgPersonagem2 = pygame.transform.scale(imgPersonagem, (200,100))
rectPersonagem2 = imgPersonagem.get_rect()
# print("qtd Players: " + str(servidor.getQuantPlayers()))
id2 = servidor.conectaPlayer("Mau2",imgPersonagem,rectPersonagem)
id2 = servidor.conectaPlayer("Mau2",imgPersonagem,rectPersonagem)
id2 = servidor.conectaPlayer("Mau2",imgPersonagem2,rectPersonagem2)
id = servidor.conectaPlayer("Mau",imgPersonagem,rectPersonagem)

player = servidor.getPlayer(id)
player.setNome("Beta")
player2 = servidor.getPlayer(id2)
player2.setNome("Alfa")

servidor.atualizaPlayer(id,player)
servidor.atualizaPlayer(id2,player2)

print(player.getNome())


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #Movimentação do personagem
    imgPersonagem = player.getImgPlayer()
    rectPersonagem = player.getRectPlayer()
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_d]:
        rectPersonagem.move_ip(player.getVelocidade(), 0)
    if tecla[pygame.K_a]:
        rectPersonagem.move_ip(-player.getVelocidade(), 0)
    if tecla[pygame.K_w]:
        rectPersonagem.move_ip(0, -player.getVelocidade())
    if tecla[pygame.K_s]:
        rectPersonagem.move_ip(0, player.getVelocidade())


    if tecla[pygame.K_l]:
        rectPersonagem2.move_ip(player2.getVelocidade(), 0)
    if tecla[pygame.K_j]:
        rectPersonagem2.move_ip(-player2.getVelocidade(), 0)
    if tecla[pygame.K_i]:
        rectPersonagem2.move_ip(0, -player2.getVelocidade())
    if tecla[pygame.K_k]:
        rectPersonagem2.move_ip(0, player2.getVelocidade())

    player2.setImgPlayer(imgPersonagem2)
    player2.setRectPlayer(rectPersonagem2)
    servidor.atualizaPlayer(id2,player2)
    
    #Desenho do background
    tela.fill(preto)

    player.setImgPlayer(imgPersonagem)
    player.setRectPlayer(rectPersonagem)

    servidor.atualizaPlayer(id,player)
    
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
                    servidor.atualizaPlayer(id2,player2)


        
    #player.setImgPlayer(imgPersonagem)
    #player.setRectPlayer(rectPersonagem)
        
    #tela.blit(imgPersonagem, rectPersonagem)
    
    pygame.display.update()
    clock.tick(30)

pygame.quit ()
