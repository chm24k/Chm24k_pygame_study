from tkinter import *
from PIL import ImageTk as imk
import garden
import map
get_eye = 0
get_eye_to_baby = 0
class BLOOD_EYE1:
    def __init__(self,be1):
        global get_eye
        self.be1 = be1
        if get_eye_to_baby == 0:
            self.blood_eye_statue = imk.PhotoImage(file="illust/야외/동상/피눈물흘리는동상.png")
            self.blood_s = Label(self.be1, image=self.blood_eye_statue)
            self.blood_s.place(x=-2, y=-2)
        elif get_eye_to_baby ==1:
            self.blood_eye_statue_end = imk.PhotoImage(file="illust/야외/동상/피눈물흘리는동상_완료.png")
            self.blood_end = Label(self.be1, image=self.blood_eye_statue_end)
            self.blood_end.place(x=-2, y=-2)

        if get_eye ==0:
            self.eye_s = imk.PhotoImage(file="illust/야외/동상/아기눈.png")
            self.eyebtn = Button(image = self.eye_s, command =lambda :self.get_baby_eyes(self.eyebtn))
            self.eyebtn.place(x = 629, y = 500)
            get_eye=1




        Backbtn = Button(self.be1, text="돌아가기", command=self.movBack)
        Backbtn.place(x=1070, y=600)

    def get_baby_eyes(self,event):

        map.Map_gone.inven.append('아기눈')
        event.place_forget()

    def movBack(self):
        garden.GARDEN(self.be1)
