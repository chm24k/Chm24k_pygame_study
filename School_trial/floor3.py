#음악실0 #교무실0 #체육관(체육창고) #옥상으로가는길0 # 옥상

from tkinter import *
from PIL import ImageTk as imk
import map
import music_room
import faculty_room
import upside
class Floor3:
    def __init__(self,f3):
        self.f3 = f3

        self.f3_illust = imk.PhotoImage(file = "illust/음악실/음악실흐림.png")
        self.f3_il = Label(self.f3, image = self.f3_illust)
        self.f3_il.place(x = -2, y = -2)


        self.f2_artroom = PhotoImage(file = "illust/시작화면/music.png")
        self.f2_art = Label(self.f3, image = self.f2_artroom)
        self.f2_art.place(x = 100, y = 140)

        self.f2_scienceroom = PhotoImage(file = "illust/교무실/교무실_숏.png")
        self.f2_science = Label(self.f3, image = self.f2_scienceroom)
        self.f2_science.place(x = 460, y = 140)

        self.f2_library_c = PhotoImage(file = "illust/야외/옥상계단입구_숏.png")
        self.f2_library = Label(self.f3, image = self.f2_library_c)
        self.f2_library.place(x = 820, y = 140)


        one_cls = Button(self.f3, text = "음악실", command = self.go_musicroom, padx = 30, pady = 10)
        one_cls.place(x = 200, y=500)

        two_cls = Button(self.f3, text = "교무실",command = self.go_facultyroom, padx = 30, pady = 10)
        two_cls.place(x = 560, y=500)

        three_cls = Button(self.f3, text = "옥상입구",command = self.go_upstair, padx = 30, pady = 10)
        three_cls.place(x = 920, y=500)

        nextpgbtn = Button(self.f3, text = "▶", command = self.go_musicroom, padx = 20, pady = 20)
        nextpgbtn.place(x = 1100, y = 250)

        Backbtn = Button(self.f3, text="돌아가기", command=self.movBack)
        Backbtn.place(x=1070, y=600)


    def go_musicroom(self):
        music_room.MUSIC_ROOM(self.f3)

    def go_facultyroom(self):
        faculty_room.FACULTY(self.f3)

    def go_upstair(self):
        upside.UPSIDE(self.f3)

    def movBack(self):
        map.Map_gone(self.f3)
