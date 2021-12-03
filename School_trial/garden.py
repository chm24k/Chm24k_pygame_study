from tkinter import *
from PIL import ImageTk as imk
import map
import violin
import reading
import shouting
import blood_eye
class GARDEN:
    def __init__(self,g1):
        self.g1 = g1
        self.garden_all = imk.PhotoImage(file="illust/야외/정원.jpg")
        self.garden_1 = Label(self.g1, image=self.garden_all)
        self.garden_1.place(x=-2, y=-2)

        self.violin_img = imk.PhotoImage(file="illust/야외/정원버튼/바이올린.png")
        violinbtn = Button(image=self.violin_img, command=self.go_violin)
        violinbtn.place(x=322, y=288)

        self.reading_img = imk.PhotoImage(file="illust/야외/정원버튼/책읽는.png")
        readbtn = Button(image=self.reading_img, command=self.go_reading)
        readbtn.place(x=569, y=337)

        self.blood_eye = imk.PhotoImage(file="illust/야외/정원버튼/피눈물.png")
        bloodbtn = Button(image=self.blood_eye, command=self.go_blood_eye)
        bloodbtn.place(x=650, y=256)

        self.shout_img = imk.PhotoImage(file="illust/야외/정원버튼/소리치는.png")
        shoutbtn = Button(image=self.shout_img, command=self.go_shouting)
        shoutbtn.place(x=435, y=251)



        Backbtn = Button(self.g1, text="돌아가기", command=self.movBack)
        Backbtn.place(x=1070, y=600)



    def go_violin(self):
        violin.VIOLIN(self.g1)

    def go_reading(self):
        reading.READING1(self.g1)

    def go_blood_eye(self):
        blood_eye.BLOOD_EYE1(self.g1)

    def go_shouting(self):
        shouting.SHOUTING1(self.g1)


    def movBack(self):
        map.Map_gone(self.g1)