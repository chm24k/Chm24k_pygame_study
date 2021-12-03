from tkinter import *
from PIL import ImageTk as imk
import floor2
import lab_2
class LABROOM:
    def __init__(self,lab1):
        self.lab1 = lab1
        self.lab1_room = imk.PhotoImage(file = "illust/과학실/과학실.jpg")
        self.labroom = Label(self.lab1, image = self.lab1_room)
        self.labroom.place(x = -2, y = -2)


        self.go_doll = imk.PhotoImage(file="illust/과학실/과학실모형버튼.png")
        dollbtn = Button(image = self.go_doll, command = self.talk_doll)
        dollbtn.place(x = 636, y = 1)

        Backbtn = Button(self.lab1, text="돌아가기", command=self.movBack)
        Backbtn.place(x=1070, y=600)

    def talk_doll(self):
        lab_2.LAB2(self.lab1)
    def movBack(self):
        floor2.Floor2(self.lab1)
