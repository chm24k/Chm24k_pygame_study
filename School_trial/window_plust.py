from tkinter import *
from PIL import ImageTk as imk
import map
import hall_to_go
cnt_pap = 0
class WINDOWP:
    def __init__(self,windo):
        self.windo = windo
        global cnt_pap


        self.lab1_room = imk.PhotoImage(file = "illust/복도/복도창문.jpg")
        self.labroom = Label(self.windo, image = self.lab1_room)
        self.labroom.place(x = -2, y = -2)

        if cnt_pap == 0:
            self.choi_pap = imk.PhotoImage(file="illust/복도/최시연 사물함 쪽지버튼.png")
            self.choibtn = Button(image = self.choi_pap, command = lambda: self.get_choi(self.choibtn))
            self.choibtn.place(x = 187, y = 318)
            cnt_pap=1

        Backbtn = Button(self.windo, text="돌아가기", command=self.movBack)
        Backbtn.place(x=1070, y=600)

    def get_choi(self,event):
        map.Map_gone.inven.append('사물함 비번쪽지')
        event.place_forget()
    def movBack(self):
        hall_to_go.LONG_HALL(self.windo)
