import pygame
from pygame import *
from classes.app import App

class Pacman(object):
    LEFT = 0
    UP = 1
    RIGHT = 2
    DOWN = 3
    COLOR = (255, 255, 0)

    def __init__(self, x, y, tiles,imagePath):
        self.x = x
        self.lifes = 3
        self.y = y
        self.app = App()
        self.tiles = tiles
        self.points = 0
        self.cointiles = self.app.TILES.copy()
        self.image = pygame.transform.smoothscale(self.loadImage(imagePath),(30,30))

    
    def loadImage(self,path):
        imageSurface = pygame.image.load(path)
        return imageSurface

    def move(self, direction):
        if self.__can_move(direction):
            if direction == Pacman.LEFT: self.y -= 1
            elif direction == Pacman.UP: self.x -= 1
            elif direction == Pacman.RIGHT: self.y += 1
            elif direction == Pacman.DOWN: self.x += 1

    def __can_move(self, direction):
        width = len(self.tiles[0]) - 1
        if direction == Pacman.LEFT and self.y > 0 and self.tiles[self.x][self.y - 1]: return True
        if direction == Pacman.UP and self.x > 0 and self.tiles[self.x - 1][self.y]: return True
        if direction == Pacman.RIGHT and self.y < width and self.tiles[self.x][self.y + 1]: return True
        if direction == Pacman.DOWN and self.x < width and self.tiles[self.x + 1][self.y]: return True
        return False

    def PacmanIsDead(self,ghost):
        if self.x == ghost.x and self.y == ghost.y:
            self.lifes -= 1
            return True
        return False


