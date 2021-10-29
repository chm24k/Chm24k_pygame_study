import random, pygame, sys
from pygame.locals import *

FPS = 30 # 초당 프레임
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
REVEALSPEED = 8 #상자가 보였다가 가려지는 속도
BOXSIZE = 40
GAPSIZE = 10 #상자 사이의 간격
BOARDWIDTH = 10 #아이콘 가로줄 수
BOARDHEIGHT = 7 #아이콘 세로줄 수
assert()