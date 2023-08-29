import random
import time
board_list = [
    "# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #",
    "#         #         #         #         #         #         #         #         #         #         #",
    "#         #         #         #         #         #         #         #         #         #         #",
    "# 41      # 42      # 43  L2- # 44      # 45      # 46      # 47  S1+ # 48      # 49  L3- # 50      #",
    "# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #",
    "#         #         #         #         #         #         #         #         #         #         #",
    "#         #         #         #         #         #         #         #         #         #         #",
    "# 40      # 39      # 38      # 37  S3+ # 36      # 35  L4- # 34      # 33      # 32      # 31      #",
    "# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #",
    "#         #         #         #         #         #         #         #         #         #         #",
    "#         #         #         #         #         #         #         #         #         #         #",
    "# 21  L2+ # 22      # 23      # 24  S4+ # 25      # 26      # 27  L3+ # 28      # 29      # 30      #",
    "# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #",
    "#         #         #         #         #         #         #         #         #         #         #",
    "#         #         #         #         #         #         #         #         #         #         #",
    "# 20  L4+ # 19      # 18  L1- # 17      # 16  S3- # 15      # 14      # 13      # 12  S2+ # 11      #",
    "# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #",
    "#         #         #         #         #         #         #         #         #         #         #",
    "#         #         #         #         #         #         #         #         #         #         #",
    "# 1       # 2   S1- # 3   L1+ # 4       # 5       # 6   S4- # 7   S2- # 8       # 9       # 10      #",
    "# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #"
]
def row_col():
    dic = dict()
    row = 18
    col = 3
    bool = True
    for i in range(1, 51):
        dic[str(i)] = (row, col)
        if bool:
            col += 10
        else:
            col -= 10

        if i % 10 == 0:
            row -= 4
            if row % 8 != 2:
                col = 93
                bool = False
            else:
                col = 3
                bool = True
    return dic

def board(position):
    k_v = row_col()
    snakes = {'47': '2', '37': '16', '12': '7', '24': '6'}
    ladders = {'3': '18', '20': '35', '21': '43', '27': '49'}
    board_lists = board_list[:]
    for player,pos in position.items():
        if str(pos) in snakes:
            print(player+' is bitten by snake :(')
            pos = snakes[str(pos)]
            position[player] = str(pos)
        if str(pos) in ladders:
            print(player+' is climbed ladder :)')
            pos = ladders[str(pos)]
            position[player] = str(pos)
        r,c = k_v[str(pos)]
        r = int(r)
        c = int(c)
        if board_lists[r][c]!=' ':
            if board_lists[r][c+3]!=' ':
                if board_lists[r-1][c+3]!=' ':
                    board_lists[r-1] = board_lists[r-1][:c]+player+board_lists[r-1][c+2:]
                else:
                    board_lists[r-1] = board_lists[r-1][:c+3] + player + board_lists[r-1][c + 5:]
            else:
                board_lists[r] = board_lists[r][:c+3]+player+board_lists[r][c+5:]
        else:
            board_lists[r] = board_lists[r][:c]+player+board_lists[r][c+2:]
    for i in board_lists:
        print(i)

def introduction():
    print(' hello welcome to the snake and ladder game  :) '.title().center(80,'-'))
    print('')
    print(' red the description before enter into the game '.title().center(80,'-'))
    print('')
    print(' game description '.center(80,'-').upper())
    print('')
    print('maximum 4 player allowed'.title().center(80,' '))
    print('L for Ladder --> L+ --> Ladder Start  L- --> Ladder End'.center(80,' '))
    print('S for Snake -> S+ --> Snake Start  S- --> Sanke End'.center(80,' '))
    print('game starts from 1 to 50'.capitalize().center(80,' '))
    print('lets enter into the game'.capitalize().center(80,' '))
    print('-'*80)
    print('\n')
def if_win(position):
    if any(value == '50' for value in position.values()):
        return True
#Game implementation
introduction()
players = int(input('Enter how many players : '.title()))
while players > 4:
    print('Maximum player is 4')
    players = int(input('Enter how many players : '.title()))
position = {'P'+str(i+1):1 for i in range(players)}
turns = {i+1:'P'+str(i+1) for i in range(players)}
count = 1
while True:
    if count > players:
        count = 1
    board(position)
    print(turns[count]+' Turns')
    in_put = input('press enter to roll the dice'.title())
    if in_put == '':
        dice = random.randint(1,5)
        print('Your dice number is '.title(),dice)
        time.sleep(1)
        if int(position[turns[count]])+dice <= 50:
            position[turns[count]] = str(int(position[turns[count]])+dice)
        if if_win(position):
            board(position)
            print('hey '.title()+turns[count]+' win the match.....'.title())
            print('game over'.center(80,'-').upper())
            break
        count+=1
    else:
        print('press enter to roll dice your entered invalid key'.title())