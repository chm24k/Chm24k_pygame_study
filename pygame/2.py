import pygame, sys
from pygame.locals import *

pygame.init()

#윈도우 설정
DISPLAYSURF = pygame.display.set_mode((400,300), 0, 32)
pygame.display.set_caption('Drawing')

#색상설정
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

#surface 객체상에 그리기
DISPLAYSURF.fill(WHITE)
pygame.draw.polygon(DISPLAYSURF, GREEN, ((146,0), (291,106), (236,277), (56,277), (0,106)))

pixObj = pygame.PixelArray(DISPLAYSURF)
pixObj[380][280] = BLACK
pixObj[382][282] = BLACK
pixObj[384][284] = BLACK
pixObj[386][286] = BLACK
pixObj[388][288] = BLACK
del pixObj


#게임 루프 수행
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()