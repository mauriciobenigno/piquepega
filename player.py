import numpy as np
class Player:
    def __init__(self,nome,skin,id):
        self.nome=nome
        self.skin=skin
        self.id=id
        self.pos=np.array([0.0,0.0])
        self.status=False
        self.vidas=3

    def setStatus(self,status):
        self.status=status
        
    def setNome(self,nome):
        self.nome=nome

    def setPos(self,pos):
        self.pos=pos

    def setVidas(self,vidas):
        self.vidas=vidas

    def getNome(self):
        return self.nome

    def getStatus(self):
        return self.status

    def getPos(self):
        return self.pos

    def getVidas(self):
        return self.vidas

    def getID(self):
        return self.id
    
