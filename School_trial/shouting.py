from tkinter import *
from PIL import ImageTk as imk
import garden


class SHOUTING1:
    def __init__(self,sh1):
        self.sh1 = sh1
        self.shouting_statue = imk.PhotoImage(file="illust/야외/동상/소리치는동상.png")
        self.shouting_s = Label(self.sh1, image=self.shouting_statue)
        self.shouting_s.place(x=-2, y=-2)



        Backbtn = Button(self.sh1, text="돌아가기", command=self.movBack)
        Backbtn.place(x=1070, y=600)

    def movBack(self):
        garden.GARDEN(self.sh1)
