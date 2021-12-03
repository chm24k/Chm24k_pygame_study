from tkinter import *
from PIL import ImageTk as imk
import library
import map
cnt = 0
class LIBRARIAN:
    def __init__(self,lib2):
        self.lib2 = lib2
        global cnt
        self.lib2_room = imk.PhotoImage(file = "illust/도서관/도서관_사서자리.jpg")
        self.libr = Label(self.lib2, image = self.lib2_room)
        self.libr.place(x = -2, y = -2)

        if cnt ==0:
            self.book_log = imk.PhotoImage(file="illust/도서관/도서기록일지버튼.png")
            self.booklogbtn = Button(image = self.book_log, command = lambda: self.book_log_get(self.booklogbtn))
            self.booklogbtn.place(x = 392, y = 1)
            cnt=1

        Backbtn = Button(self.lib2, text="돌아가기", command=self.movBack)
        Backbtn.place(x=1070, y=600)


#393*1
    def book_log_get(self,event):
        map.Map_gone.inven.append('『1988 - 독서동아리 활동일지』')
        event.place_forget()
    def movBack(self):
        library.LIBRARY(self.lib2)
