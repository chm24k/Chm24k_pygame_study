#2층 맵
# 복도, 복도창가,  음악실
from tkinter import *
import map
import art_room
import floor2
import hall_to_go
from PIL import ImageTk as imk
import library

class FloorNEXT2:
    def __init__(self,f2n):
        self.f2n = f2n
#2층 2번째 페이지
        self.f2_ill = imk.PhotoImage(file = "illust/복도/복도흐림.png")
        self.f2_il = Label(self.f2n, image = self.f2_ill)
        self.f2_il.place(x = -2, y = -2)


        self.f2_artroom = PhotoImage(file = "illust/시작화면/hall복도.png")
        self.f2_art = Label(self.f2n, image = self.f2_artroom)
        self.f2_art.place(x = 100, y = 140)





        four_cls = Button(self.f2n, text = "복도", command = self.go_hall_1, padx = 30, pady = 10)
        four_cls.place(x = 200, y=500)


        nextpgbtn = Button(self.f2n, text = "▶", command = self.nextpage, padx = 20, pady =20)
        nextpgbtn.place(x = 1100, y = 250)

        Backbtn = Button(self.f2n, text="돌아가기", command=self.movBack)
        Backbtn.place(x=1070, y=600)



    def go_hall_1(self):
        hall_to_go.LONG_HALL(self.f2n)

    def nextpage(self):
        floor2.Floor2(self.f2n)


    def movBack(self):
        map.Map_gone(self.f2n)
