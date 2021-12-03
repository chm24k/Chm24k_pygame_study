#1층 맵
# 1-1 #1-2 #1-3
from tkinter import *
import map
import classroom1_1
import classroom1_2

class Floor1:
    def __init__(self,f1):
        self.f1 = f1

        self.f1_ill = PhotoImage(file = "illust/시작화면/맵1층.png")
        self.f1_il = Label(self.f1, image = self.f1_ill)
        self.f1_il.place(x = 0, y = 0)


        self.f1_1_1 = PhotoImage(file = "illust/시작화면/1_1.png")
        self.f1_1 = Label(self.f1, image = self.f1_1_1)
        self.f1_1.place(x = 100, y = 140)

        self.f1_1_2 = PhotoImage(file = "illust/시작화면/1_2.png")
        self.f1_2 = Label(self.f1, image = self.f1_1_2)
        self.f1_2.place(x = 460, y = 140)

        self.f1_1_3 = PhotoImage(file = "illust/시작화면/1_3.png")
        self.f1_3 = Label(self.f1, image = self.f1_1_3)
        self.f1_3.place(x = 820, y = 140)




        one_cls = Button(self.f1, text = "1학년 1반", command = self.go1_1, padx = 30, pady = 10)
        one_cls.place(x = 200, y=500)

        two_cls = Button(self.f1, text = "1학년 2반",command = self.go1_2, padx = 30, pady = 10)
        two_cls.place(x = 560, y=500)

        three_cls = Button(self.f1, text = "1학년 3반",command = self.go1_3, padx = 30, pady = 10)
        three_cls.place(x = 920, y=500)

        Backbtn = Button(self.f1, text="돌아가기", command=self.movBack)
        Backbtn.place(x=1070, y=600)


    def go1_1(self):
        classroom1_1.CLASSROOM1_1(self.f1)

    def go1_2(self):
        classroom1_2.CLASSROOM1_2(self.f1)

    def go1_3(self):
        pass
    def movBack(self):
        map.Map_gone(self.f1)
