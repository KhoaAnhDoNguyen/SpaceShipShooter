import pygame , time, sys
import random
import math
from pygame import mixer
import time

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
screen = pygame.display.set_mode((1400, 788))

class Bullet():
    def __init__ (self, x = -100, y = -100, Status = 'Free', Type = 'S'):
        self.x = x
        self.y = y
        self.Bullet = pygame.image.load("yellowbulletS.png").convert_alpha()
        self.Status = Status
        self.Type = Type
    def DisPlayBullet(self):
        screen.blit(self.Bullet, (self.x, self.y))
    def Get_Status(self):
        return self.Status
    def Get_x(self):
        return self.x
    def Get_y (self):
        return self.y



