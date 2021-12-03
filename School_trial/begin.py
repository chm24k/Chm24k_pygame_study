#시작페이지
# 시작버튼, 배경

from tkinter import *
import map
import pygame

pygame.init()
pygame.mixer.music.load("나의 이름은.mp3")
pygame.mixer.music.play(-1)

class BEGIN:
    def __init__(self,rot):
        self.rot = rot


        self.begin_ill = PhotoImage(file ="illust/시작화면/시작화면.png")
        self.begin_a = Label(image = self.begin_ill)
        self.begin_a.place(x = -2, y = -2)

        self.startbtn = Button(self.rot, text="시작하기", command=self.map_go)
        self.startbtn.place(x=280, y=500)


        #
        # self.btn1 = Button(self.rot, text = "▶", command = self.sound_window)
        # self.btn1.place(x =600, y = 500)


    def map_go(self):
        map.Map_gone(self.rot)

    def play(self):
        self.rot.mainloop()


if __name__ == '__main__':
    rot = Tk()
    rot.title("학교재판")
    rot.geometry("1200x660+150+80")
    rot.resizable(False,False)

    BEGIN(rot).play()