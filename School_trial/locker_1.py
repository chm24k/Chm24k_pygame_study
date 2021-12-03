from tkinter import *
from PIL import ImageTk as imk
import classroom1_1
import locker_2
import locker1_2
import map

class LOCKER1:
    def __init__(self,lk1):
        self.lk1 = lk1

        self.lk1_ill = imk.PhotoImage(file="illust/교실/사물함.jpg")
        self.lk1_il = Label(self.lk1, image=self.lk1_ill)
        self.lk1_il.place(x=-2, y=-2)

        self.lk1_go = imk.PhotoImage(file="illust/교실/1_1사물함내부로버튼.png")
        imgbtn = Button(image=self.lk1_go, command=self.locker_inside)
        imgbtn.place(x=508, y=46)

        self.lock0723 = imk.PhotoImage(file="illust/교실/0723.png")
        lock0723btn = Button(image=self.lock0723, command=self.locker2_inside)
        lock0723btn.place(x=24, y=257)







        Backbtn = Button(self.lk1, text="돌아가기", command=self.movBack)
        Backbtn.place(x=1070, y=600)

    def locker_inside(self):
        if '사물함 비번쪽지' in map.Map_gone.inven:
            print("존재")
            locker_2.LOCKER2(self.lk1)
        else:
            self.saylabel = Label(self.lk1, text = "비밀번호 쪽지가 필요하다.")
            self.saylabel.place(x = 605, y = 504)

    def locker2_inside(self):
        self.lock0723label = imk.PhotoImage(file="illust/교실/비밀번호힌트.png")
        self.hint_label = Label(self.lk1, image = self.lock0723label)
        self.hint_label.place(x = 14, y = 174)

        self.ent = Entry(self.lk1, width=10)
        self.ent.insert(END, "□□□□")
        self.ent.place(x = 50, y = 300)

        btn = Button(self.lk1, text = "확인", command = self.answer_ch)
        btn.place(x = 110, y =300)



    def answer_ch(self):

        self.ans = self.ent.get()
        if self.ans == "0723":
            locker1_2.LOCKER1_2(self.lk1)

    def movBack(self):
        classroom1_1.CLASSROOM1_1(self.lk1)