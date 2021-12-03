
from tkinter import *
from PIL import ImageTk as imk
import lab_room
import window_plust
import map
import blood_eye

lab2_cnt = 0
cnt_ch1 = 'none'
cnt_ch2 = 'none'
cnt_ch3 = 'none'
class LAB2:
    def __init__(self, lab2):
        self.lab2 = lab2
        global cnt_ch1, cnt_ch2, cnt_ch3
        self.lab2_p_shape = imk.PhotoImage(file="illust/과학실/모형/기본모형.png")
        self.lab2_p = Label(self.lab2, image=self.lab2_p_shape)
        self.lab2_p.place(x=-2, y=-2)

        if lab2_cnt == 0:
            nextbtn = Button(self.lab2, text="▼", command=self.talk_sci_1)
            nextbtn.place(x=1126, y=445)
        elif lab2_cnt ==1:
            if '썬글라스' in map.Map_gone.inven:
                cnt_ch1 ='A'
            if '목도리' in map.Map_gone.inven:
                cnt_ch2 ='B'
            if '겉옷' in map.Map_gone.inven:
                cnt_ch3 = 'C'


            if cnt_ch1 =='A' and cnt_ch2=='B' and cnt_ch3 =='C':
                self.talk_cloth_all = imk.PhotoImage(file="illust/과학실/모형/모든옷.png")
                self.lab2_p2 = Label(self.lab2, image = self.talk_cloth_all)
                self.lab2_p2.place(x = -2, y = -2)


                nextbtn = Button(self.lab2, text="▼", command=self.change4s)
                nextbtn.place(x=1126, y=445)

        elif lab2_cnt ==2:
            self.talk_cloth_all = imk.PhotoImage(file="illust/과학실/모형/모든옷.png")
            self.lab2_p.config(image=self.talk_cloth_all)

        Backbtn = Button(self.lab2, text="돌아가기", command=self.movBack)
        Backbtn.place(x=1070, y=600)

    def talk_sci_1(self):

        self.talk_w_shp = imk.PhotoImage(file="illust/과학실/모형/sci_talk1.png")
        self.talk1 = Label(self.lab2, image=self.talk_w_shp)
        self.talk1.place(x=-2, y=-2)
        nextbtn = Button(self.lab2, text="▼", command=self.change1s)
        nextbtn.place(x=1126, y=445)

    def change1s(self):
        self.talk_w_shp2 = imk.PhotoImage(file="illust/과학실/모형/sci_talk2.png")
        self.talk2 = Label(self.lab2, image=self.talk_w_shp2)
        self.talk2.place(x=-2, y=-2)

        nextbtn = Button(self.lab2, text="▼", command=self.change2s)
        nextbtn.place(x=1126, y=445)

    def change2s(self):
        self.talk_w_shp3 = imk.PhotoImage(file="illust/과학실/모형/sci_talk3.png")
        self.talk3 = Label(self.lab2, image=self.talk_w_shp3)
        self.talk3.place(x=-2, y=-2)

        nextbtn = Button(self.lab2, text="▼", command=self.change3s)
        nextbtn.place(x=1126, y=445)

    def change3s(self):
        global lab2_cnt
        self.talk_w_shp4 = imk.PhotoImage(file="illust/과학실/모형/sci_talk4.png")
        self.talk4 = Label(self.lab2, image=self.talk_w_shp4)
        self.talk4.place(x=-2, y=-2)
        lab2_cnt = 1
        nextbtn = Button(self.lab2, text="▼", command=self.movBack)
        nextbtn.place(x=1126, y=445)

    def change4s(self):
        self.talk_w_shp5 = imk.PhotoImage(file="illust/과학실/모형/sci_talk5.png")
        self.talk5 = Label(self.lab2, image=self.talk_w_shp5)
        self.talk5.place(x=-2, y=-2)

        nextbtn = Button(self.lab2, text="▼", command=self.change5s)
        nextbtn.place(x=1126, y=445)

    def change5s(self):
        self.talk_w_shp6 = imk.PhotoImage(file="illust/과학실/모형/sci_talk6.png")
        self.talk6 = Label(self.lab2, image=self.talk_w_shp6)
        self.talk6.place(x=-2, y=-2)

        nextbtn = Button(self.lab2, text="▼", command=self.change6s)
        nextbtn.place(x=1126, y=445)

    def change6s(self):
        global lab2_cnt
        self.talk_w_shp7 = imk.PhotoImage(file="illust/과학실/모형/sci_talk7.png")
        self.talk7 = Label(self.lab2, image=self.talk_w_shp7)
        self.talk7.place(x=-2, y=-2)

        map.Map_gone.inven.append('도서관열쇠')
        lab2_cnt=2
        nextbtn = Button(self.lab2, text="▼", command=self.movBack)
        nextbtn.place(x=1126, y=445)


    def movBack(self):
        lab_room.LABROOM(self.lab2)
