from tkinter import *
from PIL import ImageTk as imk
import classroom1_1
import item_c
import map
cnt_getitem = 0
class LOCKER2:
    def __init__(self, lk2):
        self.lk2 = lk2
        global cnt_getitem

        self.lk2_ill = imk.PhotoImage(file="illust/교실/사물함_안.jpg") #빈사물함함
        self.lk2_itemon = imk.PhotoImage(file = "illust/교실/사물함_안_아이템있.jpg") #아이템 있는 사물함
        self.lk2_item_o = Label(self.lk2, image = self.lk2_itemon)
        self.lk2_item_o.place(x = -2, y = -2)
        # self.lk2_il = Label(self.lk2, image=self.lk2_ill)
        # self.lk2_il.place(x=-2, y=-2)


        #아이템을 얻었다는 알림 뜨기 !!

        if cnt_getitem == 0:
            cnt_getitem+=1

            map.Map_gone.inven.append('거울')
            map.Map_gone.inven.append('목도리')
            map.Map_gone.inven.append('보온병')
        else:
            self.lk2_item_o.config(image = self.lk2_ill)

        Backbtn = Button(self.lk2, text="돌아가기", command=self.movBack)
        Backbtn.place(x=1070, y=600)


    def movBack(self):
        classroom1_1.CLASSROOM1_1(self.lk2)