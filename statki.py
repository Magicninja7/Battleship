import random




pla_board = [[0 for _ in range(10)] for _ in range(10)]
bot_board = [[0 for _ in range(10)] for _ in range(10)]

pla_possible_ships = []
cords_with_ships = []
bots_shots = []
move = 'player'
length = 5
move = 'player'

#sets who starts
def whose_turn():
    global move
    whose = input('Whose turn? b/p (bot/player)')
    while whose not in ['b', 'bot', 'p', 'player']:
        whose = input('Invalid input. Whose turn? b/p (bot/player)')
    if whose in ['b', 'bot']:
        move = 'bot'
    else:
        move = 'player'
    return

#bot chooses where to shoot, based on where a close X is
def choose_axis(x, y):
    cords_with_ships.append((x, y))
    n = len(pla_board)
    visited = [[False] * n for _ in range(n)] 
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Up, down, left, right
    
    queue = [(x, y)]
    visited[x][y] = True

    while queue:
        cx, cy = queue.pop(0)

        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < n: 
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    if pla_board[nx][ny] == 'X':
                        queue.append((nx, ny))
                        cords_with_ships.append((nx, ny))
                    else:
                        continue

    
    if cords_with_ships[0][0] == cords_with_ships[1][0]:
        temp = sorted(cords_with_ships, key=lambda coord: coord[0])
        stx, sty = temp[0]
        endx, endy = temp[-1]
        axis('x', stx, sty, endx, endy)
    else:
        temp = sorted(cords_with_ships, key=lambda coord: (coord[1], coord[0]))
        stx, sty = temp[0]
        endx, endy = temp[-1]
        axis('y', stx, sty, endx, endy)
    
    return
            

#bot chooses where to shoot, based on where a close X is
def axis(xory, stx, sty, endx, endy):
    global move
    if xory == 'x':
        if 0 < sty and pla_board[stx][sty-1] != 'X' and pla_board[stx][sty-1] != 'O':
            bots_shots.append((stx, sty-1))
            if check_result(stx, sty-1):
                pla_possible_ships.append((stx, sty-1))
        elif 9 > endy and pla_board[endx][endy+1] != 'X' and pla_board[endx][endy+1] != 'O':
            bots_shots.append((endx, endy+1))
            if check_result(endx, endy+1):
                pla_possible_ships.append((endx, endy+1))
    elif xory == 'y':
        if 0 < stx and pla_board[stx-1][sty] != 'X' and pla_board[stx-1][sty] != 'O':
            bots_shots.append((stx-1, sty))
            if check_result(stx-1, sty):
                pla_possible_ships.append((stx-1, sty))
        elif 9 > endx and pla_board[endx+1][endy] != 'X' and pla_board[endx+1][endy] != 'O':
            bots_shots.append((endx+1, endy))
            if check_result(endx+1, endy):
                pla_possible_ships.append((endx+1, endy))
    return


def connected(x, y):
    global pla_possible_ships

    n = len(pla_board)
    visited = [[False] * n for _ in range(n)] 
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Up, down, left, right
    
    queue = [(x, y)]
    visited[x][y] = True

    while queue:
        cx, cy = queue.pop(0)

        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < n: 
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    if pla_board[nx][ny] == 'X':
                        queue.append((nx, ny))
                        cords_with_ships.append((nx, ny))
                    elif pla_board[nx][ny] == 1:
                        cords_with_ships.clear()
                        return False
                    else:
                        continue
    
    temp = [item for item in pla_possible_ships if item not in cords_with_ships]
    pla_possible_ships = temp
    return True


#check if a shot is a hit or a miss
def check_result(x, y):
    global move
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
            if bot_board[i][j] == 1:
                return False
    return True

#check if bot won game
def bot_check():
    for i in range(10):
        for j in range(10):
            if pla_board[i][j] == 1:
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
    global length
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


    def near_others(x, y, length, direc):
        def is_in_bounds(a, b):
            return 0 <= a < len(bot_board) and 0 <= b < len(bot_board[0])

        def is_occupied(a, b):
            return is_in_bounds(a, b) and bot_board[a][b] == 1

        # Check if 1s around line
        for i in range(length):
            if direc == 't':
                if is_occupied(x-i, y+1) or is_occupied(x-i, y-1):
                    return False
            elif direc == 'b':
                if is_occupied(x+i, y+1) or is_occupied(x+i, y-1):
                    return False
            elif direc == 'r':
                if is_occupied(x+1, y+i) or is_occupied(x-1, y+i):
                    return False
            elif direc == 'l':
                if is_occupied(x+1, y-i) or is_occupied(x-1, y-i):
                    return False

        # if 1s at start and end point
        if direc == 't':
            if is_occupied(x+1, y) or is_occupied(x-length, y):
                return False
        elif direc == 'b':
            if is_occupied(x-1, y) or is_occupied(x+length, y):
                return False
        elif direc == 'r':
            if is_occupied(x, y-1) or is_occupied(x, y+length):
                return False
        elif direc == 'l':
            if is_occupied(x, y+1) or is_occupied(x, y-length):
                return False

        return True

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
                if other_ships(x, y, length, direc) and near_others(x, y, length, direc):
                    for c in range(length):
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

#prints both boards
def print_whole():
    pla_print_board()
    bot_print_board()

def usage():
    print('You will have 5 ships, each with a length of 1-5. Ships you place cannot be directly adjescent to each other.')
    print('to set your ships, use this format:')
    print('x,y|direction|length')
    print('directions: top, right, bottom, left')
    print('length: 1-5')
    print('example: 1,1|top|3')
    print('to shoot, use this format:')
    print('x,y')


def print_without_revealing():
    print('Opponents board (or rather how you see it). X is a hit ship, O is missed.')
    for i in range(10):
        print("|", end="")
        for j in range(10):
            if bot_board[i][j] == 'X':
                print('X', end="|")
            elif bot_board[i][j] == 'O':
                print('O', end="|")
            else:
                print('.', end="|")
        print()
        if i < 9:
            print("-" * 21)




def main():
    usage()
    pla_create_board()
    bot_create_board()
    global move
    move = 'player'
    whose_turn()
    


    while True:
        #player move
        while move == 'player':
            print_without_revealing()
            x, y = input('Enter your shot').split(',')
            x, y = int(x), int(y)
            if bot_board[x][y] == 1:
                print('Hit!')
                bot_board[x][y] = 'X'
                while True:
                    print_without_revealing()
                    if pla_check():
                        print('Player won!')
                        print_whole()
                        exit()
                    x, y = input('Enter your shot').split(',')
                    x, y = int(x), int(y)
                    if bot_board[x][y] == 1:
                        print('Hit!')
                        bot_board[x][y] = 'X'
                    else:
                        print('Miss!')
                        bot_board[x][y] = 'O'
                        move = 'bot'
            else:
                bot_board[x][y] = 'O'
                print('Miss!')
                move = 'bot'

        #bot move
        while move == 'bot':
            if pla_possible_ships == []:
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                while (x, y) in bots_shots:
                    x = random.randint(0, 9)
                    y = random.randint(0, 9)
                bots_shots.append((x, y))
                if pla_board[x][y] == 1:
                    pla_board[x][y] = 'X'
                    pla_possible_ships.append((x, y))
                else:
                    pla_board[x][y] = 'O'
                    move = 'player'
                    
            elif len(pla_possible_ships) == 1:
                x, y = pla_possible_ships[0]
                if x < 9 and pla_board[x+1][y] != 'X' and pla_board[x+1][y] != 'O':
                    bots_shots.append((x+1, y))
                    if check_result(x+1, y):
                        pla_possible_ships.append((x+1, y))
                elif x > 0 and pla_board[x-1][y] != 'X' and pla_board[x-1][y] != 'O':
                    bots_shots.append((x-1, y))
                    if check_result(x-1, y):
                        pla_possible_ships.append((x-1, y))

                elif y < 9 and pla_board[x][y+1] != 'X' and pla_board[x][y+1] != 'O':
                    bots_shots.append((x, y+1))
                    if check_result(x, y+1):
                        pla_possible_ships.append((x, y+1))
                elif y > 0 and pla_board[x][y-1] != 'X' and pla_board[x][y-1] != 'O':
                    bots_shots.append((x, y-1))
                    if check_result(x, y-1):
                        pla_possible_ships.append((x, y-1))
            else:
                x, y = pla_possible_ships[0]
                choose_axis(x, y)
            for l, m in pla_possible_ships[:]:
                connected(l, m)

            print('Opponent shot!')
            print("this is your board, with your ships and opponent's shots")
            print("Your ships are marked with 1, opponent's hits with X and misses with O")
            pla_print_board()

            if bot_check():
                print('Bot won!')
                print_whole()
                exit()

            
                


            
main()