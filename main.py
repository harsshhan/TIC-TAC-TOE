
import random


class TicTacToe:
    def __init__(self,board) -> None:
        self.board=board
    

    #getting input from the user and assigning the marker to player
    def marker(self):
        while True:
            player1_marker = input("Player 1: Enter your marker 'X' or 'O': ").upper()
            if player1_marker in ('X', 'O'):
                break
            else:
                print("Please enter 'X' or 'O'.")

        if player1_marker == 'X':
            player2_marker = 'O'
        else:
            player2_marker = 'X'
        print(f"Player 1 : {player1_marker}")
        print(f"Player 2 : {player2_marker}")
        
        return player1_marker,player2_marker

    #displaying board
    def show_board(self):
        print('\n')
        print(self.board[0]+'|'+self.board[1]+'|'+self.board[2])
        print('-'*5)
        print(self.board[3]+'|'+self.board[4]+'|'+self.board[5])
        print('-'*5)
        print(self.board[6]+'|'+self.board[7]+'|'+self.board[8])

    # #marking the players marker (X or O)
    # def place_marker(self,marker,position):
    #     self.board[position]=marker

    def win_check(self, mark):
        # Define the winning combinations as tuples of indices
        win_combinations = [
            (6, 7, 8),  # across the top
            (3, 4, 5),  # across the middle
            (0, 1, 2),  # across the bottom
            (6, 3, 0),  # down the left side
            (7, 4, 1),  # down the middle
            (8, 5, 2),  # down the right side
            (6, 4, 2),  # diagonal
            (8, 4, 0)   # diagonal
        ]
        
        # Check if any of the winning combinations contain all 'mark'
        for combination in win_combinations:
            if all(self.board[i] == mark for i in combination):
                return True
        return False

    #check if any space available in board
    def space_check(self):
        if ' ' in self.board:
            return True
        else:
            return False
        
    #player turn --> choosing the position in board
    def player_turn(self, player):
        while True:
            try:
                position = int(input(f"Player {player}: Enter the position (1-9): ")) - 1
                if 0 <= position <= 8 and self.board[position] == ' ':
                    self.board[position] = player
                    break
                else:
                    print("Invalid position. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        
board=[' ']*9
obj=TicTacToe(board)
players=['X','O']
curr_palyer=random.choice(players)
person1,person2=obj.marker()
game=True
while game:
    if obj.space_check():
        obj.show_board()
        obj.player_turn(curr_palyer)
        if obj.win_check(curr_palyer):
            print(f"Congratulations! {curr_palyer} won the game")
            break
        else:
            curr_palyer=players[(players.index(curr_palyer)+1)%2]
        
    else:
        print("-"*20+"[Match Draw]")
        game=False
