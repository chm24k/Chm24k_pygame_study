from tkinter import *
from PIL import ImageTk as imk
import art_room
count = 1
class MONARISA:
    def __init__(self,mona):
        self.mona = mona
        global count

        self.monarisa_seeA = imk.PhotoImage(file="illust/미술실/미술실.jpg")
        self.monarisa_seeA_club = imk.PhotoImage(file = "illust/미술실/모나리자A_액자.png")
        self.monarisa_seeB_club = imk.PhotoImage(file = "illust/미술실/모나리자B_액자.png")

        self.monarisaA = Label(self.mona, image=self.monarisa_seeA)
        self.monarisaA.place(x=-2, y=-2)

        if count%2==1: #홀수
            count+=1

            self.C_lab = Label(self.mona, image=self.monarisa_seeA_club)
            self.C_lab.place(x=-2, y=-2)
        else:
            count+=1

            self.D_lab = Label(self.mona, image=self.monarisa_seeB_club)
            self.D_lab.place(x=-2, y=-2)

        Backbtn = Button(self.mona, text="돌아가기", command=self.movBack)
        Backbtn.place(x=1070, y=600)

    def movBack(self):
        art_room.ARTROOM(self.mona)