from tictactoe_gameengine import TictactoeGameEngine
class TictactoeConsole:
    def __init__(self):
        self.game_engine = TictactoeGameEngine() # init함수 밖에서도 보이게 하기 위해서 self.game_engine이라고 쓴다.
    def play(self):
        # show board
        self.game_engine.show_board()
        # 무한반복
        while(True):
            # input row, col
            row = int(input('행: '))  # ctrl + d 하면 복제됨
            col = int(input('열: '))

            # set row, col
            self.game_engine.set(row, col)
            # show board
            self.game_engine.show_board()
            # set winner
            winner = self.game_engine.set_winner()
            # 승자가 있거나 무승부면, 게임오버, 결과출력
            if winner == 'X' or winner == 'O': #문자열이 있으면 True라서 /  winner와 X를 비교 or winner과 O를 비교
                print(f'{winner} 승리했습니다!🎉')
                break
            elif winner == 'd':
                print('무승부입니다.')
                break
            # change turn
            self.game_engine.change_turn()


if __name__ =='__main__':
    ttt_consol = TictactoeConsole()   #클래스 호출
    ttt_consol.play()  #play 실행

#show board
#무한반복
#  input row, col
#  set row, col
#  show board
#  set winner?
#  승자가 있으면, 끝내고 출력하자
#  change turn