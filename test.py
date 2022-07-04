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


class ball:
    def __init__(self):
        self.x = random.randrange(0,1920)
        self.y = random.randrange(0,1080)
        self.size = random.randrange(20,40)


def drawTest(x,y,size):
     pygame.draw.circle(screen,BLUE,(x,y),size)

while running:
    clock.tick(60)
    #screen.blit(bg,(0,0))
    screen.fill(BLACK)
    temp = ball()
    drawTest(temp.x,temp.y,temp.size)
    temp = ball()
    drawTest(temp.x,temp.y,temp.size)
    temp = ball()
    drawTest(temp.x,temp.y,temp.size)
    temp = ball()
    drawTest(temp.x,temp.y,temp.size)
    drawGrid()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

pygame.quit()