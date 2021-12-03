from tkinter import *
from PIL import ImageTk as imk
import floor2_2
import window_plust
import map
import blood_eye
baby_find = 0
filename = ["illust/복도/아기귀신대화/talk1.png","illust/복도/아기귀신대화/talk2.png","illust/복도/아기귀신대화/talk3.png"]
choice = 0
class LONG_HALL:
    def __init__(self,h1):
        self.h1 = h1
        self.lab1_room = imk.PhotoImage(file = "illust/복도/복도.jpg")
        self.labroom = Label(self.h1, image = self.lab1_room)
        self.labroom.place(x = -2, y = -2)

        if baby_find ==0:
            self.baby = imk.PhotoImage(file="illust/복도/복도아기귀신.png")
            self.babybtn = Button(image = self.baby, command =lambda :self.give_eye(self.babybtn))
            self.babybtn.place(x = 696, y = 207)

        self.go_win = imk.PhotoImage(file="illust/복도/창문버튼.png")
        winbtn = Button(image = self.go_win, command = self.go_window)
        winbtn.place(x = 957, y = 115)

        Backbtn = Button(self.h1, text="돌아가기", command=self.movBack)
        Backbtn.place(x=1070, y=600)

    def give_eye(self,event):
        self.talk_baby1()

        event.place_forget()

    def talk_baby1(self):


        self.talk_w_baby1 = imk.PhotoImage(file="illust/복도/아기귀신대화/talk1.png")
        self.talk1 = Label(self.h1, image=self.talk_w_baby1)
        self.talk1.place(x=-2, y=-2)
        nextbtn = Button(self.h1, text="▼", command = self.change1)
        nextbtn.place(x=1126, y=445)

    def change1(self):
        self.talk_w_baby2 = imk.PhotoImage(file="illust/복도/아기귀신대화/talk2.png")
        self.talk2 = Label(self.h1, image = self.talk_w_baby2)
        self.talk2.place(x = -2, y = -2)

        nextbtn = Button(self.h1, text="▼", command = self.change2)
        nextbtn.place(x=1126, y=445)

    def change2(self):
        self.talk_w_baby3 = imk.PhotoImage(file="illust/복도/아기귀신대화/talk3.png")
        self.talk3 = Label(self.h1, image = self.talk_w_baby3)
        self.talk3.place(x = -2, y = -2)

        yes_btn = Button(self.h1,text = '> 눈을 준다', padx = 40, pady = 10, command = self.say_yes)
        yes_btn.place(x = 900, y=300)

        no_btn = Button(self.h1,text = '> 눈을 주지 않는다', padx = 40, pady = 10, command = self.say_no)
        no_btn.place(x = 900, y=350)

    def say_yes(self):
        if '아기눈' in map.Map_gone.inven:
            global baby_find
            baby_find = 1
            self.talk_say_YES = imk.PhotoImage(file="illust/복도/아기귀신대화/talk_say_yes.png")
            self.talk5 = Label(self.h1, image=self.talk_say_YES)
            self.talk5.place(x=-2, y=-2)
            blood_eye.get_eye_to_baby = 1

            Backbtn = Button(self.h1, text="돌아가기", command=self.movBack)
            Backbtn.place(x=1070, y=600)

            map.Map_gone.inven.remove('아기눈')
        else:
            self.talk_say_YES_but_NOTHING = imk.PhotoImage(file="illust/복도/아기귀신대화/talk_say_yes_but_nothing.png")
            self.talk5_1 = Label(self.h1, image=self.talk_say_YES_but_NOTHING)
            self.talk5_1.place(x=-2, y=-2)

            nextbtn = Button(self.h1, text="▼", command=self.say_no)
            nextbtn.place(x=1126, y=445)
    def say_no(self):
        if '아기눈' in map.Map_gone.inven:
            self.talk_say_NO = imk.PhotoImage(file = "illust/복도/아기귀신대화/talk_say_no.png")
            self.talk4 = Label(self.h1, image = self.talk_say_NO)
            self.talk4.place(x = -2, y = -2)

            nextbtn = Button(self.h1, text="▼", command=self.say_no_2)
            nextbtn.place(x=1126, y=445)

        else:
            self.talk_say_NO_but_OK = imk.PhotoImage(file="illust/복도/아기귀신대화/talk_say_no_but_ok.png")
            self.talk4_1 = Label(self.h1, image=self.talk_say_NO_but_OK)
            self.talk4_1.place(x=-2, y=-2)

            Backbtn = Button(self.h1, text="돌아가기", command=self.movBack)
            Backbtn.place(x=1070, y=600)




    def say_no_2(self):
        self.talk_say_NO2 = imk.PhotoImage(file="illust/복도/아기귀신대화/이의경도망RED.png")
        self.talk5 = Label(self.h1, image=self.talk_say_NO2)
        self.talk5.place(x=-2, y=-2)

        Backbtn = Button(self.h1, text="돌아가기", command=self.movBack)
        Backbtn.place(x=1070, y=600)


    def go_window(self):
        window_plust.WINDOWP(self.h1)
    def movBack(self):
        floor2_2.FloorNEXT2(self.h1)
