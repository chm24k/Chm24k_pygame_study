import tkinter
from tkinter import messagebox

from tictactoe_gameengine import TictactoeGameEngine

class TictactoeGUI:
    def __init__(self):
        self.game_engine = TictactoeGameEngine()
        self.init_GUI()


    def init_GUI(self): #화면구성하는거 넣을거임
        self.CANVAS_SIZE = 300
        self.root = tkinter.Tk()  #창
        self.root.title('틱택토')  #타이틀명
        self.root.geometry(f'{self.CANVAS_SIZE}x{self.CANVAS_SIZE}') #여기선 문자열임 # 창크기지정
        self.root.resizable(width=False, height=False) #사이즈 변경금지
        #                              내컴퓨터     하얀색             가로길이                        세로길이
        self.canvas = tkinter.Canvas(self.root, bg = 'white', width = self.CANVAS_SIZE, height = self.CANVAS_SIZE) #도화지 생성

        self.canvas.pack() #포장하다

        #이미지 지정
        self.images = {}        #{'X': PhotoImage객체, 'O': PhotoImage객체}
        self.images['X'] = tkinter.PhotoImage(file = 'X.gif')
        self.images['O'] = tkinter.PhotoImage(file = 'O.gif')

        # bind 연결하다     Button-1(문자열임) 클릭하면 이벤트 발생!  click_handler에서 ()치면안됨 바로 실행되어버려서..XXXXXxx
        self.canvas.bind('<Button-1>', self.click_handler)  #********시험에 나올확률 UP!


        self.root.mainloop() #창 맨 마지막에 나와야함


    def click_handler(self, event): #클릭처리기  - event넣어짐
        #print(f'{event.x},{event.y}')


        row, col = self.coordinate_to_position(event.x, event.y)
        # set row, col
        self.game_engine.set(row, col)

        # show_board
        self.game_engine.show_board()
        self.draw_board()

        # set winner
        winner = self.game_engine.set_winner()
        #승자가 있거나 무승부이면, 게임오버, 결과 표시하자
        if winner == 'O' or winner == 'X':
            messagebox.showinfo('Game Over', f'{winner}이(가) 이겼습니다!')
            self.root.quit()
        elif winner =='d':  #무승부
            messagebox.showinfo('Game Over', f'무승부입니다!')
            self.root.quit()
        #change_turn
        self.game_engine.change_turn()


    def draw_board(self):
        TILE_SIZE = self.CANVAS_SIZE //self.game_engine.SIZE # 300//3 = 100
        x = 0
        y = 0

        for i, v in enumerate(self.game_engine.board):
            if v == '.':
                pass
            else: # elif v == 'X' or v=='O':
                self.canvas.create_image(x, y, anchor = 'nw', image = self.images[v])

            x += TILE_SIZE

            if i% self.game_engine.SIZE == self.game_engine.SIZE-1:
                x = 0
                y+= TILE_SIZE


    def coordinate_to_position(self, x, y):
        print(x,y)
        #return int(y / 100) + 1, int(x / 100) + 1   #y값과 x값을 100으로 나누고 나머지 버림
        return y//(self.CANVAS_SIZE //self.game_engine.SIZE) +1, x//(self.CANVAS_SIZE //self.game_engine.SIZE)+1


# #IF 6줄
#         if 0<=y <100:
#             row = 1
#         elif 100<=200:
#             row = 2
#
#
#         if 0<=x <100:
#             col = 1
#




# IF문 9개사용
        # if 0<=x<100 and 0<=y<100:return 1, 1
        # if 100<=x<200 and 0<=y<100:return 1, 2
        # if 200<=x<300 and 0<=y<100:return 1, 3
        #
        # if 0 <= x < 100 and 100<=y<200:return 2, 1
        # if 100 <= x < 200 and 100<=y<200:return 2, 2
        # if 200 <= x < 300 and 100<=y<200:return 2, 3
        #
        # if 0 <= x < 100 and 200 <= y < 300: return 3, 1
        # if 100 <= x < 200 and 200 <= y < 300: return 3, 2
        # if 200 <= x < 300 and 200 <= y <300: return 3, 3




        return


if __name__ == '__main__':
    ttt_GUI = TictactoeGUI()


