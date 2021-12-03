from tkinter import *
from PIL import ImageTk as imk
import floor3

import map
cnt_get_elbum = 0
cnt_get_sunglass = 0
class FACULTY2:
    def __init__(self, fac2):
        self.fac2 = fac2
        global cnt_get_elbum
        global cnt_get_sunglass
        self.faculty_img = imk.PhotoImage(file="illust/교무실/교무실확대.jpg")
        self.fac_img = Label(self.fac2, image=self.faculty_img)
        self.fac_img.place(x=-2, y=-2)

        if cnt_get_elbum ==0:
            self.elbum_img = imk.PhotoImage(file="illust/교무실/졸업앨범.png")
            self.elbum_click = Button(image = self.elbum_img, command =lambda :self.see_elbum(self.elbum_click))
            self.elbum_click.place(x = 781, y = 432)
            cnt_get_elbum =1

        if cnt_get_sunglass ==0:
            self.sumglass_img = imk.PhotoImage(file="illust/교무실/썬글라스버튼.png")
            self.sumglassbtn = Button(image = self.sumglass_img, command =lambda :self.get_sunglass(self.sumglassbtn))
            self.sumglassbtn.place(x = 165, y = 446)
            cnt_get_sunglass =1
        Backbtn = Button(self.fac2, text="돌아가기", command=self.movBack)
        Backbtn.place(x=1070, y=600)

    def see_elbum(self,event):
        map.Map_gone.inven.append('1989년 졸업앨범')
        event.place_forget()


    def get_sunglass(self,event):
        map.Map_gone.inven.append('썬글라스')
        event.place_forget()

    def movBack(self):
        floor3.Floor3(self.fac2)