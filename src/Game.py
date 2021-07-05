from src.Sprite import Sprite
from pygame import draw
from src.Player import Player
import pygame
from pygame.locals import *

class Game:
    def __init__(self):
        print("Game")
        self.player = Player()

        self.createWindow()

    def createWindow(self):
        pygame.init()

        size = 1600, 600

        self.screen1 = pygame.display.set_mode(size)

        pygame.display.set_caption("Zero Demo")
        self.icon = pygame.image.load("./src/media/icono.png")
        pygame.display.set_icon(self.icon)
        flag = True
        self.setSprites()
        self.frame = 0
        while flag:
            self.drawSprites()
            pygame.display.update()
            pygame.time.delay(60)
            pygame.display.flip()
            pygame.key.set_repeat(60, 30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    flag = False
                elif event.type == pygame.KEYDOWN:
                    self.moveControls(event)
                elif event.type == pygame.KEYUP:
                    self.player.image = self.player.idleSprite[self.player.direction]

    def setSprites(self):
        self.background = Sprite("./src/media/fondo-lejano.png")
        self.highGrass = Sprite("./src/media/pasto-alto.png")
        self.background.draw(self.screen1, 0, 0)
        self.player.draw(self.screen1, 180, 410)
        self.highGrass.image = pygame.transform.scale(self.highGrass.image, (1600,600))
        self.highGrass.draw(self.screen1, 0, 0)
        
    def drawSprites(self):
        self.background.draw(self.screen1, self.background.x, self.background.y)
        self.player.draw(self.screen1, self.player.x, self.player.y)
        self.highGrass.draw(self.screen1, self.highGrass.x, self.highGrass.y)
        
    def moveControls(self, event):
        if event.key == pygame.K_d:
            self.frame = self.player.moveRight(self.screen1, self.frame)
            if (self.player.x >= 1300):
                self.player.movePlayer(180, 410)
        elif event.key == pygame.K_a:
            self.frame = self.player.moveLeft(self.screen1, self.frame)
        elif  event.key == pygame.K_UP or event.key == pygame.K_w:
            self.frame = self.player.jump(self.screen1, self.frame)
            
