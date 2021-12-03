from tkinter import *
from PIL import ImageTk as imk
import floor1
import map

get_blank_w = 0
class CLASSROOM1_2:
    def __init__(self,c2):
        self.c2 = c2
        global get_blank_w
        self.c2_ill = imk.PhotoImage(file="illust/교실/교실칠판전경.jpg")
        self.c2_il = Label(self.c2, image=self.c2_ill)
        self.c2_il.place(x=-2, y=-2)

        if get_blank_w ==0:
            self.blank_write = imk.PhotoImage(file="illust/교실/빈편지지.jpg")
            self.blankwritebtn = Button(image = self.blank_write, command =lambda :self.blank_w(self.blankwritebtn))
            self.blankwritebtn.place(x = 253, y = 395)


        Backbtn = Button(self.c2, text="돌아가기", command=self.movBack)
        Backbtn.place(x=1070, y=600)

    def blank_w(self,event):
        global get_blank_w
        get_blank_w+=1
        map.Map_gone.inven.append('빈 편지지')
        event.place_forget()
    def movBack(self):
        floor1.Floor1(self.c2)
