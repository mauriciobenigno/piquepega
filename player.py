import numpy as np
import pygame

class Player:
    def __init__(self,nome,id,imgPlayer,rectPlayer):
        self.nome=nome
        self.id=id
        self.status=False
        self.vidas=3
        self.velocidade=5
        self.imgPlayer=imgPlayer
        self.rectPlayer=rectPlayer
        

    def setStatus(self,status):
        self.status=status
        
    def setNome(self,nome):
        self.nome=nome

    def setVidas(self,vidas):
        self.vidas=vidas
        
    def setImgPlayer(self,imgPlayer):
        self.imgPlayer=imgPlayer
        
    def setRectPlayer(self,rectPlayer):
        self.rectPlayer=rectPlayer

    def getNome(self):
        return self.nome

    def getStatus(self):
        return self.status

    def getVidas(self):
        return self.vidas

    def getID(self):
        return self.id
    
    def getImgPlayer(self):
        return self.imgPlayer

    def getRectPlayer(self):
        return self.rectPlayer

    def getVelocidade(self):
        return self.velocidade
    

