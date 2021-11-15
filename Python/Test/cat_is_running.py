from tkinter import *

root = Tk()         # 창 띄우기
root.title("변경테스트") # 창 이름


root.geometry("800x400+350+200") #창크기지정 / 고정위치에 생성

#root.resizable(False, False)  #가로*세로 창크기 고정


#--------------------------------------------------------
cat = PhotoImage(file = "test_img\야옹이가달린다.png")
sena = PhotoImage(file = "test_img\세나는영원하다.png")
img1 = PhotoImage(file = "시작버튼.png")

label = Label(root, text = "수정될문장")
img = Label(root, image = img1)

label.pack()
img.pack()


#--------------------------------------
#텍스트
# txt = Text(root, width=30,height=10)  #다중
# txt.pack()
#----------------
#글자를 입력하세요(미리보여줌)
# txt.insert(END, "글자를 입력하세요")
#----------------
#한줄만입력가능한 텍스트창
ent = Entry(root, width=30)
ent.pack()
ent.insert(END, "글자미리보기")

#--------------------------------------------------------


def cat1():
    cat_say = "( •̀ ω •́ )✧ 야옹이가 달린다"
    label.config(text = cat_say)

    global cat
    img.config(image = cat)




def sena1():
    sena_say = "ಠ▃ಠ) 세나는 영원하다!"
    label.config(text = sena_say)

    global sena
    img.config(image = sena)



btn_cat = Button(root, fg = 'black', bg = 'yellow', text = "고양이",command = cat1)
btn_cat.pack()

btn_sena = Button(root, fg = 'green', bg = 'black', text = "영혼", command = sena1)
btn_sena.pack()




root.mainloop()