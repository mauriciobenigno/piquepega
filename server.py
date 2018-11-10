import sys
import json
import numpy as np
from player import Player
        
import Pyro4
import Pyro4.naming


@Pyro4.expose
@Pyro4.behavior(instance_mode="single")
class Servidor(object):
    def __init__(self):
        self.players=list()
        self.obstaculos=list()
        # paredes
        self.idPegador=None
        #self.obstaculos.append()

        # obstaculos
        self.obstaculos.append((72,91))
        self.obstaculos.append((72,196))
        self.obstaculos.append((72,265))
        self.obstaculos.append((72,370))
        self.obstaculos.append((72,475))
        self.obstaculos.append((177,475))
        self.obstaculos.append((177,337))

        # mensagem ok
        print("Servidor Iniciado!")

    def conectaPlayer(self,nome,txtImg,txtCord,coordX,coordY):
        player = Player(nome,len(self.players),txtImg,txtCord,coordX,coordY)
        self.players.append(player)
        return player.getID()

    def getPlayer(self,id):
        for player in self.players:
            if player.getID()==id:
                return player.getTudo()
                #return player
            
    def getQuantPlayers(self):
        return len(self.players)
        
    def atualizaPlayer(self,id,playerL):
        contador = 0
        playerN = Player(playerL[0],playerL[1],playerL[5],playerL[6],playerL[7],playerL[8])
        if id == self.idPegador:
            playerN.setStatus(True)
        playerN.setVidas(playerL[3])
        playerN.setVelocidade(playerL[4])
        for player in self.players:
            if player.getID()==id:
                del self.players[contador]
                self.players.insert(contador, playerN)
                break
            contador=contador+1
            
    def getObstaculos(self):
        return self.obstaculos

    def setPegador(self,idP):
        self.idPegador=idP
        

   
def main():
    Pyro4.Daemon.serveSimple(
        {
            Servidor: "example.warehouse"
        },
        ns=True)

if __name__ == "__main__":
    main()
        

    

    
