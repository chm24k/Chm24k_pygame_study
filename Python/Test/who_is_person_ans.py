from tkinter import *
root = Tk()
root.title("텍스트입력") # 창 이름
root.geometry("800x400+350+200") #창크기지정 / 고정위치에 생성
a="     "

def btn_ent():
    #엔트리값 출력
    a = ent.get()
    if a=='김미화':
        label.config(text = "『학교에 온지 오래된 원귀』")
    elif a=='우진처':
        label.config(text = "우리학교의 학생")
    else:
        label.config(text = a)

def del_ent():
    #값 지우기
    ent.delete(0,END)

btn = Button(root, text = "확인", command =  btn_ent)
btn.pack()

btn_del = Button(root, text = "삭제", command = del_ent)
btn_del.pack()

label = Label(root, text=a)
label.pack()



ent = Entry(root, width=30)
ent.insert(END, "미리보기입니다.")
ent.pack()



root.mainloop()