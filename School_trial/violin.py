from tkinter import *
from PIL import ImageTk as imk
import garden
import map

class VIOLIN:
    def __init__(self,vio):
        self.vio = vio
        self.vio_statue = imk.PhotoImage(file="illust/야외/동상/바이올린켜는동상.png")
        self.vio_s = Label(self.vio, image=self.vio_statue)
        self.vio_s.place(x=-2, y=-2)



        Backbtn = Button(self.vio, text="돌아가기", command=self.movBack)
        Backbtn.place(x=1070, y=600)


    def movBack(self):
        garden.GARDEN(self.vio)
