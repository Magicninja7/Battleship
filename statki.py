import random



letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
pla_board = [[0 for _ in range(10)] for _ in range(10)]
bot_board = [[0 for _ in range(10)] for _ in range(10)]

pla_possible_ships = []
move = 'player'



def axis(xory):
    if xory == 'x':
        x, y = pla_possible_ships[0]
        if pla_board[x-1][y] != 'X' or 'O':
            check_result(x-1, y)
        elif pla_board[x+1][y] != 'X' or 'O':
            check_result(x+1, y)
    else:
        x, y = pla_possible_ships[0]
        if pla_board[x][y-1] != 'X' or 'O':
            check_result(x, y-1)
        elif pla_board[x][y+1] != 'X' or 'O':
            check_result(x, y+1)
    return
            
#check if a shot is a hit or a miss
def check_result(x, y):
    if pla_board[x][y] == 1:
        pla_board[x][y] = 'X'  
        return True  
    else:
        pla_board[x][y] = 'O'
        move = 'player'

        return False
    
    

#check if player won game
def pla_check():
    for i in range(10):
        for j in range(10):
            if pla_board[i][j] == 1:
                return False
    return True

#check if bot won game
def bot_check():
    for i in range(10):
        for j in range(10):
            if bot_board[i][j] == 1:
                return False
    return True





pla_set = []
for i in range(1, 6):
    ship, direc, leng = input(f'ship {i} ({i})').split('|')
    x, y = ship.split(',')
    pla_set.append((x, y, direc, leng))

for ship in pla_set:
    x, y, direc, leng = ship
    x, y = int(x), int(y)
    leng = int(leng)
    
    for i in range(leng):
        if direc == 'top':
            pla_board[y - i][x] = 1
        elif direc == 'right':
            pla_board[y][x + i] = 1
        elif direc == 'bottom':
            pla_board[y + i][x] = 1
        elif direc == 'left':
            pla_board[y][x - i] = 1

# Print the matrix
for row in pla_board:
    print(' '.join(map(str, row)))










def main():
    

    while True:

        while move == 'player':
            #player move
            x, y = int(input('Enter your shot').split(','))
            if bot_board[x][y] == 1:
                print('Hit!')
                bot_board[x][y] = 'X'
                while True:
                    x, y = int(input('Enter your shot').split(','))
                    if bot_board[x][y] == 1:
                        print('Hit!')
                        bot_board[x][y] = 'X'
                    else:
                        print('Miss!')
                        bot_board[x][y] = 'O'
                        move = 'bot'
            else:
                print('Miss!')

        while move == 'bot':
            #bot move###
            if pla_possible_ships == []:
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                if pla_board[x][y] == 1:
                    pla_board[x][y] = 'X'
                else:
                    pla_board[x][y] = 'O'
                    
            elif len(pla_possible_ships) == 1:
                x, y = pla_possible_ships[0]
                if pla_board[x+1][y] != 'X' and pla_board[x+1][y] != 'O':
                    check_result(x+1, y)
                elif pla_board[x-1][y] != 'X' and pla_board[x-1][y] != 'O':
                    check_result(x-1, y)
                elif pla_board[x][y+1] != 'X' and pla_board[x][y+1] != 'O':
                    check_result(x, y+1)
                else:
                    check_result(x, y-1)
            else:
                x, y = pla_possible_ships[0]
                if pla_board[x+1][y] != 'X' and pla_board[x+1][y] != 'O':
                    axis('x')
                elif pla_board[x-1][y] != 'X' and pla_board[x-1][y] != 'O':
                    axis('x')
                elif pla_board[x][y+1] != 'X' and pla_board[x][y+1] != 'O':
                    axis('y')
                else:
                    axis('y')

            print('Player board:')

            print("|", end='')
            for i in range(10):
                for j in range(10):
                    if pla_board[i][j] == 'X':
                        print('X', end='')
                    elif pla_board[i][j] == 'O':
                        print('O', end='')
                    elif pla_board[i][j] == 1:
                        print('1', end='')
                    else:
                        print('.', end='')
                    print("|")
                for _ in range(10):
                    print('-', end='')

            print('Bot board:')
            ###
            print("|", end='')
            for i in range(10):
                for j in range(10):
                    if bot_board[i][j] == 'X':
                        print('X', end='')
                    elif bot_board[i][j] == 'O':
                        print('O', end='')
                    elif bot_board[i][j] == 1:
                        print('1', end='')
                    else:
                        print('.', end='')
                    print("|")
                for _ in range(10):
                    print('-', end='')














 




