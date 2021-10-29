class TictactoeGameEngine:
    def __init__(self):
        self.board = list('.'*9)    #['.','.','.','.','.','.','.','.','.'] #3*3보드칸의 빈공간 표시
        self.turn = 'x'


    def show_board(self):
        print(self.board)

    def set(self, row, col):
        pass

    def set_winner(self):
        pass
        # ㅡ 3줄
        # ㅣ 3줄


        #/
        #\
        #4씩 더한 index가 같은지
        if self.board[0] == self.board[4] == self.board[8]:
            if self.board == 'O':
                print('O의 승리입니다.')
            elif self.board =='X':
                print('X의 승리입니다.')

        #무승부:  위의 조건 다 통과,
        #더 이상 놓을 자리가 없음==self.board에 빈칸이 없음 : self.board에 '.' 없음


    def change_turn(self):
        pass

if __name__ == '__main__':
    game_engine = TictactoeGameEngine()
    game_engine.show_board()    #...\n...\n...
    game_engine.set(2,2)        #['.','.','.','.','X','.','.','.','.']
    game_engine.show_board()
    game_engine.set(2,1)
    game_engine.set(2,3)        #['.','.','.','X','X','X','.','.','.']
    game_engine.board = ['.','.','.','X','X','X','.','.','.']
    game_engine.set_winner()    # '-'  -> 'X'
    game_engine.change_turn()
    print(game_engine.turn)     # 'O'
    game_engine.change_turn()
    print(game_engine.turn)     # 'X'