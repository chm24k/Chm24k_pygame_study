from tkinter import *
from PIL import ImageTk as imk
import floor3
import faculty_room_open
import map

class FACULTY:
    def __init__(self,fac):
        self.fac = fac

        self.faculty_img = imk.PhotoImage(file="illust/교무실/교무실.jpg")
        self.fac_img = Label(self.fac, image=self.faculty_img)
        self.fac_img.place(x=-2, y=-2)

        self.fac_plus = imk.PhotoImage(file="illust/교무실/교무실확대버튼.png")
        goopenbtn = Button(image=self.fac_plus, command=self.go_open)
        goopenbtn.place(x=514, y=352)








        Backbtn = Button(self.fac, text="돌아가기", command=self.movBack)
        Backbtn.place(x=1070, y=600)

    def go_open(self):
        faculty_room_open.FACULTY2(self.fac)
    def movBack(self):
        floor3.Floor3(self.fac)