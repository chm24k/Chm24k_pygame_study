from tkinter import *
from PIL import ImageTk as imk
import floor2
import librarian
import library_book
class LIBRARY:
    def __init__(self,lib1):
        self.lib1 = lib1

        self.lib1_room = imk.PhotoImage(file = "illust/도서관/도서관전경.jpg")
        self.libroom = Label(self.lib1, image = self.lib1_room)
        self.libroom.place(x = -2, y = -2)


        self.go_lib_img = imk.PhotoImage(file="illust/도서관/사서자리버튼.png")
        libraryanbtn = Button(image = self.go_lib_img, command = self.go_librarian)
        libraryanbtn.place(x = 11, y = 125)

        self.book_img = imk.PhotoImage(file="illust/도서관/도서버튼.png")
        bookgobtn = Button(image = self.book_img, command = self.go_book_see)
        bookgobtn.place(x = 263, y = 3)


        Backbtn = Button(self.lib1, text="돌아가기", command=self.movBack)
        Backbtn.place(x=1070, y=600)

    def go_librarian(self):
        librarian.LIBRARIAN(self.lib1)

    def go_book_see(self):
        library_book.LIBRARY2(self.lib1)

    def movBack(self):
        floor2.Floor2(self.lib1)
