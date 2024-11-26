import random



pla_board = [[0 for _ in range(10)] for _ in range(10)]
bot_board = [[0 for _ in range(10)] for _ in range(10)]

pla_possible_ships = []
move = 'player'


#bot chooses where to shoot, based on where a close X is
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


#player creates board
def pla_create_board():
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
                pla_board[x - i][y] = 1
            elif direc == 'right':
                pla_board[x][y + i] = 1
            elif direc == 'bottom':
                pla_board[x + i][y] = 1
            elif direc == 'left':
                pla_board[x][y - i] = 1

#bot creates board
def bot_create_board():
    used_cords = []
    length = 5
    def check_board():
        global length
        correct = False
        while correct == False:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if check_inside(x, y):
                correct = True
        length -= 1

    def check_inside(x, y):
        global length
        end_x = -1
        end_y = -1
        directions = ['r', 'b', 'l', 't']
        for _ in range(4):
            if directions == []:
                return False
            direc = random.choice(directions)
            directions.remove(direc)
            match direc:
                case 'r':
                    end_y = y + length
                    end_x = x
                case 'l':
                    end_y = y - length
                    end_x = x
                case 't':
                    end_y = y
                    end_x = x - length
                case 'b':
                    end_y = y
                    end_x = x + length
            if 0 <= end_x < 10 and 0 <= end_y < 10:
                if other_ships(x, y, length, direc):
                    for c in range(length): ### add cused cords and update board
                        match direc:
                            case 'r':
                                end_y = y + c
                                end_x = x
                            case 'l':
                                end_y = y - c
                                end_x = x
                            case 't':
                                end_y = y
                                end_x = x - c
                            case 'b':
                                end_y = y
                                end_x = x + c
                        used_cords.append((end_x, end_y))
                        bot_board[end_x][end_y] = 1               
                    return True
                continue
        return False
        
    def other_ships(x, y, length, direc):
        for i in range(length):
            match direc:
                case 'r':
                    curr_y = y + i
                    curr_x = x
                case 'l':
                    curr_y = y - i
                    curr_x = x
                case 't':
                    curr_y = y
                    curr_x = x - i
                case 'b':
                    curr_y = y
                    curr_x = x + i
            if (curr_x, curr_y) in used_cords:
                return False
        return True

    for d in range(5):
        check_board()


#prints players board
def pla_print_board():
    print('Player board:')
    print('Bot board:')
    for i in range(10):
        print("|", end="")
        for j in range(10):
            if pla_board[i][j] == 'X':
                print('X', end="|")
            elif pla_board[i][j] == 'O':
                print('O', end="|")
            elif pla_board[i][j] == 1:
                print('1', end="|")
            else:
                print('.', end="|")
        print()
        if i < 9:
            print("-" * 21)

#prints bots board
def bot_print_board():
    print('Bot board:')
    for i in range(10):
        print("|", end="")
        for j in range(10):
            if bot_board[i][j] == 'X':
                print('X', end="|")
            elif bot_board[i][j] == 'O':
                print('O', end="|")
            elif bot_board[i][j] == 1:
                print('1', end="|")
            else:
                print('.', end="|")
        print()
        if i < 9:
            print("-" * 21)








def main():
    pla_create_board()
    bot_create_board()
    

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
            #bot move
            if pla_possible_ships == []:
                x = random.randint(0, 10)
                y = random.randint(0, 10)
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
        pla_print_board()
        bot_print_board()

            














 




