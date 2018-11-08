import numpy as np
import pygame

class spritesheet:
    def __init__(self,arquivo,colunas,linhas):
        self.sheet=pygame.image.load(arquivo)
        self.colunas=colunas
        self.linhas=linhas
        self.contagem=colunas*linhas
        self.rect=self.sheet.get_rect()
        w=self.cellWidth=self.rect.width/colunas
        h=self.cellHeight=self.rect.height/linhas
        hw,hh=self.cellCenter=(w/2,h/2)
        self.cells=list([(index%colunas*w, index%colunas*h,w,h) for index in range(self.contagem)])
        self.handle = list([
			(0, 0), (-hw, 0), (-w, 0),
			(0, -hh), (-hw, -hh), (-w, -hh),
			(0, -h), (-hw, -h), (-w, -h),])
        
    def draw(self, surface, cellIndex, x, y, handle = 0):
    	surface.blit(self.sheet, (x + self.handle[handle][0], y + self.handle[handle][1]), self.cells[cellIndex])


    
