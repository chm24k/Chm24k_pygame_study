from tkinter import *
root = Tk()
root.title("변경테스트")
root.geometry("800x400+350+200")
a = ""
qz = Label(text = "비밀번호를 입력하세요.")
ans = Label(text =f'입력값: {a}')
ans.pack()
qz.pack()



def one():
    global a
    a+="1"

def two():
    global a
    a+="2"

def three():
    global a
    a+="3"

def four():
    global a
    a+="4"

def five():
    global a
    a+="5"





def enter():
    ans.config(text = f'입력값: {a}')
    if a == '135':
        print("문이 열렸다.")

def delete():
    global a
    a = ""
    ans.config(text =f'입력값: {a}')


btn1 = Button(padx = 10, pady = 10, text = "1",command = one)
btn2 = Button(padx = 10, pady = 10, text = "2",command = two)
btn3 = Button(padx = 10, pady = 10, text = "3",command = three)
btn4 = Button(padx = 10, pady = 10, text = "4",command = four)
btn5 = Button(padx = 10, pady = 10, text = "5",command = five)
btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()
btn5.pack()





btn_enter = Button(text = "확인",command = enter)
btn_enter.pack()

btn_del = Button(text = "삭제",command = delete)
btn_del.pack()



root.mainloop()