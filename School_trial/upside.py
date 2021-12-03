from tkinter import *
from PIL import ImageTk as imk
import floor3
import faculty_room_open
import map
import real_truth_heart
class UPSIDE:
    def __init__(self,up1):
        self.up1 = up1
        self.up1_1 = imk.PhotoImage(file="illust/야외/옥상계단입구.jpg")
        self.upup = Label(self.up1, image=self.up1_1)
        self.upup.place(x=-2, y=-2)

        self.btntable = imk.PhotoImage(file="illust/야외/옥상계단책상버튼.png")
        btnt = Button(image=self.btntable, command=self.go_and)
        btnt.place(x=378, y=153)



        Backbtn = Button(self.up1, text="돌아가기", command=self.movBack)
        Backbtn.place(x=1070, y=600)

    def go_and(self):
        real_truth_heart.UPSIDE2(self.up1)






    def movBack(self):
        floor3.Floor3(self.up1)