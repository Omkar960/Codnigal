from colorama import init, Fore, Style
import random

init(autoreset = True)

def dislpayboard(board):
    print()
    def colored(cell):
        if cell == "X":
            return Fore.RED + cell+Style.RESET_ALL
        elif cell == "O":
            return Fore.BLUE + cell+Style.RESET_ALL
        else:
            return Fore.YELLOW + cell+Style.RESET_ALL
    print(''+ colored(board[0]) + '|' + colored(board[1]) + '|' + colored(board[2]))

    print("----")
    print(''+ colored(board[3]) + '|' + colored(board[4]) + '|' + colored(board[5]))

    print("----")

    print(''+ colored(board[6]) + '|' + colored(board[7]) + '|' + colored(board[8]))

    print()
def playerchoice():
    symbol = ""

    while symbol not in ["X","O"]:
        symbol = input("Do you want to be X or O")
    if symbol == "X":
        return("X","O")
    else:
        return("O","X")
    
def playmove(board, symbol):
    move = -1

    while move not in range(1,10) or not board[move-1].isdigit():
        try:
            move = int(input("Enter your move (1,9): "))
            if move not in range(1,10) or not board[move-1].isdigit():
                print("Invalid move. Please try again")
        except ValueError:
            print("Please enter a number between 1,9")
         
    board [move-1] = symbol
def aimove(board, aisymobl, playersymbol):
    for i in range(9):
        if board[i].isdigit():
            board_copy = board.copy()
            board_copy[i] = aisymobl
            if checkwin(board_copy, aisymobl):
                board[i] = aisymobl
                return
    for i in range(9):
        if board[i].isdigit():
            board_copy = board.copy()
            board_copy[i] = playersymbol
            if checkwin(board_copy, playersymbol):
                board[i] = aisymobl
                return
        
    possiblemoves = [i for i in range(9) if board[i].isdigit()]
    move = random.choice(possiblemoves)

    board[move] = aisymobl
def checkwn(board, symbol):
    winconditions = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    for cond in winconditions:
        if board[cond[0]] == board[cond[1]] == board[cond[2]] == symbol:
            return True
    return False
def checkfull(board):
    return all(not spot.isdigit() for spot in board)