from tkinter import *
from PIL import ImageTk as imk
import floor3
import upside
import map
cnt_get_real = 0

class UPSIDE2:
    def __init__(self, up2):
        self.up2 = up2
        global cnt_get_real
        self.up1_1 = imk.PhotoImage(file="illust/야외/옥상계단.jpg")
        self.upup = Label(self.up2, image=self.up1_1)
        self.upup.place(x=-2, y=-2)

        if cnt_get_real == 0:
            self.btnup = imk.PhotoImage(file="illust/야외/오래된진심버튼.png")
            self.table_btn = Button(image=self.btnup, command=lambda: self.see_real(self.table_btn))
            self.table_btn.place(x=546, y=255)
            cnt_get_real = 1

        Backbtn = Button(self.up2, text="돌아가기", command=self.movBack)
        Backbtn.place(x=1070, y=600)

    def see_real(self, event):
        map.Map_gone.inven.append('오래된 진심')
        event.place_forget()

    def movBack(self):
        upside.UPSIDE(self.up2)