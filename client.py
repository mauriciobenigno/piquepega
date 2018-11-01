import sys
#import Pyro4
#import Pyro4.util
import pygame
import server
from server import Servidor
from player import Player


#sys.excepthook = Pyro4.util.excepthook

#servidor = Pyro4.Proxy("PYRONAME:example.warehouse")

servidor = Servidor()

id = servidor.conectaPlayer("Mau",2)

player = servidor.getPlayer(id)

player.setNome("Beta")

servidor.atualizaPlayer(id,player)

print(player.getNome())
