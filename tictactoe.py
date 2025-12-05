

                
            

from colorama import init, Fore, Style
import random

init(autoreset=True)

def displayboard(board):
    print()
    def colored(cell):
        if cell == "X":
            return Fore.RED + cell + Style.RESET_ALL
        elif cell == "O":
            return Fore.BLUE + cell + Style.RESET_ALL
        else:
            return Fore.YELLOW + cell + Style.RESET_ALL
    print(colored(board[0]) + '|' + colored(board[1]) + '|' + colored(board[2]))
    print("----")
    print(colored(board[3]) + '|' + colored(board[4]) + '|' + colored(board[5]))
    print("----")
    print(colored(board[6]) + '|' + colored(board[7]) + '|' + colored(board[8]))
    print()

def playerchoice():
    symbol = ""
    while symbol not in ["X", "O"]:
        symbol = input("Do you want to be X or O: ").upper()
    if symbol == "X":
        return ("X", "O")
    else:
        return ("O", "X")

def playmove(board, symbol):
    move = -1
    while move not in range(1, 10) or not board[move - 1].isdigit():
        try:
            move = int(input("Enter your move (1-9): "))
            if move not in range(1, 10) or not board[move - 1].isdigit():
                print("Invalid move. Please try again")
        except ValueError:
            print("Please enter a number between 1-9")
    board[move - 1] = symbol

def aimove(board, aisymbol, playersymbol):
    for i in range(9):
        if board[i].isdigit():
            board_copy = board.copy()
            board_copy[i] = aisymbol
            if checkwn(board_copy, aisymbol):
                board[i] = aisymbol
                return
    for i in range(9):
        if board[i].isdigit():
            board_copy = board.copy()
            board_copy[i] = playersymbol
            if checkwn(board_copy, playersymbol):
                board[i] = aisymbol
                return
    possiblemoves = [i for i in range(9) if board[i].isdigit()]
    move = random.choice(possiblemoves)
    board[move] = aisymbol

def checkwn(board, symbol):
    winconditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for cond in winconditions:
        if board[cond[0]] == board[cond[1]] == board[cond[2]] == symbol:
            return True
    return False

def checkfull(board):
    return all(not spot.isdigit() for spot in board)

def tictactoe():
    print('Welcome to Tic-Tac-Toe!')
    playername = input(f"{Fore.GREEN}Enter your name: {Style.RESET_ALL}")

    while True:
        board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        playersymbol, aisymbol = playerchoice()
        turn = "Player"
        game_on = True

        while game_on:
            displayboard(board)
            if turn == "Player":
                playmove(board, playersymbol)
                if checkwn(board, playersymbol):
                    displayboard(board)
                    print(f'Congratulations {playername}, you have won the game!')
                    game_on = False
                elif checkfull(board):
                    displayboard(board)
                    print("It's a tie!")
                    game_on = False
                else:
                    turn = "AI"
            else:
                aimove(board, aisymbol, playersymbol)
                if checkwn(board, aisymbol):
                    displayboard(board)
                    print("AI won! Better luck next time.")
                    game_on = False
                elif checkfull(board):
                    displayboard(board)
                    print("It's a tie!")
                    game_on = False
                else:
                    turn = "Player"

        playagain = input("Do you want to play again (yes/no): ").lower()
        if playagain != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    tictactoe()