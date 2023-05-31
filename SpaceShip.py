import pygame , time, sys
import random
import math
from pygame import mixer
import time
import Bullet
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
screen = pygame.display.set_mode((1400, 788))

class SpaceShip():
    def __init__ (self, x = 700, y = 680, name = ""):
        self.x = x
        self.y = y
        self.Rocket = pygame.image.load(name).convert_alpha()
    def MoveRocket(self, Game_Control = 'Both'):
        if Game_Control == 'Both':
            Button = pygame.key.get_pressed()
            Mouse = pygame.mouse.get_pressed()
            if (Button[pygame.K_w] or Button[pygame.K_UP]) and self.y >= 300:
                self.y -= 10
            if (Button[pygame.K_s] or Button[pygame.K_DOWN]) and self.y <= 680:
                self.y += 10
            if (Button[pygame.K_a] or Button[pygame.K_LEFT]) and self.x >= 7:
                self.x -= 10
            if (Button[pygame.K_d] or Button[pygame.K_RIGHT]) and self.x <= 1325:
                self.x += 10
        if Game_Control == 'Keyboard':
            Button = pygame.key.get_pressed()
            if (Button[pygame.K_w] or Button[pygame.K_UP]) and self.y >= 300:
                self.y -= 10
            if (Button[pygame.K_s] or Button[pygame.K_DOWN]) and self.y <= 680:
                self.y += 10
            if (Button[pygame.K_a] or Button[pygame.K_LEFT]) and self.x >= 7:
                self.x -= 10
            if (Button[pygame.K_d] or Button[pygame.K_RIGHT]) and self.x <= 1325:
                self.x += 10
        if Game_Control == 'Mouse':
            #pygame.mouse.set_visible(False)
            #screen.blit(NewCursor, (-100, -100))
            pos = pygame.mouse.get_pos()
            distance = math.sqrt( (( pos[0] - self.x )**2) + (( pos[1] - self.y )**2) )
            if pos[0] >= 7 and pos[0] <= 1325 and pos[1] >= 300 and pos[1] <= 680: 
                if distance > 1:
                    if self.x < pos[0] and self.y > pos[1]:
                        self.x += 10
                        self.y -= 10
                    if self.x < pos[0] and self.y < pos[1]:
                        self.x += 10
                        self.y += 10
                    if self.x > pos[0] and self.y > pos[1]:
                        self.x -= 10
                        self.y -= 10
                    if self.x > pos[0] and self.y < pos[1]:
                        self.x -= 10
                        self.y += 10
    def DisPlayRocket(self):
        screen.blit(self.Rocket, (self.x, self.y))
    def PrepareBullet(self, Bull, Bullet_Color):
        if Bull.Get_Status() == 'Free':
            if Bull.Type == 'S':
                if Bullet_Color == 'Yellow':
                    Bull = Bullet.Bullet(self.x - 5, self.y - 50, 'Ready', 'S')
                    Bull.Bullet = pygame.image.load("yellowbulletS.png").convert_alpha()           
                if Bullet_Color == 'Red':
                    Bull = Bullet.Bullet(self.x - 22 , self.y - 90, 'Ready', 'S')
                    Bull.Bullet = pygame.image.load("redbulletS.png").convert_alpha()          
                if Bullet_Color == 'Blue':
                    Bull = Bullet.Bullet(self.x - 3, self.y - 90, 'Ready', 'S')
                    Bull.Bullet = pygame.image.load("bluebulletS.png").convert_alpha()          
                if Bullet_Color == 'Green':
                    Bull = Bullet.Bullet(self.x - 5, self.y - 90, 'Ready', 'S')
                    Bull.Bullet = pygame.image.load("greenbulletS.png").convert_alpha()
           
            if Bull.Type == 'R':
                if Bullet_Color == 'Yellow':
                    Bull = Bullet.Bullet(self.x - 10, self.y - 60, 'Ready', 'R')
                    Bull.Bullet = pygame.image.load("yellowbulletR.png").convert_alpha()
                if Bullet_Color == 'Red':
                    Bull = Bullet.Bullet(self.x - 30, self.y - 90, 'Ready', 'R')
                    Bull.Bullet = pygame.image.load("redbulletR.png").convert_alpha()
                if Bullet_Color == 'Blue':
                    Bull = Bullet.Bullet(self.x - 20, self.y - 80, 'Ready', 'R')
                    Bull.Bullet = pygame.image.load("bluebulletR.png").convert_alpha()
                if Bullet_Color == 'Green':
                    Bull = Bullet.Bullet(self.x - 20, self.y - 80, 'Ready', 'R')
                    Bull.Bullet = pygame.image.load("greenbulletR.png").convert_alpha()

            if Bull.Type == 'L':
                if Bullet_Color == 'Yellow':
                    Bull = Bullet.Bullet(self.x -40, self.y - 60, 'Ready', 'L')
                    Bull.Bullet = pygame.image.load("yellowbulletL.png").convert_alpha()
                if Bullet_Color == 'Red':
                    Bull = Bullet.Bullet(self.x -70, self.y - 90, 'Ready', 'L')
                    Bull.Bullet = pygame.image.load("redbulletL.png").convert_alpha()
                if Bullet_Color == 'Blue':
                    Bull = Bullet.Bullet(self.x -70, self.y - 90, 'Ready', 'L')
                    Bull.Bullet = pygame.image.load("bluebulletL.png").convert_alpha()
                if Bullet_Color == 'Green':
                    Bull = Bullet.Bullet(self.x -70, self.y - 90, 'Ready', 'L')
                    Bull.Bullet = pygame.image.load("greenbulletL.png").convert_alpha()
        return Bull
    def Shoot(self, Bull, Bullet_Color):
        if Bull.Type == 'S':
            if Bull.Get_y() < 0:
                Bull.Status = 'Free'
                if Bullet_Color == 'Yellow':
                    Bull.Bullet = pygame.image.load("yellowbulletS.png").convert_alpha()           
                if Bullet_Color == 'Red':
                    Bull.Bullet = pygame.image.load("redbulletS.png").convert_alpha()         
                if Bullet_Color == 'Blue':
                    Bull.Bullet = pygame.image.load("bluebulletS.png").convert_alpha()         
                if Bullet_Color == 'Green':
                    Bull.Bullet = pygame.image.load("greenbulletS.png").convert_alpha()     
                Bull.Type = 'S'
                Bull.x = -100
                Bull.y = -100
            if Bull.Get_Status() == 'Ready':
                Bull.y -= 30
                Bull.DisPlayBullet()
        if Bull.Type == 'L':
            if Bull.Get_y() < 0:
                Bull.Status = 'Free'
                if Bullet_Color == 'Yellow':
                    Bull.Bullet = pygame.image.load("yellowbulletL.png").convert_alpha()           
                if Bullet_Color == 'Red':
                    Bull.Bullet = pygame.image.load("redbulletL.png").convert_alpha()         
                if Bullet_Color == 'Blue':
                    Bull.Bullet = pygame.image.load("bluebulletL.png").convert_alpha()         
                if Bullet_Color == 'Green':
                    Bull.Bullet = pygame.image.load("greenbulletL.png").convert_alpha()
                Bull.Type = 'L'
                Bull.x = -100
                Bull.y = -100
            if Bull.Get_Status() == 'Ready':
                Bull.y -= 20
                Bull.x -= 15
                Bull.DisPlayBullet()
        if Bull.Type == 'R':
            if Bull.Get_y() < 0:
                Bull.Status = 'Free'
                if Bullet_Color == 'Yellow':
                    Bull.Bullet = pygame.image.load("yellowbulletR.png").convert_alpha()           
                if Bullet_Color == 'Red':
                    Bull.Bullet = pygame.image.load("redbulletR.png").convert_alpha()         
                if Bullet_Color == 'Blue':
                    Bull.Bullet = pygame.image.load("bluebulletR.png").convert_alpha()         
                if Bullet_Color == 'Green':
                    Bull.Bullet = pygame.image.load("greenbulletR.png").convert_alpha()
                Bull.Type = 'R'
                Bull.x = -100
                Bull.y = -100
            if Bull.Get_Status() == 'Ready':
                Bull.y -= 20
                Bull.x += 15
                Bull.DisPlayBullet()
    def Get_x(self):
        return self.x
    def Get_y (self):
        return self.y



