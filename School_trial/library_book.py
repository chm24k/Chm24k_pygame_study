from tkinter import *
from PIL import ImageTk as imk
import map
import library
cnt_get_book = 0
class LIBRARY2:
    def __init__(self,lib3):
        self.lib3 = lib3
        global cnt_get_book
        self.lib3_room = imk.PhotoImage(file = "illust/도서관/도서관_책꽂이.jpg")
        self.libroom3 = Label(self.lib3, image = self.lib3_room)
        self.libroom3.place(x = -2, y = -2)


        if cnt_get_book == 0:
            self.btnbook = imk.PhotoImage(file="illust/도서관/기증된책버튼.png")
            self.btnbook_1 = Button(image=self.btnbook, command=lambda: self.book_get(self.btnbook_1))
            self.btnbook_1.place(x=158, y=70)
            cnt_get_book = 1


        Backbtn = Button(self.lib3, text="돌아가기", command=self.movBack)
        Backbtn.place(x=1070, y=600)

    def book_get(self, event):
        map.Map_gone.inven.append('『기증된책』')
        event.place_forget()


    def movBack(self):
        library.LIBRARY(self.lib3)
