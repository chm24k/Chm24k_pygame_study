# 교실  #옥상전
# 복도창가 #교실(사물함) #정원    /    #미술실 #교실(칠판) #과학실 #도서관
#음악실

from tkinter import *
import begin
import floor1
import floor2
import floor3
import item_c
import garden
import lab_2
class Map_gone:
    inven = []
    if '『따뜻한 국화』' in inven:
        inven.remove('보온병')
        inven.remove('차가운 국화')

    if '『누군가의 진심이 담긴 편지』' in inven:
        inven.remove('잉크')
        inven.remove('빈 편지지')
        inven.remove('오래된 진심')

    if lab_2.lab2_cnt ==2:
        inven.remove('썬글라스')
        inven.remove('목도리')
        inven.remove('겉옷')

    def __init__(self,map):
        self.map = map



        self.map_ill = PhotoImage(file = "illust/시작화면/맵.png")
        self.map_ill_a = Label(self.map, image = self.map_ill)
        self.map_ill_a.place(x = -2, y = -2)



        Backbtn = Button(self.map, text="돌아가기", command=self.movBack)
        Backbtn.place(x=1070, y=600)

        floor1btn = Button(self.map, text = "1층", command = self.floor1_go, padx = 20, pady = 20)
        floor1btn.place(x = 1070, y=120)

        floor2btn = Button(self.map, text = "2층", command = self.floor2_go, padx = 20, pady = 20)
        floor2btn.place(x = 1070, y=300)

        floor3btn = Button(self.map, text = "3층", command = self.floor3_go, padx = 20, pady = 20)
        floor3btn.place(x = 1070, y=480)

        floor4btn = Button(self.map, text = "정원", command = self.floor4_go, padx = 20, pady = 20)
        floor4btn.place(x = 600, y=480)

        item_checkbtn = Button(self.map, text = "아이템", command = self.item_check, padx = 20, pady = 20)
        item_checkbtn.place(x = 1060, y=30)


    def floor1_go(self):
        floor1.Floor1(self.map)

    def floor2_go(self):
        floor2.Floor2(self.map)

    def floor3_go(self):
        floor3.Floor3(self.map)

    def floor4_go(self):
        garden.GARDEN(self.map)

    def item_check(self):
        item_c.ITEMCHECK(self.map)




    def movBack(self):
        begin.BEGIN(self.map)



