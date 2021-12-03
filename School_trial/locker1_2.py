from tkinter import *
from PIL import ImageTk as imk
import classroom1_1
import item_c
import map
cnt_get_flower_ice = 0
class LOCKER1_2:
    def __init__(self, lk3):
        self.lk3 = lk3
        global cnt_get_flower_ice

        self.lk3_locker_in = imk.PhotoImage(file="illust/교실/사물함_안.jpg") #빈사물함함
        self.lk2_item_o = Label(self.lk3, image = self.lk3_locker_in)
        self.lk2_item_o.place(x = -2, y = -2)


        if cnt_get_flower_ice ==0:
            self.ice_flower = imk.PhotoImage(file="illust/교실/차가운국화.png")
            self.iceflowerbtn = Button(image = self.ice_flower, command =lambda :self.get_iceflower(self.iceflowerbtn))
            self.iceflowerbtn.place(x = 308, y = 259)
            cnt_get_flower_ice = 1

        Backbtn = Button(self.lk3, text="돌아가기", command=self.movBack)
        Backbtn.place(x=1070, y=600)

    def get_iceflower(self,event):
        map.Map_gone.inven.append('차가운 국화')
        event.place_forget()

    def movBack(self):
        classroom1_1.CLASSROOM1_1(self.lk3)