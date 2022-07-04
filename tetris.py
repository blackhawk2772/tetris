import pygame
from pygame.locals import *
import random
import copy


pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 40)
pygame.mixer.music.load("resources/99.mp3")
bg = pygame.image.load("resources/bg.jpg")
width = 1920
height = 1080
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tetris")

BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
ORANGE = (255,165,00)

clock = pygame.time.Clock()
PLAYER_SPEED = 15
running = True
nextShape = 0
rotation=0
activeBlocks = [None,None,None,None]
nextBlocks = [None,None,None,None]
staticBlocks = [None] *20*10


class block:
    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        self.color = color

def spawn():
    global nextShape
    global rotation
    #te
    rotation = 0
    if (nextShape == 0):
        block0 = block(width/2+2,53,CYAN)
        block1 = block(width/2+2,53+48,CYAN)
        block2 = block(width/2+2-48,53+48,CYAN)
        block3 = block(width/2+2+48,53+48,CYAN)    
    #square
    elif (nextShape == 1):
        block0 = block(width/2+2,53,BLUE)
        block1 = block(width/2+2,53+48,BLUE)
        block2 = block(width/2+2-48,53+48,BLUE)
        block3 = block(width/2+2-48,53,BLUE)
    #zetal
    elif (nextShape == 2):
        block0 = block(width/2+2,53,ORANGE)
        block1 = block(width/2+2-48,53,ORANGE)
        block2 = block(width/2+2,53+48,ORANGE)
        block3 = block(width/2+2+48,53+48,ORANGE)
    #zetar
    elif (nextShape == 3):
        block0 = block(width/2+2,53,GREEN)
        block1 = block(width/2+2-48,53,GREEN)
        block2 = block(width/2+2-48,53+48,GREEN)
        block3 = block(width/2+2-48*2,53+48,GREEN)
    #stick
    elif (nextShape == 4):
        block0 = block(width/2+2,53,RED)
        block1 = block(width/2+2,53+48,RED)
        block2 = block(width/2+2,53+48*2,RED)
        block3 = block(width/2+2,53+48*3,RED)
    #elel
    elif (nextShape == 5):
        block0 = block(width/2+2,53,MAGENTA)
        block1 = block(width/2+2,53+48,MAGENTA)
        block2 = block(width/2+2,53+48*2,MAGENTA)
        block3 = block(width/2+2-48,53+48*2,MAGENTA)
    #eler
    elif (nextShape == 6):
        block0 = block(width/2+2,53,YELLOW)
        block1 = block(width/2+2,53+48,YELLOW)
        block2 = block(width/2+2,53+48*2,YELLOW)
        block3 = block(width/2+2+48,53+48*2,YELLOW)
    
    activeBlocks[0] = block0
    activeBlocks[1] = block1
    activeBlocks[2] = block2
    activeBlocks[3] = block3    
    nextShape = random.randrange(0,7)

def drawGrid():
    for i in range(21):              # x         y        width  height
        pygame.draw.rect(screen,GRAY,[717, 48 + 48*i, 1920/3-48*3-11, 5],1)
    for i in range(11):
        pygame.draw.rect(screen,GRAY,[717 + 48*i, 48, 5, 48*20],1)    

def moveActiveBlocksDown():
    for bloque in activeBlocks:
        bloque.y +=48
    
def moveActiveBlocks():
    if(direction == 1 and checkSafeMoveR() == True):
        for bloque in activeBlocks:
            bloque.x +=48    
    elif(direction == -1 and checkSafeMoveL() == True):
        for bloque in activeBlocks:
            bloque.x -=48

def rotate():
    global rotation
    #te
    if(activeBlocks[0].color==CYAN):
        if(rotation == 0):
            activeBlocks[0].x = activeBlocks[1].x +48
            activeBlocks[0].y = activeBlocks[1].y
            activeBlocks[2].x = activeBlocks[1].x
            activeBlocks[2].y = activeBlocks[1].y-48
            activeBlocks[3].x = activeBlocks[1].x
            activeBlocks[3].y = activeBlocks[1].y+48
            rotation += 1
        elif(rotation == 1):
            activeBlocks[0].x = activeBlocks[1].x
            activeBlocks[0].y = activeBlocks[1].y+48
            activeBlocks[2].x = activeBlocks[1].x+48
            activeBlocks[2].y = activeBlocks[1].y
            activeBlocks[3].x = activeBlocks[1].x-48
            activeBlocks[3].y = activeBlocks[1].y
            rotation += 1
        elif(rotation == 2):
            activeBlocks[0].x = activeBlocks[1].x-48
            activeBlocks[0].y = activeBlocks[1].y
            activeBlocks[2].x = activeBlocks[1].x
            activeBlocks[2].y = activeBlocks[1].y+48
            activeBlocks[3].x = activeBlocks[1].x
            activeBlocks[3].y = activeBlocks[1].y-48
            rotation += 1
        elif(rotation == 3):
            activeBlocks[0].x = activeBlocks[1].x
            activeBlocks[0].y = activeBlocks[1].y-48
            activeBlocks[2].x = activeBlocks[1].x-48
            activeBlocks[2].y = activeBlocks[1].y
            activeBlocks[3].x = activeBlocks[1].x+48
            activeBlocks[3].y = activeBlocks[1].y
            rotation = 0
    #square
    elif(activeBlocks[0].color==BLUE):
            rotation = 0
    #zetal
    elif(activeBlocks[0].color==ORANGE):
        if(rotation == 0):
            activeBlocks[0].x = activeBlocks[2].x+48
            activeBlocks[0].y = activeBlocks[2].y
            activeBlocks[1].x = activeBlocks[2].x+48
            activeBlocks[1].y = activeBlocks[2].y-48
            activeBlocks[3].x = activeBlocks[2].x
            activeBlocks[3].y = activeBlocks[2].y+48
            rotation += 1
        elif(rotation == 1):
            activeBlocks[0].x = activeBlocks[2].x
            activeBlocks[0].y = activeBlocks[2].y-48
            activeBlocks[1].x = activeBlocks[2].x-48
            activeBlocks[1].y = activeBlocks[2].y-48
            activeBlocks[3].x = activeBlocks[2].x+48
            activeBlocks[3].y = activeBlocks[2].y
            rotation = 0
    #zetar
    elif(activeBlocks[0].color==GREEN):
        if(rotation == 0):
            activeBlocks[0].x = activeBlocks[2].x-48
            activeBlocks[0].y = activeBlocks[2].y-48
            activeBlocks[1].x = activeBlocks[2].x-48
            activeBlocks[1].y = activeBlocks[2].y
            activeBlocks[3].x = activeBlocks[2].x
            activeBlocks[3].y = activeBlocks[2].y+48
            rotation += 1
        elif(rotation == 1):
            activeBlocks[0].x = activeBlocks[2].x+48
            activeBlocks[0].y = activeBlocks[2].y-48
            activeBlocks[1].x = activeBlocks[2].x
            activeBlocks[1].y = activeBlocks[2].y-48
            activeBlocks[3].x = activeBlocks[2].x-48
            activeBlocks[3].y = activeBlocks[2].y
            rotation = 0       
    #stick
    elif(activeBlocks[0].color==RED):
        if(rotation == 0):
            activeBlocks[0].x = activeBlocks[1].x-48
            activeBlocks[0].y = activeBlocks[1].y
            activeBlocks[2].x = activeBlocks[1].x+48
            activeBlocks[2].y = activeBlocks[1].y
            activeBlocks[3].x = activeBlocks[1].x+48*2
            activeBlocks[3].y = activeBlocks[1].y
            rotation += 1
        elif(rotation == 1):
            activeBlocks[0].x = activeBlocks[1].x
            activeBlocks[0].y = activeBlocks[1].y-48
            activeBlocks[2].x = activeBlocks[1].x
            activeBlocks[2].y = activeBlocks[1].y+48
            activeBlocks[3].x = activeBlocks[1].x
            activeBlocks[3].y = activeBlocks[1].y+48*2
            rotation = 0
    #elel
    elif(activeBlocks[0].color==MAGENTA):
        if(rotation == 0):
            activeBlocks[0].x = activeBlocks[1].x+48
            activeBlocks[0].y = activeBlocks[1].y
            activeBlocks[2].x = activeBlocks[1].x-48
            activeBlocks[2].y = activeBlocks[1].y
            activeBlocks[3].x = activeBlocks[1].x-48
            activeBlocks[3].y = activeBlocks[1].y-48
            rotation += 1
        elif(rotation == 1):
            activeBlocks[0].x = activeBlocks[1].x
            activeBlocks[0].y = activeBlocks[1].y+48
            activeBlocks[2].x = activeBlocks[1].x
            activeBlocks[2].y = activeBlocks[1].y-48
            activeBlocks[3].x = activeBlocks[1].x+48
            activeBlocks[3].y = activeBlocks[1].y-48
            rotation += 1
        elif(rotation == 2):
            activeBlocks[0].x = activeBlocks[1].x-48
            activeBlocks[0].y = activeBlocks[1].y
            activeBlocks[2].x = activeBlocks[1].x+48
            activeBlocks[2].y = activeBlocks[1].y
            activeBlocks[3].x = activeBlocks[1].x+48
            activeBlocks[3].y = activeBlocks[1].y+48
            rotation += 1
        elif(rotation == 3):
            activeBlocks[0].x = activeBlocks[1].x
            activeBlocks[0].y = activeBlocks[1].y-48
            activeBlocks[2].x = activeBlocks[1].x
            activeBlocks[2].y = activeBlocks[1].y+48
            activeBlocks[3].x = activeBlocks[1].x-48
            activeBlocks[3].y = activeBlocks[1].y+48
            rotation = 0    
    #eler            
    elif(activeBlocks[0].color==YELLOW):
        if(rotation == 0):
            activeBlocks[0].x = activeBlocks[1].x+48
            activeBlocks[0].y = activeBlocks[1].y
            activeBlocks[2].x = activeBlocks[1].x-48
            activeBlocks[2].y = activeBlocks[1].y
            activeBlocks[3].x = activeBlocks[1].x-48
            activeBlocks[3].y = activeBlocks[1].y+48
            rotation += 1
        elif(rotation == 1):
            activeBlocks[0].x = activeBlocks[1].x
            activeBlocks[0].y = activeBlocks[1].y+48
            activeBlocks[2].x = activeBlocks[1].x
            activeBlocks[2].y = activeBlocks[1].y-48
            activeBlocks[3].x = activeBlocks[1].x-48
            activeBlocks[3].y = activeBlocks[1].y-48
            rotation += 1
        elif(rotation == 2):
            activeBlocks[0].x = activeBlocks[1].x+48
            activeBlocks[0].y = activeBlocks[1].y
            activeBlocks[2].x = activeBlocks[1].x-48
            activeBlocks[2].y = activeBlocks[1].y
            activeBlocks[3].x = activeBlocks[1].x-48
            activeBlocks[3].y = activeBlocks[1].y-48
            rotation += 1
        elif(rotation == 3):
            activeBlocks[0].x = activeBlocks[1].x
            activeBlocks[0].y = activeBlocks[1].y-48
            activeBlocks[2].x = activeBlocks[1].x
            activeBlocks[2].y = activeBlocks[1].y+48
            activeBlocks[3].x = activeBlocks[1].x+48
            activeBlocks[3].y = activeBlocks[1].y+48
            rotation = 0

direction = 0

def checkBottom():
    for bloque in activeBlocks:
        if (bloque.y >= 869+48*2):
            return True
    return False
def checkOtherBlocks():
    for bloque in activeBlocks:
        for elem in staticBlocks:
            if(elem != None):
                if(abs(elem.y - bloque.y - 48== 0) and elem.x == bloque.x):
                    return True
    return False 

def checkSafeMoveL():
    for bloque in activeBlocks:    
        if(bloque.x==722):
            return False
    for bloque in activeBlocks:
        for elem in staticBlocks:
            if(elem != None):
                if(abs(elem.y - bloque.y == 0) and elem.x - bloque.x == -48):
                    return False
    return True     

def checkSafeMoveR():
    for bloque in activeBlocks:
        if(bloque.x==1154):
            return False
    for bloque in activeBlocks:
        for elem in staticBlocks:
            if(elem != None):
                if(abs(elem.y - bloque.y == 0) and elem.x - bloque.x == 48):
                    return False
    return True     

def safeRotate():
    global rotation
    bx1=activeBlocks[0].x
    by1=activeBlocks[0].y
    bx2=activeBlocks[1].x
    by2=activeBlocks[1].y
    bx3=activeBlocks[2].x
    by3=activeBlocks[2].y
    bx4=activeBlocks[3].x
    by4=activeBlocks[3].y
    rot = rotation
    rotate()
    for blok in activeBlocks:
        for bloque in staticBlocks:
            if (bloque is not None and ((blok.x == bloque.x and blok.y == bloque.y) or blok.x == 722-48 or blok.x == 1154+48)):
                activeBlocks[0].x=bx1
                activeBlocks[0].y=by1
                activeBlocks[1].x=bx2
                activeBlocks[1].y=by2
                activeBlocks[2].x=bx3
                activeBlocks[2].y=by3
                activeBlocks[3].x=bx4
                activeBlocks[3].y=by4
                rotation = rot
                return       
            
def popBlocks(height):
    i=0
    while(i<200):
        if(staticBlocks[i] != None and staticBlocks[i].y==height):
            staticBlocks[i] = None
        i+=1    


def checkLine():
    global score
    i = 0
    done = False
    while(i<20 and not done):
        count=0
        for bloque in staticBlocks:
            if(bloque != None and bloque.y == 965-48*i):
                count +=1
            if(count == 10):
                count = 0
                popBlocks(965-48*i)
                score+=1
                for blok in staticBlocks:
                    if (blok != None and blok.y<965-48*i):
                        blok.y+=48
                done = True
        i+=1

def checkBottomShade(shadeBlocks):
    for bloque in shadeBlocks:
        if (bloque.y == 965):
            return True
    return False
def checkOtherBlocksShade(shadeBlocks):
    for bloque in shadeBlocks:
        for elem in staticBlocks:
            if(elem != None):
                if(abs(elem.y - bloque.y - 48== 0) and elem.x == bloque.x):
                    return True
    return False 

def drawShade(shadeBlocks):
    while(checkBottomShade(shadeBlocks) == False and checkOtherBlocksShade(shadeBlocks) == False):
        for bloque in shadeBlocks:
            bloque.y += 48
    for bloque in shadeBlocks:
        pygame.draw.rect(screen,bloque.color,[bloque.x, bloque.y, 43, 43],3)
    return shadeBlocks

def moveToShade(shadeBlocks):
    i=0
    while(i<4):
        activeBlocks[i].x = shadeBlocks[i].x
        activeBlocks[i].y = shadeBlocks[i].y
        i+=1


def spawnNextShape():
    if (nextShape == 0):
        block0 = block(1600,800,CYAN)
        block1 = block(1600,800+48,CYAN)
        block2 = block(1600-48,800+48,CYAN)
        block3 = block(1600+48,800+48,CYAN)    
    #square
    elif (nextShape == 1):
        block0 = block(1600,800,BLUE)
        block1 = block(1600,800+48,BLUE)
        block2 = block(1600-48,800+48,BLUE)
        block3 = block(1600-48,800,BLUE)
    #zetal
    elif (nextShape == 2):
        block0 = block(1600,800,ORANGE)
        block1 = block(1600-48,800,ORANGE)
        block2 = block(1600,800+48,ORANGE)
        block3 = block(1600+48,800+48,ORANGE)
    #zetar
    elif (nextShape == 3):
        block0 = block(1600,800,GREEN)
        block1 = block(1600-48,800,GREEN)
        block2 = block(1600-48,800+48,GREEN)
        block3 = block(1600-48*2,800+48,GREEN)
    #stick
    elif (nextShape == 4):
        block0 = block(1600,800,RED)
        block1 = block(1600,800+48,RED)
        block2 = block(1600,800+48*2,RED)
        block3 = block(1600,800+48*3,RED)
    #elel
    elif (nextShape == 5):
        block0 = block(1600,800,MAGENTA)
        block1 = block(1600,800+48,MAGENTA)
        block2 = block(1600,800+48*2,MAGENTA)
        block3 = block(1600-48,800+48*2,MAGENTA)
    #eler
    elif (nextShape == 6):
        block0 = block(1600,800,YELLOW)
        block1 = block(1600,800+48,YELLOW)
        block2 = block(1600,800+48*2,YELLOW)
        block3 = block(1600+48,800+48*2,YELLOW)
    
    nextBlocks[0] = block0
    nextBlocks[1] = block1
    nextBlocks[2] = block2
    nextBlocks[3] = block3

counter = 0
adder = 1
limit = 50
pygame.mixer.music.play(-1)
spawn()
spawnNextShape()
scoretext = myfont.render('Score: ', False, (255, 255, 255))

def gameStage(score):
    global limit
    if(score != 0 and score%10 == 0 and score<40):
        limit = 50 - 10*score/10

def checkFailure():
    global running
    global over 
    for block in activeBlocks:
        for blok in staticBlocks:
            if (blok is not None and block.x == blok.x and block.y == blok.y):
                over = True

def gameOver():
    adder = 0
    screen.blit(myfont.render("You lost! Press the r key to restart", False, (255, 255, 255)),(1920/2-350,1080/2))

def restart():
    global limit
    global score
    global over
    limit = 50
    score = 0
    i=0
    while (i < 4):
        activeBlocks[i] = None
        i+=1
    i=0
    while (i < 200):
        staticBlocks[i] = None
        i+=1

    nextShape = random.randrange(0,7)
    spawn()
    spawnNextShape()
    over=False

score = 0
over = False
while running:
    gameStage(score)
    clock.tick(60)
    #screen.blit(bg,(0,0))
    screen.fill(BLACK)
    counter += adder
    direction = 0
    shadeBlocks=copy.deepcopy(activeBlocks)
    shadeBlocks = drawShade(shadeBlocks)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if(not over):
                if event.key == pygame.K_a or event.key == pygame.K_LEFT and adder != 0:
                    direction = -1
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT and adder != 0:
                    direction = 1
                if event.key == pygame.K_w or event.key == pygame.K_UP and adder != 0:
                    safeRotate()
                    #rotate()
                if event.key == pygame.K_SPACE:
                    moveToShade(shadeBlocks)
                    counter = limit
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    if(checkBottom() == False and checkOtherBlocks() == False):
                        moveActiveBlocksDown()
                if event.key == pygame.K_p and not over:
                    if(adder == 1):
                        adder = 0
                        pygame.mixer.music.pause()
                    else:
                        adder = 1
                        pygame.mixer.music.unpause()
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_r:
                restart()
    
    moveActiveBlocks()
    drawGrid()
    
    if(counter >= limit and not over):
        if(checkBottom() == True or checkOtherBlocks() == True):
            for bloque in activeBlocks:
                i=0
                while(i < 200):
                    if(staticBlocks[i] == None):
                        staticBlocks[i] = bloque
                        break
                    i+=1
            spawn()
            spawnNextShape()
            checkFailure() 
        else:
            moveActiveBlocksDown()
        counter = 0  
    checkLine()
    for bloque in activeBlocks:
        pygame.draw.rect(screen,bloque.color,[bloque.x, bloque.y, 43, 43],0)              
    for bloque in staticBlocks:
        if(bloque != None):
            pygame.draw.rect(screen,bloque.color,[bloque.x, bloque.y, 43, 43],0)
    for bloque in nextBlocks:
        pygame.draw.rect(screen,bloque.color,[bloque.x, bloque.y, 43, 43],0)              
    screen.blit(scoretext,(100,800))
    scorerender = myfont.render(str(score), False, (255, 255, 255))
    screen.blit(scorerender,(280,800))
    if(over == True):
        gameOver()
        
    pygame.display.update()
    del shadeBlocks

pygame.quit()