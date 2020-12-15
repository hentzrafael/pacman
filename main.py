import pygame,random
from classes.pacman import Pacman
from classes.ghosts import Ghost
from classes.maze import Maze
from classes.app import App
from pygame import *

pygame.init()

app = App()
pacman = Pacman(1, 1, app.TILES,'img/pacman.png')
maze = Maze(app.TILES,pacman)
ghost = Ghost(9,10,app.TILES,maze.screen)
secondGhost = Ghost(9,10,app.TILES,maze.screen)
thirdGhost = Ghost(9,10,app.TILES,maze.screen)

welcomeScreen = True
winScreen = False
gameScreen = False
restartScreen = False

iconSurface = app.loadImage('img/icon.png')
app.iconifyWindow(iconSurface)

imagemWelcome = app.loadImage('img/welcome.jpg')
imagemRestart = app.loadImage('img/restart.jpg')
imagemGame = app.loadImage('img/ingame.jpg')
imagemWin = app.loadImage('img/winScreen.jpg')

first = True
firstTime = True

lastPressed = Pacman.RIGHT
numberOfGhosts = 1

def resetPositions():
    pacman.x = 1
    pacman.y = 1
    ghost.x = 9
    secondGhost.x = 9
    secondGhost.y = 10
    thirdGhost.x = 9 
    thirdGhost.y = 10 
    ghost.y = 10

def resetData():
    pacman.points = 0
    welcomeScreen = True
    restartScreen = False
    pacman.lifes = 3
    numberOfGhosts = 1
    lastPressed = pacman.RIGHT


while True:

    if welcomeScreen:
        app.putImageOnScreen(imagemWelcome,maze.screen,0,0)
        app.quitApp()        
        if app.spacePressed():
            welcomeScreen = False
            gameScreen = True
                
    elif gameScreen:
        app.putImageOnScreen(imagemGame,maze.screen,0,0)
        maze.draw()

        if numberOfGhosts == 1:
            ghost.ghostDraw(ghost)
            ghost.move()
            if pacman.PacmanIsDead(ghost):
                pacman.x = 1
                pacman.y = 1
        elif numberOfGhosts == 2:
            ghost.ghostDraw(ghost)
            secondGhost.ghostDraw(secondGhost)
            ghost.move()
            secondGhost.move()
            if pacman.PacmanIsDead(ghost) or pacman.PacmanIsDead(secondGhost):
                pacman.x = 1
                pacman.y = 1
        elif numberOfGhosts == 3:
            ghost.ghostDraw(ghost)
            secondGhost.ghostDraw(secondGhost)
            thirdGhost.ghostDraw(thirdGhost)
            ghost.move()
            secondGhost.move()
            thirdGhost.move()
            if pacman.PacmanIsDead(ghost) or pacman.PacmanIsDead(secondGhost) or pacman.PacmanIsDead(thirdGhost):
                pacman.x = 1
                pacman.y = 1
        app.putText('Vidas restantes: '+str(pacman.lifes),60,(255,255,255),maze.screen,800,200)
        app.putText(str(pacman.points),50,(255,255,255),maze.screen,800,600)

        
        if pacman.lifes == 0:
            gameScreen = False
            restartScreen = True

        if app.tabPressed():
            pacman.points = 2140
   
        if app.upPressed(): 
            lastPressed = Pacman.UP
            pacman.move(Pacman.UP)

        if app.downPressed(): 
            lastPressed = Pacman.DOWN
            pacman.move(Pacman.DOWN)

        if app.leftPressed(): 
            pacman.move(Pacman.LEFT)
            lastPressed = Pacman.LEFT

        if app.rightPressed(): 
            pacman.move(Pacman.RIGHT)
            lastPressed = Pacman.RIGHT
        
        if pacman.points >= 400 and first:
            numberOfGhosts = 2
            first = False
        elif pacman.points >= 700 and firstTime:
            numberOfGhosts = 3
            firstTime = False
        
        if pacman.points == 2140:
            winScreen = True
            gameScreen = False

        pacman.move(lastPressed)


    elif winScreen:
        app.putImageOnScreen(imagemWin,maze.screen,0,0)
        if app.rPressed():
            winScreen = False
            welcomeScreen = True
            resetData()


    elif restartScreen:
        app.putImageOnScreen(imagemRestart,maze.screen,0,0)
        app.putText(str(pacman.points),100,(255,255,255),maze.screen,860,345)
        if app.rPressed():
            resetData()
            numberOfGhosts = 1
            maze.createCointiles()
            resetPositions()
            restartScreen = False
            welcomeScreen = True
    
    app.quitApp()    
    pygame.display.update()
    app.clock.tick(30)
