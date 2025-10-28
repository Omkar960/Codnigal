boards = {'7': " ",'8': " ","9": " ",
        '4': " ",'5': " ", '6': " ",
        '1':" ",'2': " ", '3': " "}
boardkeys = []

for key in boards:
    boardkeys.append(key)


    
def printboard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def game():
    turn = 'X'
    count = 0

    for i in range(10):
        printboard(boards)
        print("It's your turn"+  turn   +"where do you want to go: ")
        move = input()
        if boards[move] == " ":
            boards[move] = turn
            count+=1
        else:
            print("Pick somewhere else: ")
            continue
        if count >= 5:
            if boards['7'] == boards['8'] == boards['9'] != " ":
                print(boards)
                print("Game over")
                print(turn,"won")
                break
            

            elif boards['4'] == boards['5'] == boards['6'] != " ":
                print(boards)
                print("Game over")
                print(turn,"won")
                break
                

            elif boards['1'] == boards['2'] == boards['3'] != " ":
                print(boards)
                print("Game over")
                print(turn,"won")
                break
            elif boards['1'] == boards['4'] == boards['7'] != " ":
                print(boards)
                print("Game over")
                print(turn,"won")
                break
            elif boards['3'] == boards['6'] == boards['9'] != " ":
                print(boards)
                print("Game over")
                print(turn,"won")
                break
            
            elif boards['7'] == boards['5'] == boards['3'] != " ":
                print(boards)
                print("Game over")
                print(turn,"won")
                break
         
            elif boards['1'] == boards['5'] == boards['9'] != " ":
                print(boards)
                print("Game over")
                print(turn,"won")
                break
            elif boards['2'] == boards['5'] == boards['8'] != " ":
                print(boards)
                print("Game over")
                print(turn,"won")
                break
        if count == 9:
            print("Game over")
            print("It's a tie")
        
        if turn == "X":
            turn = "O"
        else:
            turn = "X"

    restart= input('Do you want to play again,Y or N: ')
    if restart == "Y" or restart == "y":
        for key in boardkeys:
            boards[key] = " "

        game()
if __name__ == "__main__":
    game()

   
   

        
            
        

    
