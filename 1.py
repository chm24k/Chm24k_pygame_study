import pygame, sys          #함수 사용할수 있게
from pygame.locals import * # pygame모듈 다 가져오기

pygame.init()       # 필수수행
DISPLAYSURF = pygame.display.set_mode((400,300))    # 400*300 사이즈로 만든단 말
pygame.display.set_caption('Hello World!')      # 캡션이름
while True: #main game loop
    for event in pygame.event.get():
        if event.type == QUIT:      #만약 event type이  QUIT이면 종료
            pygame.quit()
            sys.exit()
        pygame.display.update()