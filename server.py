import sys
import numpy as np
from player import Player

        
import Pyro4


@Pyro4.expose
@Pyro4.behavior(instance_mode="single")
class Servidor(object):
    def __init__(self):
        self.players=list()
        print("Servidor Iniciado!")

    def conectaPlayer(self,nome,imgP,rectP):
        player = Player(nome,len(self.players)+1,imgP,rectP)
        self.players.append(player)
        return player.getID()

    def getPlayer(self,id):
        for player in self.players:
            if player.getID()==id:
                return player
            
    def getQuantPlayers(self):
        return len(self.players)
        
    def atualizaPlayer(self,id,player):
        contador = 0
        for player in self.players:
            if player.getID()==id:
                del self.players[contador]
                self.players.insert(contador, player)
                break

            contador=contador+1

   
def main():
    Pyro4.Daemon.serveSimple(
        {
            Servidor: "example.warehouse"
        },
        ns=True)
   


if __name__ == "__main__":
    main()
        

    

    
