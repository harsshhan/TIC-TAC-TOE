import random
#displaying board
def play_board(board):
    print('\n')
    print(board[1]+'|'+board[2]+'|'+board[3])
    print('-'*5)
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-'*5)
    print(board[7]+'|'+board[8]+'|'+board[9])

#getting input from the user and assigning the marker to player
def marker():
    global p1,p2
    p1=input("Player 1 : Enter your marker 'X' or 'O': ").upper()
    while p1.upper()=='X' or p1.upper()=='O':
        if p1=='X':
            p2='O'
        else:
            p2='X'
        break
    else:
        print("Enter the correct marker: ")
        marker()

#marking the players marker (X or O)
def place_marker(board,marker,position):
    board[position]=marker

#checking if the player win or not
def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

def space_check(board):
    if ' ' in board:
        return True
    else:
        return False


ch=True
while ch:
    print("Welcome to Tic Tac Toe")
    #initialising the board
    board=[' ']*10 
    game=True
    turn=random.randint(1,2)
    marker()
    print(f"Player 1 : {p1}")
    print(f"Player 2 : {p2}")
    print(f"Player {turn} go first")
    play_board(board)
    while game:
        
        #player1
        if turn==1:
            print('\n')
            position=int(input("Player 1 : Enter the position: "))
            if board[position]==' ':
                place_marker(board,p1,position)
                play_board(board)

                if win_check(board,p1):
                    print("Congratulations Player 1 won the game!")
                    ch=False
                    game=False
                else:
                    if space_check(board):
                        turn=2
                    else:
                        print("Match draw")
                        game=False
            else:
                print("Entered position is already occupied")
                turn=1
        #player2
        else:
            print('\n')
            position=int(input("Player 2 : Enter the position: "))
            if board[position]==' ':
                place_marker(board,p2,position)
                play_board(board)

                if win_check(board,p2):
                    print("Congratulations Player 2 won the game!")
                    ch=False
                    game=False
                else:
                    if space_check(board):
                        turn=1
                    else:
                        print("Match draw")
                        game=False
            else:
                print("Entered position is already occupied")
                turn=2