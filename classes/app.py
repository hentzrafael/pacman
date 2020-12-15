import pygame
from pygame import *

class App(object):
    def __init__(self):
        super().__init__()
        self.createTilesMap()
        self.clock = pygame.time.Clock()
        self.applyTitle('Pacman - 2F Project')

    def applyTitle(self,text):
        pygame.display.set_caption(text)

    def spacePressed(self):
        key = pygame.key.get_pressed()
        if key[K_SPACE]==1:
            return True
        return False

    def tabPressed(self):
        key = pygame.key.get_pressed()
        if key[K_TAB]==1:
            return True
        return False
    
    def upPressed(self):
        key = pygame.key.get_pressed()
        if key[K_UP]==1:
            return True
        return False
    
    def downPressed(self):
        key = pygame.key.get_pressed()
        if key[K_DOWN]==1:
            return True
        return False
    
    def leftPressed(self):
        key = pygame.key.get_pressed()
        if key[K_LEFT]==1:
            return True
        return False
    
    def rightPressed(self):
        key = pygame.key.get_pressed()
        if key[K_RIGHT]==1:
            return True
        return False
    
    def rPressed(self):
        key = pygame.key.get_pressed()
        if key[K_r]==1:
            return True
        return False
    
    def createTilesMap(self):
        self.TILES = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
            [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0],
            [0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
  
    def loadImage(self,path):
        imageSurface = pygame.image.load(path)
        return imageSurface
    
    def putImageOnScreen(self,image,screen,x,y):
        screen.blit(image,[x,y])
    
    def quitApp(self):
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT or keys[K_ESCAPE]:
                pygame.quit()
                exit()

    def putText(self,text, tamanho, color,tela,x,y):
        pygame.font.init()
        base = pygame.font.SysFont('arial',tamanho,False,False)
        surface = base.render(text,0,color)
        tela.blit(surface,[x,y])
    
    def iconifyWindow(self,icon):
        pygame.display.set_icon(icon)
    


