import random









opp_board = [[0 for _ in range(10)] for _ in range(10)]
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
                    opp_board[end_x][end_y] = 1               
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




print('Bot board:')
for i in range(10):
    print("|", end="")
    for j in range(10):
        if opp_board[i][j] == 'X':
            print('X', end="|")
        elif opp_board[i][j] == 'O':
            print('O', end="|")
        elif opp_board[i][j] == 1:
            print('1', end="|")
        else:
            print('.', end="|")
    print()
    if i < 9:
        print("-" * 21)

