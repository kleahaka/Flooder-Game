import random , bext , sys
title_types = (0,1,2,3,4,5)
colors_map = {0:"red",1:"green",2:"blue",3:"yellow",4:"cyan",5:"purple"}

board_width = 12
board_height = 10
moves_per_game = 20
left_right = chr(9472)
up_down = chr(9474)
down_right = chr(9484)
down_left = chr(9488)
up_right = chr(9492)
up_left = chr(9496)
block = chr(9608)
def get_new_board():
    board ={}
    for x in range(board_width):
        for y in range(board_height):
            board[(x,y)] = random.choice(title_types)
    for i in range(board_width*board_height):
        x = random.randint(0,board_width-2)
        y = random.randint(0,board_height-1)
        board[(x+1,y)] = board[(x,y)]
    return board

def display_board(board):
    bext.fg("white")
    print(down_right+left_right*board_width + down_left  )
    for y in range(board_height):
        bext.fg("white")
        if y == 0:
            print('>',end = "")
        else:
            print(up_down , end = "")
        for x in range(board_width):
            bext.fg(colors_map[board[(x,y)]])
            print(block , end="")
        bext.fg("white")
        print(up_down)
    print(up_right + left_right*board_width + up_left)

def ask_for_player_move():
    while True:
        bext.fg('white')
        print("Choose one of ", end="")
        bext.fg('red')
        print(" (R)ed", end="")
        bext.fg('green')
        print(" (G)reen", end="")
        bext.fg('blue')
        print(" (B)lue", end="")
        bext.fg('yellow')
        print(" (Y)ellow", end="")
        bext.fg('cyan')
        print(" (C)yan",end="")
        bext.fg('purple')
        print(" (P)urple",end="")
        bext.fg('white')
        print(" or QUIT:")
        response = input("> ").upper()
        if response == "QUIT":
            print("Thanks for playing!")
            sys.exit()
        result = {'R':0,'G':1,'B':2 ,'Y':3,'C':4,'P':5}
        return result[response]
def change_tile(tile_color,board , x , y, color_to_change=None):
    if x == 0 and y == 0 :
        color_to_change = board[(x,y)]
        if tile_color == color_to_change:
            return 
    board[(x,y)] = tile_color
    if x > 0 and board[(x-1,y)]==color_to_change:
        change_tile(tile_color,board,x-1,y,color_to_change)
    if y > 0 and board[(x,y-1)] == color_to_change:
        change_tile(tile_color,board,x,y-1,color_to_change)
    if x < board_width -1 and board[(x+1,y)] == color_to_change:
        change_tile(tile_color,board,x+1,y,color_to_change)
    if y < board_height -1 and board[(x,y+1)]==color_to_change:
        change_tile(tile_color,board,x,y+1,color_to_change)


def has_won(board):
    tile = board[(0,0)]
    for x in range(board_width):
        for y in range(board_height):
            if board[(x,y)] != tile:
                return False
    return True

print("Wellcome to Flooder Game!")
moves_left = moves_per_game
new_board  = get_new_board()
while True:
    display_board(new_board)
    print("Moves left:",moves_left)
    player_move = ask_for_player_move()
    change_tile(player_move,new_board,0,0)
    moves_left -= 1
    if has_won(new_board):
        display_board(new_board)
        print("You have won!")
        break
    elif moves_left == 0:
        display_board(new_board)
        print("You have run out of moves!")
        break
