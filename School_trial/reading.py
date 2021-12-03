from tkinter import *
from PIL import ImageTk as imk
import garden


class READING1:
    def __init__(self,re1):
        self.re1 = re1
        self.reading_statue = imk.PhotoImage(file="illust/야외/동상/책읽는동상.png")
        self.reading_s = Label(self.re1, image=self.reading_statue)
        self.reading_s.place(x=-2, y=-2)



        Backbtn = Button(self.re1, text="돌아가기", command=self.movBack)
        Backbtn.place(x=1070, y=600)

    def movBack(self):
        garden.GARDEN(self.re1)
