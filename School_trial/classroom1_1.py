from tkinter import *
from PIL import ImageTk as imk
import floor1
import locker_1
import map
page_change = 0
class CLASSROOM1_1:
    def __init__(self,c1):
        self.c1 = c1
        global page_change


        self.c1_ill = imk.PhotoImage(file="illust/교실/교실전경게시판.jpg")
        self.c1_il = Label(self.c1, image=self.c1_ill)
        self.c1_il.place(x=-2, y=-2)

        self.c1_lock = imk.PhotoImage(file="illust/교실/1_1버튼사물함.png")
        lockergobtn = Button(image = self.c1_lock, command = self.click_locker)
        lockergobtn.place(x = 388, y = 151)


        if page_change == 0:
            self.ink_1 = imk.PhotoImage(file="illust/교실/잉크.jpg")
            self.inkbtn = Button(image=self.ink_1, command=lambda:self.click_ink(self.inkbtn))
            self.inkbtn.place(x=959, y=372)



        Backbtn = Button(self.c1, text="돌아가기", command=self.movBack)
        Backbtn.place(x=1070, y=600)

    def click_ink(self,event):
        global page_change
        page_change += 1
        map.Map_gone.inven.append('잉크')
        event.place_forget()


    def click_locker(self):
        locker_1.LOCKER1(self.c1)
    def movBack(self):
        floor1.Floor1(self.c1)
