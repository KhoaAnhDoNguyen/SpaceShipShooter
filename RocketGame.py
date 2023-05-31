import pygame , time, sys
import random
import math
from pygame import mixer
import time
import SpaceShip
import Bullet
import Meteoric
import Aliens
import InterFace

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
#pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)

#mixer.init()

# Create Screen
screen = pygame.display.set_mode((1400, 788))
# Create Caption Game
pygame.display.set_caption("Rocket GamePlay")
# Create Logo
Logo = pygame.image.load("Rocket.png").convert_alpha()
pygame.display.set_icon(Logo)
# FPS
clock = pygame.time.Clock()
# Create BackGround
BackGround = pygame.image.load("bg.png").convert_alpha()
BG_Move_Y = 0
#Create Triple Bullet
powerup = pygame.image.load("lightning.png").convert_alpha()
#Create Live Tree
livetree = pygame.image.load("livetree.png").convert_alpha()
#Create Front
font=pygame.font.SysFont('Arial',32,'bold')
font_stage=pygame.font.SysFont('Arial',100,'bold')
font_gameover=pygame.font.SysFont('Arial',100,'bold')
font_sound = pygame.font.SysFont('Arial', 32, 'bold')
font_SpaceShip = pygame.font.SysFont('Arial', 32, 'bold')
font_Success = pygame.font.SysFont('Arial', 32, 'bold')
#Create Score
Score = 0
#Create Play Button
playbutton = "play.png"
optionbutton = "option.png"
quitbutton = "quit.png"
resumebutton = "resume.png"
pause = "pause.png"
musicon = "musicon.png"
musicoff = "musicoff.png"
backbutton = "back.png"
arcade = "arcade.png"
spaceship = "rocket.png"
spaceship1 = "spaceship1.png"
spaceship2 = "spaceship2.png"
replay = "replay.png"
quitbutton1 = "exit.png"
boom = "boom.png"
lt = "livetree.png"
pu = "lightning.png"
nextleft = "nextleft.png"
nextright = "nextright.png"


def Display_Stage():
    img = font_stage.render(f'STAGE : {Stage}', True, 'red')
    screen.blit(img, (550,300))
def score_text():
    img=font.render(f'Score:{Score}',True,'red')
    screen.blit(img,(10,10))
def GameOver():
    img_gameover = font_gameover.render('GAME OVER . . .', True, 'white')
    screen.blit(img_gameover, (500, 100))
    img_s=font_gameover.render(f'Score: {Score}',True,'red')
    screen.blit(img_s,(400,250))
def Victory():    
    img_s=font_gameover.render(f'Score: {Score}',True,'red')
    screen.blit(img_s,(520,70))
def Draw_BackGround():
    screen.blit(BackGround, (0,BG_Move_Y) )
    screen.blit(BackGround, (0, -788 + BG_Move_Y) )
def Draw_BackGround234():
    screen.blit(BackGround, (0,0) )
def Draw_Sound():
    img = pygame.image.load("soundicon.png").convert_alpha()
    screen.blit(img, (620,140))
def Choose_Spaceship():
    img = font_SpaceShip.render('CHOOSE SPACESHIP : ', True, (236, 236, 236))
    screen.blit(img, (460,530))
def Draw_Success():
    img = font_Success.render('CHOOSE SUCCESSFULLY !!!: ', True, 'yellow')
    screen.blit(img, (800,530))
def Draw_LiveTree(x,y):
    screen.blit(livetree, (int(x),int(y)))
def Draw_PowerUp():
    screen.blit(powerup, (1325, 100))
def Draw_BossBlood(Boss):
    pygame.draw.rect( screen, (255,0,0), [Boss.x + 25,Boss.y -20, 150,10])
    pygame.draw.rect( screen, (255,255,255), [Boss.x + 25,Boss.y -20, 150-Boss.Blood ,10])
def Draw_GameMode(Game_Mode = 'Easy'):
    if Game_Mode == 'Easy':
        img = pygame.image.load("easy.png").convert_alpha()
    if Game_Mode == 'Medium':
        img = pygame.image.load("medium.png").convert_alpha()
    if Game_Mode == 'Hard':
        img = pygame.image.load("Hard.png").convert_alpha()
    screen.blit(img, (730, 450))
    img1 = font_SpaceShip.render('GAME MODE : ', True, (91, 189, 43))
    screen.blit(img1, (350, 465))
def Draw_BulletColor(Bullet_Color = 'Yellow'):
    if Bullet_Color == 'Yellow':
        img = pygame.image.load("yellowbullet.png").convert_alpha()
    if Bullet_Color == 'Red':
        img = pygame.image.load("redbullet.png").convert_alpha()
    if Bullet_Color == 'Blue':
        img = pygame.image.load("bluebullet.png").convert_alpha()
    if Bullet_Color == 'Green':
        img = pygame.image.load("greenbullet.png").convert_alpha()
    screen.blit(img, (690, 220))
    img1 = font_SpaceShip.render('BULLET COLOR : ', True, (249, 244, 0))
    screen.blit(img1, (350, 260))
def Draw_GameControl(Game_Control = 'Both'):
    if Game_Control == 'Mouse':
        img = pygame.image.load("mouse.png").convert_alpha()
        screen.blit(img, (735, 320))
    if Game_Control == 'Keyboard':
        img = pygame.image.load("keyboard.png").convert_alpha()
        screen.blit(img, (698, 300))
    if Game_Control == 'Both':
        img = pygame.image.load("both.png").convert_alpha()
        screen.blit(img, (735, 330))
    img1 = font_SpaceShip.render('GAME CONTROL : ', True, (0, 178, 191))
    screen.blit(img1, (350, 360))


PlayButton = InterFace.InterFace(625, 200, playbutton)
OptionButton = InterFace.InterFace(625, 300, optionbutton)
QuitButton = InterFace.InterFace(625, 400, quitbutton)
ResumeButton = InterFace.InterFace(625, 200, resumebutton)
PauseButton = InterFace.InterFace(1320,10,pause)
SoundStatusOn = InterFace.InterFace(730, 130, musicon)
SoundStatusOff = InterFace.InterFace(730, 130, musicoff)
BackButton = InterFace.InterFace(350, 650, backbutton)
Arcade = InterFace.InterFace(450, 580, arcade)
Rocket1 = InterFace.InterFace(600,580, spaceship)
SpaceShip1 = InterFace.InterFace(750, 580, spaceship1)
SpaceShip2 = InterFace.InterFace(900, 580, spaceship2)
Replay = InterFace.InterFace(380, 500, replay)
ExitButton = InterFace.InterFace(700,500, quitbutton1)
Boom = InterFace.InterFace(-100,-100,boom)
NextLeft = InterFace.InterFace(630, 460, nextleft)
NextRight = InterFace.InterFace(890, 460, nextright)
NextBulletLeft = InterFace.InterFace(630, 250, nextleft)
NextBulletRight = InterFace.InterFace(890, 250, nextright)
NextControlLeft = InterFace.InterFace(630, 350, nextleft)
NextControlRight = InterFace.InterFace(890, 350, nextright)
#GAMEPLAY
Rocket = SpaceShip.SpaceShip(700,680, "spaceship.png")
Bull = Bullet.Bullet()
BullL = Bullet.Bullet()
BullL.Bullet = pygame.image.load("yellowbulletL.png").convert_alpha()
BullL.Type = 'L'
BullR = Bullet.Bullet()
BullL.Bullet = pygame.image.load("yellowbulletR.png").convert_alpha()
BullR.Type = 'R'

#UFO
ListUFO = []
NumUFO = 0
QuantityUFO = 30
for i in range(5):
    A = Aliens.Aliens(x = -100, y = -100, Image = "alien1.png")
    ListUFO.append(A)
ListMeteoric = []
for i in range(5):
    M = Meteoric.Meteoric()
    ListMeteoric.append(M)

#ENEMY
ListEnemy = []
NumEnemy = 0
QuantityEnemy = -1
for i in range(5):
    E = Aliens.Aliens(x = -100, y = -100, Image = "enemy.png")
    ListEnemy.append(E)
ListEnemyBull = []
for i in range(5):
    M = Meteoric.Meteoric(x = -100, y = -100, Meteoric = 'bullet.png', Status = 'Free', Type = 'Straight')
    ListEnemyBull.append(M)

#BOSS
Boss = Aliens.Aliens(x = -100, y = -100, Image = "boss.png") 
BossBullet = Meteoric.Meteoric(x = -100, y = -100, Meteoric = 'bossbulletS1.png', Status = 'Free', Type = 'Straight')

ExplosionMusic = mixer.Sound("explosion.wav")
ExplosionMusic.set_volume(0.8)
LaserMusic = mixer.Sound("laser.wav")
LaserMusic.set_volume(0.8)
LevelPassMusic = mixer.Sound("level.wav")
LevelPassMusic.set_volume(1)

#Time
choose_successfully = pygame.USEREVENT + 1
pygame.time.set_timer(choose_successfully, 2000)

#Live Tree
live_tree = pygame.USEREVENT + 3
time_live_tree = random.randint(5000, 15000)
pygame.time.set_timer(live_tree, time_live_tree)
DropLiveTree = 'No'
LiveTree = InterFace.InterFace(-100, -100, lt)
LiveTreeMusic = mixer.Sound("livetree.wav")

#Power Up
power_up = pygame.USEREVENT + 4
time_power_up = random.randint(5000, 15000)
pygame.time.set_timer(power_up, time_power_up)
DropPowerUp = 'No'
PowerUp = InterFace.InterFace(-100, -100, pu)
PowerUpMusic = mixer.Sound("livetree.wav")
TripleBullet = 'No'

#Time Power Up
time_use_power_up = pygame.USEREVENT + 5
pygame.time.set_timer(time_use_power_up, 10000)

#STAGE
Stage = 1
Stage_Status = 'Yes'
Stage_Event = pygame.USEREVENT + 6
pygame.time.set_timer(Stage_Event, 3500)

#BackGroundMusic = mixer.Sound("background.wav")
#BackGroundMusic.play(-1)
#BackGroundMusic.set_volume(0.3)

Game_Menu = 'Open'
InGame = 'No'
OptionStatus = 'No'
SoundOnOff = 'On'
Choose = 'No'
Game_Over = 'No'
Game_Win = 'No'
Game_Mode = 'Easy'
NumLiveTree = 3
Bullet_Color = 'Yellow'
Game_Control = 'Both'

Running = True
while Running == True:
    
    #Event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
            sys.exit()
        
        if event.type == choose_successfully:
            if Choose == 'Yes':
                Choose = 'No'
        
        if event.type == live_tree:
            if DropLiveTree == 'No':
                DropLiveTree = 'Yes'

        if event.type == power_up:
            if DropPowerUp == 'No':
                DropPowerUp = 'Yes'

        if event.type == time_use_power_up:
            if TripleBullet == 'Yes':
                TripleBullet = 'No'

        if event.type == Stage_Event:
            if Stage_Status == 'Yes':
                Stage_Status = 'No'

    # IF GAMEMENU IS OPEN
    if Game_Menu == 'Open' and InGame == 'No' and OptionStatus == 'No' and Game_Over == 'No':        
        Draw_BackGround()
        BG_Move_Y += 2
        if BG_Move_Y == 790:
            BG_Move_Y = 0
        PlayButton.Draw()
        if PlayButton.Click(Game_Control, Game_Menu, InGame, OptionStatus, Game_Over, Game_Win) == True:
            Game_Menu = 'Close'
            InGame = 'Yes'
            OptionStatus = 'No'
            Game_Over = 'No'
            Stage_Status = 'Yes'
        OptionButton.Draw()
        if OptionButton.Click(Game_Control, Game_Menu, InGame, OptionStatus, Game_Over, Game_Win) == True:
            BackGround = pygame.image.load("bg.png").convert_alpha()
            OptionStatus = 'Yes'
            Game_Menu = 'Close'
        QuitButton.Draw()
        if QuitButton.Click(Game_Control, Game_Menu, InGame, OptionStatus, Game_Over, Game_Win) == True:
            Running = False
            sys.exit()

    # GAMEMENU IN GAME
    elif Game_Menu == 'Open' and InGame == 'Yes' and OptionStatus == 'No' and Game_Over == 'No':
        Draw_BackGround()
        BG_Move_Y += 2
        if BG_Move_Y == 790:
            BG_Move_Y = 0
        ResumeButton.Draw()
        if ResumeButton.Click(Game_Control, Game_Menu, InGame, OptionStatus, Game_Over, Game_Win) == True:
            if Stage == 2:
                BackGround = pygame.image.load("bg2.png").convert_alpha()
            if Stage == 3:
                BackGround = pygame.image.load("bg3.png").convert_alpha()
            if Stage == 4:
                BackGround = pygame.image.load("bg4.png").convert_alpha()
            Game_Menu = 'Close'
            InGame = 'Yes'
        OptionButton.Draw()
        if OptionButton.Click(Game_Control, Game_Menu, InGame, OptionStatus, Game_Over, Game_Win) == True:
            BackGround = pygame.image.load("bg.png").convert_alpha()
            OptionStatus = 'Yes'
            Game_Menu = 'Close'
        QuitButton.Draw()
        if QuitButton.Click(Game_Control, Game_Menu, InGame, OptionStatus, Game_Over, Game_Win) == True:
            Running = False
            sys.exit()
    
     #Stage
    elif Stage_Status == 'Yes' and InGame == 'Yes':
        if Stage == 1:
            Draw_BackGround()
            BG_Move_Y += 2
            if BG_Move_Y == 790:
                BG_Move_Y = 0
            Display_Stage()
        else:
            TripleBullet = 'No'
            LevelPassMusic.play()
            if Stage == 2:
                BackGround = pygame.image.load("bg2.png").convert_alpha()
            if Stage == 3:
                BackGround = pygame.image.load("bg3.png").convert_alpha()
            if Stage == 4:
                BackGround = pygame.image.load("bg4.png").convert_alpha()
            Draw_BackGround234()
            Display_Stage()

    #PLAY
    elif Game_Menu == 'Close' and InGame == 'Yes' and OptionStatus == 'No' and Game_Over == 'No' and Stage_Status == 'No':      
        # ADD BG AND DISPLAY
        if Stage == 1:
            Draw_BackGround()
            BG_Move_Y += 2
            if BG_Move_Y == 790:
                BG_Move_Y = 0
        else:
            Draw_BackGround234()

        # Draw Live Tree
        for i in range(NumLiveTree):
            Draw_LiveTree(10+i*50, 50)

        # Drop Live Tree
        if DropLiveTree == 'Yes':
            LiveTree.x = random.randint(10,1300)
            LiveTree.y = 0
            DropLiveTree = 'No'
        LiveTree.y += 3
        LiveTree.Draw()
       
        #Colision Rocket and LiveTree
        distance = math.sqrt( (( Rocket.Get_x() - LiveTree.x )**2) + (( Rocket.Get_y() - LiveTree.y )**2) )
        if distance <= 40:
            LiveTreeMusic.play()
            Score += 3
            LiveTree = InterFace.InterFace(-100, -100, lt)
            LiveTree.Draw()
            if NumLiveTree <= 2 and NumLiveTree > 0:
                NumLiveTree += 1

        # Drop Power up
        if DropPowerUp == 'Yes':
            PowerUp.x = random.randint(10,1300)
            PowerUp.y = 0 
            DropPowerUp = 'No'
        PowerUp.y += 3
        PowerUp.Draw()

        # Colision Rocket and PowerUp
        distance = math.sqrt( (( Rocket.Get_x() - PowerUp.x )**2) + (( Rocket.Get_y() - PowerUp.y )**2) )
        if distance <= 40:
            PowerUpMusic.play()
            Score += 5
            PowerUp = InterFace.InterFace(-100, -100, pu)
            PowerUp.Draw()
            TripleBullet = 'Yes'

        # Draw Tripe Bullet
        if TripleBullet == 'Yes':
            Draw_PowerUp()

        # Create Rocket and move
        Rocket.MoveRocket(Game_Control)
        Rocket.DisPlayRocket()

        #Create UFO
        if Stage == 1 or Stage == 3 or Stage == 4:
            if NumUFO > QuantityUFO:
                for i in range(5):
                    if ListUFO[i].Status == 'Live':
                        ListUFO[i].DisPlayAliens()
                    elif  ListUFO[i].Status == 'Die':
                        ListUFO[i].x = -100
                        ListUFO[i].UFO = pygame.image.load("alien1.png").convert_alpha()
            else:
                for i in range(5):
                    if ListUFO[i].Status == 'Die':
                        ListUFO[i].x = -100
                        ListUFO[i].UFO = pygame.image.load("alien1.png").convert_alpha()
                        ListUFO[i].Status = 'Live'
                    ListUFO[i].DisPlayAliens()
          
        #Create Enenmy
        if Stage == 2 or Stage == 3 or Stage == 4:
            if NumEnemy > QuantityEnemy:
                for i in range(5):
                    if ListEnemy[i].Status == 'Live':
                        ListEnemy[i].DisPlayAliens()
                    elif ListEnemy[i].Status == 'Die':
                        ListEnemy[i].x = -100
                        ListEnemy[i].UFO = pygame.image.load("enemy.png").convert_alpha()
            else:
                for i in range(5):
                    if ListEnemy[i].Status == 'Die':
                        ListEnemy[i].x = -100
                        ListEnemy[i].UFO = pygame.image.load("enemy.png").convert_alpha()
                        ListEnemy[i].Status = 'Live'
                    ListEnemy[i].DisPlayAliens()
       
        #Create Boss   
        if Stage == 4:         
            Boss.DisPlayAliens()
            Draw_BossBlood(Boss)

        #Game_Mode
        for i in range(5):
            if Game_Mode == 'Easy':
                ListMeteoric[i].velocityMeteoric = 3
                ListEnemyBull[i].velocityMeteoric = 3
                BossBullet.velocityMeteoric = 3
            elif Game_Mode == 'Medium':
                ListMeteoric[i].velocityMeteoric = 4
                ListEnemyBull[i].velocityMeteoric = 4
                BossBullet.velocityMeteoric = 4
            else:
                ListMeteoric[i].velocityMeteoric = 5
                ListEnemyBull[i].velocityMeteoric = 5
                BossBullet.velocityMeteoric = 5
         
        #Bullet Shoot
        if Game_Control == 'Both':
            Mouse = pygame.mouse.get_pressed()
            Button = pygame.key.get_pressed()
            if (Button[pygame.K_SPACE] or Mouse[0]) and TripleBullet == 'No':
                if Bull.Get_Status() == 'Free':
                    Bull = Rocket.PrepareBullet(Bull, Bullet_Color)
                    LaserMusic.play()
                Rocket.Shoot(Bull, Bullet_Color)
            if (Button[pygame.K_SPACE] or Mouse[0]) and TripleBullet == 'Yes':
                LaserMusic.play()
                if Bull.Get_Status() == 'Free':
                    Bull = Rocket.PrepareBullet(Bull, Bullet_Color)              
                if BullL.Get_Status() == 'Free':
                    BullL = Rocket.PrepareBullet(BullL, Bullet_Color)          
                if BullR.Get_Status() == 'Free':
                    BullR = Rocket.PrepareBullet(BullR, Bullet_Color)
                if Bull.Get_Status() == 'Ready' and BullL.Get_Status() == 'Ready' and BullR.Get_Status() == 'Ready':
                    Rocket.Shoot(Bull, Bullet_Color)
                    Rocket.Shoot(BullL, Bullet_Color)
                    Rocket.Shoot(BullR, Bullet_Color)
        if Game_Control == 'Keyboard':
            Button = pygame.key.get_pressed()
            if (Button[pygame.K_SPACE]) and TripleBullet == 'No':
                if Bull.Get_Status() == 'Free':
                    Bull = Rocket.PrepareBullet(Bull, Bullet_Color)
                    LaserMusic.play()
                Rocket.Shoot(Bull, Bullet_Color)
            if (Button[pygame.K_SPACE]) and TripleBullet == 'Yes':
                LaserMusic.play()
                if Bull.Get_Status() == 'Free':
                    Bull = Rocket.PrepareBullet(Bull, Bullet_Color)              
                if BullL.Get_Status() == 'Free':
                    BullL = Rocket.PrepareBullet(BullL, Bullet_Color)          
                if BullR.Get_Status() == 'Free':
                    BullR = Rocket.PrepareBullet(BullR, Bullet_Color)
                if Bull.Get_Status() == 'Ready' and BullL.Get_Status() == 'Ready' and BullR.Get_Status() == 'Ready':
                    Rocket.Shoot(Bull, Bullet_Color)
                    Rocket.Shoot(BullL, Bullet_Color)
                    Rocket.Shoot(BullR, Bullet_Color)
        if Game_Control == 'Mouse':            
            Mouse = pygame.mouse.get_pressed()
            if (Mouse[0]) and TripleBullet == 'No':
                if Bull.Get_Status() == 'Free':
                    Bull = Rocket.PrepareBullet(Bull, Bullet_Color)
                    LaserMusic.play()
                Rocket.Shoot(Bull, Bullet_Color)
            if (Mouse[0]) and TripleBullet == 'Yes':
                LaserMusic.play()
                if Bull.Get_Status() == 'Free':
                    Bull = Rocket.PrepareBullet(Bull, Bullet_Color)              
                if BullL.Get_Status() == 'Free':
                    BullL = Rocket.PrepareBullet(BullL, Bullet_Color)          
                if BullR.Get_Status() == 'Free':
                    BullR = Rocket.PrepareBullet(BullR, Bullet_Color)
                if Bull.Get_Status() == 'Ready' and BullL.Get_Status() == 'Ready' and BullR.Get_Status() == 'Ready':
                    Rocket.Shoot(Bull, Bullet_Color)
                    Rocket.Shoot(BullL, Bullet_Color)
                    Rocket.Shoot(BullR, Bullet_Color)
        if Stage == 4:
        #Create Bullet Boss
            #PREPARE
            BossBullet = Boss.PrepareMeteoric(BossBullet, Rocket, StraightI = 'bossbulletS1.png' ,LeftI = 'bossbulletL1.png', RightI = 'bossbulletR1.png' )
            #Shoot
            Boss.Shoot(BossBullet, Rocket)

        #Create Meteoric UFO
            #PREPARE
        for i in range(5):
            ListMeteoric[i] = ListUFO[i].PrepareMeteoric(ListMeteoric[i], Rocket, StraightI = 'meteoricS.png' ,LeftI = 'meteoricL.png', RightI = 'meteoricR.png')           
            #Shoot
        if NumUFO <= QuantityUFO:
            for i in range(5):
                ListUFO[i].Shoot(ListMeteoric[i], Rocket)
        else:
            for i in range(5):
                ListUFO[i].Shoot(ListMeteoric[i], Rocket)

        #Create Meteoric Enemy
            #PREPARE
        for i in range(5):
            ListEnemyBull[i] = ListEnemy[i].PrepareMeteoric(ListEnemyBull[i], Rocket, StraightI = 'bullet.png' ,LeftI = 'bulletL.png', RightI = 'bulletR.png')
            #Shoot
        if NumEnemy <= QuantityEnemy:
            for i in range(5):
                ListEnemy[i].Shoot(ListEnemyBull[i], Rocket)
        else:
            for i in range(5):
                ListEnemy[i].Shoot(ListEnemyBull[i], Rocket)
           
        #Check Colision Bullet and Aliens   
        for i in range(5):
            if TripleBullet == 'No':
                distance_UFO = math.sqrt( (( Bull.Get_x() - ListUFO[i].Get_x() )**2) + (( Bull.Get_y() - ListUFO[i].Get_y() )**2) )
                distance_Enemy = math.sqrt( (( Bull.Get_x() - ListEnemy[i].Get_x() )**2) + (( Bull.Get_y() - ListEnemy[i].Get_y() )**2) )
                #UFO
                if distance_UFO < 40 and Bull.Get_y() >= 0 and Bull.Get_y() <= 788 and ListUFO[i].x >= 0 and ListUFO[i].x <= 1400 and ListUFO[i].Status == 'Live':
                    ExplosionMusic.play()
                    Bull.x, Bull.y = -100, -100
                    Score += 1
                    ListUFO[i].Status = 'Die'
                    NumUFO += 1
                    print(Stage, 'UFO: ', NumUFO)
                # Enemy
                if distance_Enemy < 40 and Bull.Get_y() >= 0 and Bull.Get_y() <= 788 and ListEnemy[i].x >= 0 and ListEnemy[i].x <= 1400 and ListEnemy[i].Status == 'Live':
                    ExplosionMusic.play()
                    Bull.x, Bull.y = -100, -100
                    Score += 1
                    ListEnemy[i].Status = 'Die'
                    NumEnemy += 1
                    print(Stage, 'Enemy: ', NumEnemy)

            else:
                distance_UFO = math.sqrt( (( Bull.Get_x() - ListUFO[i].Get_x() )**2) + (( Bull.Get_y() - ListUFO[i].Get_y() )**2) )
                distanceL_UFO = math.sqrt( (( BullL.Get_x() - ListUFO[i].Get_x() )**2) + (( BullL.Get_y() - ListUFO[i].Get_y() )**2) )
                distanceR_UFO = math.sqrt( (( BullR.Get_x() - ListUFO[i].Get_x() )**2) + (( BullR.Get_y() - ListUFO[i].Get_y() )**2) )

                distance_Enemy = math.sqrt( (( Bull.Get_x() - ListEnemy[i].Get_x() )**2) + (( Bull.Get_y() - ListEnemy[i].Get_y() )**2) )
                distanceL_Enemy = math.sqrt( (( BullL.Get_x() - ListEnemy[i].Get_x() )**2) + (( BullL.Get_y() - ListEnemy[i].Get_y() )**2) )
                distanceR_Enemy = math.sqrt( (( BullR.Get_x() - ListEnemy[i].Get_x() )**2) + (( BullR.Get_y() - ListEnemy[i].Get_y() )**2) )
                #UFO
                if distance_UFO < 40   and Bull.Get_y() > 0 and Bull.Get_y() <= 788 and ListUFO[i].x >= 0 and ListUFO[i].x <= 1400 and ListUFO[i].Status == 'Live' and ListUFO[i].y >= 0 and ListUFO[i].y <= 788:
                    ExplosionMusic.play()
                    Bull.x, Bull.y = -100, -100
                    Score += 1
                    ListUFO[i].Status = 'Die'
                    NumUFO += 1
                    print(Stage, 'UFO: ', NumUFO)
                elif distanceL_UFO < 40   and BullL.Get_y() > 0 and Bull.Get_y() <= 788 and ListUFO[i].x >= 0 and ListUFO[i].x <= 1400 and ListUFO[i].Status == 'Live' and ListUFO[i].y >= 0 and ListUFO[i].y <= 788:
                    ExplosionMusic.play()
                    BullL.x, BullL.y = -100, -100
                    Score += 1
                    ListUFO[i].Status = 'Die'
                    NumUFO += 1
                    print(Stage, 'UFO: ', NumUFO)
                elif distanceR_UFO < 40   and BullR.Get_y() > 0 and Bull.Get_y() <= 788 and ListUFO[i].x >= 0 and ListUFO[i].x <= 1400 and ListUFO[i].Status == 'Live' and ListUFO[i].y >= 0 and ListUFO[i].y <= 788:
                    ExplosionMusic.play()
                    BullR.x, BullR.y = -100, -100
                    Score += 1
                    ListUFO[i].Status = 'Die'
                    NumUFO += 1
                    print(Stage, 'UFO: ', NumUFO)

                #ENEMY
                if distance_Enemy < 40   and Bull.Get_y() > 0 and Bull.Get_y() <= 788 and ListEnemy[i].x >= 0 and ListEnemy[i].x <= 1400 and ListEnemy[i].Status == 'Live' and ListEnemy[i].y >= 0 and ListEnemy[i].y <= 788:
                    ExplosionMusic.play()
                    Bull.x, Bull.y = -100, -100
                    Score += 1
                    ListEnemy[i].Status = 'Die'
                    NumEnemy += 1
                    print(Stage, 'Enemy: ', NumEnemy)
                elif distanceL_Enemy < 40   and BullL.Get_y() > 0 and Bull.Get_y() <= 788 and ListEnemy[i].x >= 0 and ListEnemy[i].x <= 1400 and ListEnemy[i].Status == 'Live' and ListEnemy[i].y >= 0 and ListEnemy[i].y <= 788:
                    ExplosionMusic.play()
                    BullL.x, BullL.y = -100, -100
                    Score += 1
                    ListEnemy[i].Status = 'Die'
                    NumEnemy += 1
                    print(Stage, 'Enemy: ', NumEnemy)
                elif distanceR_Enemy < 40   and BullR.Get_y() > 0 and Bull.Get_y() <= 788 and ListEnemy[i].x >= 0 and ListEnemy[i].x <= 1400 and ListEnemy[i].Status == 'Live' and ListEnemy[i].y >= 0 and ListEnemy[i].y <= 788:
                    ExplosionMusic.play()
                    BullR.x, BullR.y = -100, -100
                    Score += 1
                    ListEnemy[i].Status = 'Die'
                    NumEnemy += 1
                    print(Stage, 'Enemy: ', NumEnemy)
        
        #Check Colision Bullet and Boss
        if TripleBullet == 'No':
            distance_Boss = math.sqrt( (( Bull.Get_x() - Boss.Get_x() )**2) + (( Bull.Get_y() - Boss.Get_y() )**2) )
            if distance_Boss <= 80 and Bull.x >= 0 and Bull.y <= 1400 and Bull.y >= 0 and Bull.y <= 788:
                Boss.Blood -= 5
                Bull.x = -100
                Bull.y = -100
        elif TripleBullet == 'Yes':
            distance_Boss = math.sqrt( (( Bull.Get_x() - Boss.Get_x() )**2) + (( Bull.Get_y() - Boss.Get_y() )**2) )
            distance_Boss_L = math.sqrt( (( BullL.Get_x() - Boss.Get_x() )**2) + (( BullL.Get_y() - Boss.Get_y() )**2) )
            distance_Boss_R = math.sqrt( (( BullR.Get_x() - Boss.Get_x() )**2) + (( BullR.Get_y() - Boss.Get_y() )**2) )
            if distance_Boss <= 80 and Bull.x >= 0 and Bull.y <= 1400 and Bull.y >= 0 and Bull.y <= 788:
                Boss.Blood -= 5
                Bull.x = -100
                Bull.y = -100
            elif distance_Boss_L <= 80 and BullL.x >= 0 and BullL.y <= 1400 and BullL.y >= 0 and BullL.y <= 788:
                Boss.Blood -= 5
                BullL.x = -100
                BullL.y = -100
            elif distance_Boss_R <= 80 and BullR.x >= 0 and BullR.y <= 1400 and BullR.y >= 0 and BullR.y <= 788:
                Boss.Blood -= 5
                BullR.x = -100
                BullR.y = -100
        if Boss.Blood < 0 and Boss.x >= 0 and Boss.x <= 1400 and Boss.y > 0 and Boss.y < 788:
             #ExplosionMusic.play()
             print("Boss")

        #Check Win
        check = 0
        for i in range(5):
            if ListUFO[i].Status == 'Live' or ListEnemy[i].Status == 'Live':
                check = 1
        if Boss.Blood < 0 and Stage == 4 and check == 0:
            #LevelPassMusic.play()
            Game_Win = 'Yes'
            BackGround = pygame.image.load("victory.png").convert_alpha()
        elif Boss.Blood < 0 and check == 1:
            Boss.y = -100
            Boss.Status = 'Die'

        #Display Score
        score_text()

        #Check Colision Meteorics and Spaceship
        for i in range(5):
            #UFO
            if ListMeteoric[i].Get_x() >= 0 and ListMeteoric[i].Get_x() <= 1400 and ListMeteoric[i].Get_y() >=0 and ListMeteoric[i].Get_y() <= 788:
                distance_UFO_C = math.sqrt( ((Rocket.Get_x() - ListMeteoric[i].Get_x())**2) + (( Rocket.Get_y() - ListMeteoric[i].Get_y())**2) )
                if distance_UFO_C < 30 and ListUFO[i].Status == 'Live':
                    ExplosionMusic.play()
                    NumLiveTree -= 1
                    ListMeteoric[i].x = -100
                    ListMeteoric[i].y = -100
                    #ListMeteoric[i] = Meteoric(x = -100, y = -100, Meteoric = 'meteoricS.png', Status = 'Free', Type = 'Straight')
                    if NumLiveTree == 0:
                        Game_Over = 'Yes'
                        BackGround = pygame.image.load("bg.png").convert_alpha()

            #Enemy
            if ListEnemyBull[i].Get_x() >= 0 and ListEnemyBull[i].Get_x() <= 1400 and ListEnemyBull[i].Get_y() >=0 and ListEnemyBull[i].Get_y() <= 788:
                distance_Enemy_C = math.sqrt( ((Rocket.Get_x() - ListEnemyBull[i].Get_x())**2) + (( Rocket.Get_y() - ListEnemyBull[i].Get_y())**2) )
                if distance_Enemy_C < 30 and ListEnemy[i].Status == 'Live':
                    ExplosionMusic.play()
                    NumLiveTree -= 1
                    ListEnemyBull[i].x = -100
                    ListEnemyBull[i].y = -100
                    #ListEnemyBull[i] = Meteoric(x = -100, y = -100, Meteoric = 'bullet.png', Status = 'Free', Type = 'Straight')
                    if NumLiveTree == 0:
                        Game_Over = 'Yes'
                        BackGround = pygame.image.load("bg.png").convert_alpha()
        #Check Colision Spaceship and Boss Bullet
        if Stage == 4:
            if BossBullet.Get_x() >= 0 and BossBullet.Get_x() <= 1400 and BossBullet.Get_y() >=0 and BossBullet.Get_y() <= 788:
                distance = math.sqrt( ((Rocket.Get_x() - BossBullet.Get_x())**2) + (( Rocket.Get_y() - BossBullet.Get_y())**2) )
                if distance < 60 and Boss.Status == 'Live':
                    ExplosionMusic.play()
                    NumLiveTree -= 1
                    BossBullet.x = -100
                    BossBullet.y = -100
                    if NumLiveTree == 0:
                        Game_Over = 'Yes'
                        BackGround = pygame.image.load("bg.png").convert_alpha()
        #Stage Switch
        check = 0
        if Stage == 1 and NumUFO > QuantityUFO : # Up to Stage 2
            for i in range(5):
                if ListUFO[i].Status == 'Live':
                    check = 1
            if check == 0:
                Stage += 1
                NumUFO = 0
                NumEnemy = 0
                QuantityEnemy = 30
                Stage_Status = 'Yes'
                for i in range(5):
                    ListMeteoric[i].x = -100
                    ListMeteoric[i].y = -100
                    ListEnemyBull[i].x = -100
                    ListEnemyBull[i].y = -100
        elif Stage == 2 and  NumEnemy > QuantityEnemy: # Up to Stage 3
            check = 0
            for i in range(5):
                if ListEnemy[i].Status == 'Live':
                    check = 1
            if check == 0:
                Stage += 1
                NumUFO = 0
                NumEnemy = 0
                QuantityUFO = 30
                QuantityEnemy = 30
                Stage_Status = 'Yes'
                for i in range(5):
                    ListMeteoric[i].x = -100
                    ListMeteoric[i].y = -100
                    ListEnemyBull[i].x = -100
                    ListEnemyBull[i].y = -100
        elif Stage == 3 and NumUFO > QuantityUFO and NumEnemy > QuantityEnemy: #Up to Stage 4
            check =0
            for i in range(5):
                if ListUFO[i].Status == 'Live' or ListEnemy[i].Status == 'Live':
                    check = 1
            if check == 0:
                Stage += 1
                NumUFO = 0
                NumEnemy = 0
                QuantityUFO = 35
                QuantityEnemy = 35
                Stage_Status = 'Yes'
                for i in range(5):
                    ListMeteoric[i].x = -100
                    ListMeteoric[i].y = -100
                    ListEnemyBull[i].x = -100
                    ListEnemyBull[i].y = -100

        #Pause Click
        PauseButton.Draw()
        Button = pygame.key.get_pressed()
        if PauseButton.Click(Game_Control, Game_Menu, InGame, OptionStatus, Game_Over, Game_Win) or Button[pygame.K_ESCAPE]:
            BackGround = pygame.image.load("bg.png").convert_alpha()
            Game_Menu = 'Open'
            InGame = 'Yes'

    #Open Option
    elif  Game_Menu == 'Close' and  Game_Over == 'No' and OptionStatus == 'Yes':
        #BackGround
        Draw_BackGround()
        BG_Move_Y += 2
        if BG_Move_Y == 790:
            BG_Move_Y = 0
        #Sound
        Draw_Sound()
        if SoundOnOff == 'On':
            SoundStatusOn.Draw()
            if SoundStatusOn.Click(Game_Control, Game_Menu, InGame, OptionStatus, Game_Over, Game_Win):
                SoundOnOff = 'Off'
                SoundStatusOff.Draw()
                ExplosionMusic.set_volume(0.0)
                LaserMusic.set_volume(0.0)
                #BackGroundMusic.set_volume(0.0)
                LiveTreeMusic.set_volume(0.0)
                PowerUpMusic.set_volume(0.0)
                LevelPassMusic.set_volume(0.0)
        if SoundOnOff == 'Off':
            SoundStatusOff.Draw()
            if SoundStatusOff.Click(Game_Control, Game_Menu, InGame, OptionStatus, Game_Over, Game_Win):
                SoundOnOff = 'On'
                SoundStatusOn.Draw()
                ExplosionMusic.set_volume(0.8)
                LaserMusic.set_volume(0.8)
                #BackGroundMusic.set_volume(0.8)
                LiveTreeMusic.set_volume(1.0)
                PowerUpMusic.set_volume(1.0)
                LevelPassMusic.set_volume(1.0)
        #Back
        BackButton.Draw()
        if BackButton.Click(Game_Control, Game_Menu, InGame, OptionStatus, Game_Over, Game_Win):
            Game_Menu = 'Open'
            OptionStatus = 'No'

        #Choose Spaceship Bullet
        NextBulletLeft.Draw()
        NextBulletRight.Draw()
        Draw_BulletColor(Bullet_Color)
        if Bullet_Color == 'Yellow' and NextBulletLeft.Click(Game_Control, Game_Menu, InGame, OptionStatus, Game_Over, Game_Win) :
            Bullet_Color = 'Green'
        if Bullet_Color == 'Yellow' and NextBulletRight.Click(Game_Control, Game_Menu, InGame, OptionStatus, Game_Over, Game_Win) :
            Bullet_Color = 'Red'
        if Bullet_Color == 'Red' and NextBulletLeft.Click(Game_Control, Game_Menu, InGame, OptionStatus, Game_Over, Game_Win) :
            Bullet_Color = 'Yellow'
        if Bullet_Color == 'Red' and NextBulletRight.Click(Game_Control, Game_Menu, InGame, OptionStatus, Game_Over, Game_Win) :
            Bullet_Color = 'Blue'
        if Bullet_Color == 'Blue' and NextBulletLeft.Click(Game_Control, Game_Menu, InGame, OptionStatus, Game_Over, Game_Win) :
            Bullet_Color = 'Red'
        if Bullet_Color == 'Blue' and NextBulletRight.Click(Game_Control, Game_Menu, InGame, OptionStatus, Game_Over, Game_Win) :
            Bullet_Color = 'Green'
        if Bullet_Color == 'Green' and NextBulletLeft.Click(Game_Control, Game_Menu, InGame, OptionStatus, Game_Over, Game_Win) :
            Bullet_Color = 'Blue'
        if Bullet_Color == 'Green' and NextBulletRight.Click(Game_Control, Game_Menu, InGame, OptionStatus, Game_Over, Game_Win) :
            Bullet_Color = 'Yellow'
        
        #Choose Game Control
        NextControlLeft.Draw()
        NextControlRight.Draw()
        Draw_GameControl(Game_Control)
        if Game_Control == 'Mouse' and NextControlRight.Click(Game_Control, Game_Menu, InGame, OptionStatus, Game_Over, Game_Win):
            Game_Control = 'Keyboard'
        if Game_Control == 'Mouse' and NextControlLeft.Click(Game_Control, Game_Menu, InGame, OptionStatus, Game_Over, Game_Win):
            Game_Control = 'Both'
        if Game_Control == 'Keyboard' and NextControlRight.Click(Game_Control, Game_Menu, InGame, OptionStatus, Game_Over, Game_Win):
            Game_Control = 'Both'
        if Game_Control == 'Keyboard' and NextControlLeft.Click(Game_Control, Game_Menu, InGame, OptionStatus, Game_Over, Game_Win):
            Game_Control = 'Mouse'
        if Game_Control == 'Both' and NextControlRight.Click(Game_Control, Game_Menu, InGame, OptionStatus, Game_Over, Game_Win):
            Game_Control = 'Mouse'
        if Game_Control == 'Both' and NextControlLeft.Click(Game_Control, Game_Menu, InGame, OptionStatus, Game_Over, Game_Win):
            Game_Control = 'Keyboard'

        #Choose Spaceship  
        if InGame == 'No':
            Choose_Spaceship()
            Arcade.Draw()
            Rocket1.Draw()
            SpaceShip1.Draw()
            SpaceShip2.Draw()
            if Arcade.Click(Game_Control, Game_Menu, InGame, OptionStatus, Game_Over, Game_Win):
                Choose = 'Yes'
                Rocket = SpaceShip.SpaceShip(700,680, "arcade.png")
            if Rocket1.Click(Game_Control, Game_Menu, InGame, OptionStatus, Game_Over, Game_Win):
                Choose = 'Yes'               
                Rocket = SpaceShip.SpaceShip(700,680, "spaceship.png")
            if Choose == 'Yes':
                Draw_Success()
            if SpaceShip1.Click(Game_Control, Game_Menu, InGame, OptionStatus, Game_Over, Game_Win):
                Choose = 'Yes'
                Rocket = SpaceShip.SpaceShip(700,680, "spaceship1.png")
            if SpaceShip2.Click(Game_Control, Game_Menu, InGame, OptionStatus, Game_Over, Game_Win):
                Choose = 'Yes'
                Rocket = SpaceShip.SpaceShip(700,680, "spaceship2.png")
            NextLeft.Draw()
            NextRight.Draw()
            Draw_GameMode(Game_Mode)
            if Game_Mode == 'Easy' and NextRight.Click(Game_Control, Game_Menu, InGame, OptionStatus, Game_Over, Game_Win):
                Game_Mode = 'Medium'
            if Game_Mode == 'Easy' and NextLeft.Click(Game_Control, Game_Menu, InGame, OptionStatus, Game_Over, Game_Win):
                Game_Mode = 'Hard'
            if Game_Mode == 'Medium' and NextRight.Click(Game_Control, Game_Menu, InGame, OptionStatus, Game_Over, Game_Win):
                Game_Mode = 'Hard'
            if Game_Mode == 'Medium' and NextLeft.Click(Game_Control, Game_Menu, InGame, OptionStatus, Game_Over, Game_Win):
                Game_Mode = 'Easy'
            if Game_Mode == 'Hard' and NextRight.Click(Game_Control, Game_Menu, InGame, OptionStatus, Game_Over, Game_Win):
                Game_Mode = 'Easy'
            if Game_Mode == 'Hard' and NextLeft.Click(Game_Control, Game_Menu, InGame, OptionStatus, Game_Over, Game_Win):
                Game_Mode = 'Medium'
            
    #Game Over
    elif Game_Over == 'Yes' :
        Draw_BackGround()
        BG_Move_Y += 2
        if BG_Move_Y == 790:
            BG_Move_Y = 0
        GameOver()
        Replay.Draw()
        ExitButton.Draw()
        if Replay.Click(Game_Control, Game_Menu, InGame, OptionStatus, Game_Over, Game_Win):          
            Score = 0
            Game_Menu = 'Open'
            InGame = 'No'
            OptionStatus = 'No'
            Game_Over = 'No'
            Stage = 1
            Stage_Status = 'Yes'
            #UFO
            NumUFO = 0
            QuantityUFO = 10
            ListUFO = []
            for i in range(5):
                A = Aliens.Aliens(x = -100, y = -100, Image = "alien1.png")
                ListUFO.append(A)
            ListMeteoric = []
            for i in range(5):              
                M = Meteoric.Meteoric()
                ListMeteoric.append(M)
            #ENEMY
            ListEnemy = []
            NumEnemy = 0
            QuantityEnemy = -1
            for i in range(5):
                E = Aliens.Aliens(x = -100, y = -100, Image = "enemy.png")
                ListEnemy.append(E)
            ListEnemyBull = []
            for i in range(5):
                M = Meteoric.Meteoric(x = -100, y = -100, Meteoric = 'bullet.png', Status = 'Free', Type = 'Straight')
                ListEnemyBull.append(M)
            #BOSS
            Boss = Aliens.Aliens(x = -100, y = -100, Image = "boss.png")
            Rocket = SpaceShip.SpaceShip(700,680, "spaceship.png")
            Bull = Rocket.PrepareBullet(Bull, Bullet_Color)
            NumLiveTree = 3           
        if ExitButton.Click(Game_Control, Game_Menu, InGame, OptionStatus, Game_Over, Game_Win):
            Running = False
            sys.exit()
    
    #Game win
    if Game_Win == 'Yes' :
        Draw_BackGround234()
        Victory()
        Replay.Draw()
        ExitButton.Draw()
        if Replay.Click(Game_Control, Game_Menu, InGame, OptionStatus, Game_Over, Game_Win):          
            Score = 0
            Game_Menu = 'Open'
            InGame = 'No'
            OptionStatus = 'No'
            Game_Win = 'No'
            Stage = 1
            Stage_Status = 'Yes'
            BackGround = pygame.image.load("bg.png").convert_alpha()
            #UFO
            NumUFO = 0
            QuantityUFO = 10
            ListUFO = []
            for i in range(5):
                A = Aliens.Aliens(x = -100, y = -100, Image = "alien1.png")
                ListUFO.append(A)
            ListMeteoric = []
            for i in range(5):              
                M = Meteoric.Meteoric()
                ListMeteoric.append(M)
            #ENEMY
            ListEnemy = []
            NumEnemy = 0
            QuantityEnemy = -1
            for i in range(5):
                E = Aliens.Aliens(x = -100, y = -100, Image = "enemy.png")
                ListEnemy.append(E)
            ListEnemyBull = []
            for i in range(5):
                M = Meteoric.Meteoric(x = -100, y = -100, Meteoric = 'bullet.png', Status = 'Free', Type = 'Straight')
                ListEnemyBull.append(M)
            #BOSS
            Boss = Aliens.Aliens(x = -100, y = -100, Image = "boss.png")
            Rocket = SpaceShip.SpaceShip(700,680, "spaceship.png")
            Bull = Rocket.PrepareBullet(Bull, Bullet_Color)
            NumLiveTree = 3          
        if ExitButton.Click(Game_Control, Game_Menu, InGame, OptionStatus, Game_Over, Game_Win):
            Running = False
            sys.exit()

    #FPS frame per second
    clock.tick(120)
    pygame.display.update()