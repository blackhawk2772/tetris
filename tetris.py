import pygame
from pygame.locals import *

pygame.init()
#gg=G

#LOGGER
screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Tetris")
#while True:
#	for event in pygame.event.get():
#		print(event)
#crear objetos, con sus propiedades y a partir de ellas display en screen
#COLORS
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
#VARIABLES
speed = 1080/20 
startx
starty
#192 pxls es un bloque
#pygame.draw.rect(surface, color, rect, width)
#square = pygame.draw.rect(screen, YELLOW, [400, 400, 1080/20*2, 1080/20*2], 2)
#l =
#l_invertida blue
#bar = pygame.draw.rect(screen, RED, [400, 400, 192*4, 1080/20], 2)
#z =	Magenta
#z_invertida w
#t =

#functions
def spawner():
    figure = random.randint(0, 6)
    if(figure == 0){
    	#square	
    	pygame.draw.rect(screen, YELLOW, [400, 400, 1080/20*2, 1080/20*2], 2)
    }else if(figure == 1){
    	#bar
    	pygame.draw.rect(screen, RED, [400, 400, 192*4, 1080/20], 2)
    }else if(figure == 2){
    	#l
    }else if(figure == 3){
    	#l invert
    }else if(figure == 4){
    	#z
    }else if(figure == 5){
    	#z invert
    }else{
    	#t

    }
#lambda func draw figure
#loop
#

running = True
while running:
    screen.fill(BLACK)				#x    y    	

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
#	

pygame.quit()






















