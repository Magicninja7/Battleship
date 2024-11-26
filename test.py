pla_board = [[0 for _ in range(10)] for _ in range(10)]


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