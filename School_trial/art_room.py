from tkinter import *
from PIL import ImageTk as imk
import floor2
import monarisa
import map
cnt_cloth = 0
class ARTROOM:
    def __init__(self,art1):
        self.art1 = art1

        global cnt_cloth


        self.art1_artroom = imk.PhotoImage(file="illust/미술실/미술실.jpg")
        self.artroom = Label(self.art1, image=self.art1_artroom)
        self.artroom.place(x=-2, y=-2)

        self.clock = imk.PhotoImage(file="illust/미술실/시계.png")
        clockbtn = Button(image = self.clock, command = self.go_clock)
        clockbtn.place(x = 133, y = 121)


        self.statue = imk.PhotoImage(file="illust/미술실/조각상.png")
        statuebtn = Button(image = self.statue, command = self.go_clock)
        statuebtn.place(x = 658, y = 325)

        self.monarisa = imk.PhotoImage(file="illust/미술실/모나리자.png")
        monarisabtn = Button(image = self.monarisa, command = self.go_monarisa)
        monarisabtn.place(x = 44, y = 463)

        if cnt_cloth == 0:
            self.cloth1 = imk.PhotoImage(file="illust/미술실/미술실겉옷버튼.png")
            self.cloth1btn = Button(image = self.cloth1, command = lambda: self.get_cloth(self.cloth1btn))
            self.cloth1btn.place(x = 222, y = 367)
            cnt_cloth=1


        Backbtn = Button(self.art1, text="돌아가기", command=self.movBack)
        Backbtn.place(x=1070, y=600)


    def get_cloth(self,event):
        map.Map_gone.inven.append('겉옷')
        event.place_forget()


    def go_clock(self):
        self.clock_text = Label(self.art1, text = "멈춰있는 시계다. 아마도 고장났겠지.. 4시 53분을 가리키고 있다.")
        self.clock_text.place(x = 400, y = 550)



    def go_monarisa(self):
        monarisa.MONARISA(self.art1)

    def movBack(self):
        floor2.Floor2(self.art1)