import numpy as np
import pygame

class Player:
    def __init__(self,nome,id,txtImg,txtRect,coordX,coordY):
        self.nome=nome
        self.id=id
        self.status=False
        self.vidas=3
        self.velocidade=3
        self.txtImg=txtImg
        self.txtRect=txtRect
        self.coordX=coordX;
        self.coordY=coordY;

    def getTudo(self):
        return [self.nome,self.id,self.status,self.vidas,self.velocidade,self.txtImg,self.txtRect,self.coordX,self.coordY]    

    def setStatus(self,status):
        self.status=status
        
    def setNome(self,nome):
        self.nome=nome

    def setVidas(self,vidas):
        self.vidas=vidas
        
    def setImg(self,txtImg):
        self.txtImg=txtImg
        
    def setRect(self,txtImg,txtRect):
        self.txtRect=txtRect

    def setImgRect(self,txtImg,txtRect):
        self.txtImg=txtImg
        self.txtRect=txtRect
        
    def setVelocidade(self,velocidade):
        self.velocidade=velocidade

    def setCoords(self,coordX,coordY):
        self.coordX=coordX;
        self.coordY=coordY;

    def getNome(self):
        return self.nome

    def getStatus(self):
        return self.status

    def getVidas(self):
        return self.vidas

    def getID(self):
        return self.id
    
    def getImg(self):
        return self.txtImg

    def getRect(self):
        return self.txtRect

    def getVelocidade(self):
        return self.velocidade

    def getCoordX(self):
        return self.coordX;
    
    def getCoordY(self):
        return self.coordY;
    

