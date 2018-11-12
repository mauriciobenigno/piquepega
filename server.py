import sys
import json
import numpy as np
from random import randint
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
        # Bonus
        self.bonus=False
        self.cordBonus= list()
        self.cordBonus.append(0.0)
        self.cordBonus.append(0.0)

        # obstaculos
        valX = 60
        valY = 60
        for i in range(12):
            for k in range(8):
                if i%2 != 0 and k%2 !=0:
                    self.obstaculos.append((valX*(i),valY*(k)))
            

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

    def ativarBonus(self):
        self.bonus=True
        valX = 60
        valY = 60
        numSorteado = randint(0,48)
        contador = 0
        print("Bonus num "+str(numSorteado))
        for i in range(12):
            for k in range(8):
                if i%2 == 0 and k%2 ==0:
                    print("contador = "+str(contador))
                    if contador == numSorteado:
                        self.cordBonus[0]=(valX*(i))
                        self.cordBonus[1]=(valY*(k))
                        print("Novo cord X "+str(self.cordBonus[0])+" Y "+str(self.cordBonus[1]))
                        break
                    else:
                        contador= contador+1
            if contador == numSorteado:
                break
                        
        
    def desativarBonus(self):
        self.bonus=False

    def getBonus(self):
        return self.bonus

    def getCordBonus(self):
        return self.cordBonus
        

   
def main():
    Pyro4.Daemon.serveSimple(
        {
            Servidor: "example.warehouse"
        },
        ns=True)

if __name__ == "__main__":
    main()
        

    

    
