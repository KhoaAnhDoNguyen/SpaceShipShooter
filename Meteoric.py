import pygame , time, sys
import random
import math
from pygame import mixer
import time
import Bullet
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
screen = pygame.display.set_mode((1400, 788))

class Meteoric():
    def __init__ (self, x = -100, y = -100, Meteoric = 'meteoricS.png', Status = 'Free', Type = 'Straight'):
        self.x = x 
        self.y = y
        self.Meteoric = pygame.image.load(Meteoric).convert_alpha()
        self.Status = Status
        self.Type = Type
        self.velocityMeteoric = 3
    def DisPlayMeteoric(self):
        screen.blit( self.Meteoric, (self.x, self.y) )
    def Get_Status(self):
        return self.Status
    def Get_x(self):
        return self.x
    def Get_y (self):
        return self.y
    def Get_Type(self):
        return self.Type




