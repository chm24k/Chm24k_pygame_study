#2층 맵
# 복도, 복도창가, ##미술실, 과학실, 도서관, 음악실
from tkinter import *
import map
import art_room
import lab_room
import library
import floor2_2
class Floor2:
    def __init__(self,f2):
        self.f2 = f2

        self.f2_ill = PhotoImage(file = "illust/시작화면/맵2층.png")
        self.f2_il = Label(self.f2, image = self.f2_ill)
        self.f2_il.place(x = -2, y = -2)


        self.f2_artroom = PhotoImage(file = "illust/시작화면/art.png")
        self.f2_art = Label(self.f2, image = self.f2_artroom)
        self.f2_art.place(x = 100, y = 140)

        self.f2_scienceroom = PhotoImage(file = "illust/시작화면/science.png")
        self.f2_science = Label(self.f2, image = self.f2_scienceroom)
        self.f2_science.place(x = 460, y = 140)

        self.f2_library_c = PhotoImage(file = "illust/시작화면/library.png")
        self.f2_library = Label(self.f2, image = self.f2_library_c)
        self.f2_library.place(x = 820, y = 140)


        one_cls = Button(self.f2, text = "미술실", command = self.go_artroom, padx = 30, pady = 10)
        one_cls.place(x = 200, y=500)

        two_cls = Button(self.f2, text = "과학실",command = self.go_labroom, padx = 30, pady = 10)
        two_cls.place(x = 560, y=500)


        if '도서관열쇠' in map.Map_gone.inven:
            three_cls = Button(self.f2, text = "도서관",command = self.go_library, padx = 30, pady = 10)
            three_cls.place(x = 920, y=500)
        else:
            label2 = Label(self.f2, text="열쇠필요")
            label2.place(x=920, y=500)

        nextpgbtn = Button(self.f2, text = "▶", command = self.nextpage, padx = 20, pady = 20)
        nextpgbtn.place(x = 1100, y = 250)

        Backbtn = Button(self.f2, text="돌아가기", command=self.movBack)
        Backbtn.place(x=1070, y=600)


    def go_artroom(self):
        art_room.ARTROOM(self.f2)

    def go_labroom(self):
        lab_room.LABROOM(self.f2)

    def go_library(self):
        library.LIBRARY(self.f2)

    def nextpage(self):
        floor2_2.FloorNEXT2(self.f2)
    def movBack(self):
        map.Map_gone(self.f2)
