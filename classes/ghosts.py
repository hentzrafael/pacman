import pygame,random
from pygame import *
from classes.maze import Maze
from classes.pacman import Pacman

class Ghost(Pacman):
    def __init__(self, x, y, tiles,screen):
        self.x = x
        self.y = y
        self.screen = screen
        self.drawer = pygame.draw
        self.tiles = tiles

    def randomDirection(self):
        selectedDirection = random.choice([Ghost.LEFT,Ghost.RIGHT,Ghost.UP,Ghost.DOWN])
        return selectedDirection
    
    def move(self):
        direction = self.randomDirection()
        if self.__can_move(direction):
            if direction == Ghost.LEFT: self.y -= 1
            elif direction == Ghost.UP: self.x -= 1
            elif direction == Ghost.RIGHT: self.y += 1
            elif direction == Ghost.DOWN: self.x += 1

    def __can_move(self, direction):
        width = len(self.tiles[0]) - 1
        if direction == Ghost.LEFT and self.y > 0 and self.tiles[self.x][self.y - 1]: return True
        if direction == Ghost.UP and self.x > 0 and self.tiles[self.x - 1][self.y]: return True
        if direction == Ghost.RIGHT and self.y < width and self.tiles[self.x][self.y + 1]: return True
        if direction == Ghost.DOWN and self.x < width and self.tiles[self.x + 1][self.y]: return True
        return False
    

    def ghostDraw(self,ghost):
        mid_square = Maze.SQUARE_SIZE // 2
        ghostY = ghost.y * Maze.SQUARE_SIZE
        ghostX = ghost.x * Maze.SQUARE_SIZE
        ghost.drawer.circle(ghost.screen, (0,255,0), (ghostY + mid_square, ghostX + mid_square), 10, 0)

    def ghostTwoDraw(self):
        mid_square = Maze.SQUARE_SIZE // 2
        ghostY = self.y * Maze.SQUARE_SIZE
        ghostX = self.x * Maze.SQUARE_SIZE
        self.drawer.circle(self.screen, (0,255,0), (ghostY + mid_square, ghostX + mid_square), 10, 0)
    
    def ghostThreeDraw(self):
        mid_square = Maze.SQUARE_SIZE // 2
        ghostY = self.y * Maze.SQUARE_SIZE
        ghostX = self.x * Maze.SQUARE_SIZE
        self.drawer.circle(self.screen, (0,255,0), (ghostY + mid_square, ghostX + mid_square), 10, 0)
