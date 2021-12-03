from tkinter import *
from PIL import ImageTk as imk
import floor3

import map

class MUSIC_ROOM:
    def __init__(self,music):
        self.music = music

        self.musicroom_illust = imk.PhotoImage(file="illust/음악실/음악실.jpg")
        self.musicroom_il = Label(self.music, image=self.musicroom_illust)
        self.musicroom_il.place(x=-2, y=-2)

        # self.lk1_go = imk.PhotoImage(file="illust/교실/1_1사물함내부로버튼.png")
        # imgbtn = Button(image=self.lk1_go, command=self.locker_inside)
        # imgbtn.place(x=508, y=46)








        Backbtn = Button(self.music, text="돌아가기", command=self.movBack)
        Backbtn.place(x=1070, y=600)

    def movBack(self):
        floor3.Floor3(self.music)