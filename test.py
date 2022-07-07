import pygame
from pygame.locals import *
import random
import copy


pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 40)
pygame.mixer.music.load("resources/99.mp3")
#bg = pygame.image.load("resources/bg.jpg")
width = 1920
height = 1080
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("test")
clock = pygame.time.Clock()
running = True


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

def drawGrid():
    #draw vertical grid
    for i in range(21):              # x         y        width  height
        pygame.draw.rect(screen,GRAY,[717, 48 + 48*i, 1920/3-48*3-11, 5],1)
    #draw horizontal grid
    for i in range(11):
        pygame.draw.rect(screen,GRAY,[717 + 48*i, 48, 5, 48*20],1)    

#muchas lineas de der a izq y viceversa de color azul (o de todos los colores) que vaya cambiando su glow
#crear array de objetos luz e ir avanzandolos en su direccion y cuando llegan al final ponerles que aparezcan a la misma altura por el otro lado
#cada linea es un rect con una elipse o maybe solo una elipse
#o
#hacer como una onda de color que va cambiando (maybe hacerlo pixelado)

class ball:
    def __init__(self):
        self.x = random.randrange(0,1920)
        self.y = random.randrange(0,1080)
        self.size = random.randrange(20,40)


def drawGlow(x,y,size):
    global glowVal
    global mult
    x = 1000
    y = 500
    pygame.draw.line(screen, (0,glowVal,glowVal), (1000,500), (1050,500), 8)
    pygame.draw.circle(screen,(0,glowVal,glowVal),(999,501),4)
    pygame.draw.circle(screen,(0,glowVal,glowVal),(1051,501),4)
    
    if (glowVal == 254):
        mult = -1
    elif (glowVal == 130):
        mult = 1

    glowVal += mult*2
    print(glowVal)
    #pygame.draw.ellipse(screen, (0,160,160),(x, y,    50, 30))
    #pygame.draw.ellipse(screen, (0,180,180),(x, y+2,  50, 25))
    #pygame.draw.ellipse(screen, (0,200,200),(x, y+5,  50, 20))
    #pygame.draw.ellipse(screen, (0,220,220),(x, y+7,  50, 15))
    #pygame.draw.ellipse(screen, (0,240,240),(x, y+10, 50, 10))
    #pygame.draw.ellipse(screen, (0,255,255),(x, y+12, 50, 5))
    #pygame.draw.ellipse(screen, WHITE,(x, y, 10, 40))
    #pygame.draw.ellipse(screen, BLACK,(x, y, 5, 40))

#def start(self):
    
glowVal = 130
mult = 1
#start()
while running:
    clock.tick(60)
    #screen.blit(bg,(0,0))
    screen.fill(BLACK)
    temp = ball()
    drawGlow(temp.x,temp.y,temp.size)
    #drawGrid()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

pygame.quit()